import os
from pathlib import Path
from dotenv import load_dotenv

from kaggle.api.kaggle_api_extended import KaggleApi
from azure.identity import DefaultAzureCredential
from azure.storage.filedatalake import DataLakeServiceClient

# ---------------------------
# Carregar variáveis do .env
# ---------------------------
load_dotenv()

AZURE_STORAGE_ACCOUNT = os.getenv("AZURE_STORAGE_ACCOUNT") 
AZURE_FILESYSTEM = os.getenv("AZURE_FILESYSTEM", "bronze")  # container
KAGGLE_DATASET = os.getenv("KAGGLE_DATASET")
KAGGLE_FILE = os.getenv("KAGGLE_FILE")      
BRONZE_PREFIX = os.getenv("BRONZE_PREFIX", "kaggle")  # subpasta no bronze

assert AZURE_STORAGE_ACCOUNT, "Defina AZURE_STORAGE_ACCOUNT no .env"
assert KAGGLE_DATASET, "Defina KAGGLE_DATASET no .env"
assert KAGGLE_FILE, "Defina KAGGLE_FILE no .env"

# Diretório local temporário
WORKDIR = Path.cwd() / "data" / "raw"
WORKDIR.mkdir(parents=True, exist_ok=True)
LOCAL_FILE = WORKDIR / KAGGLE_FILE

# Caminho final no ADLS
ADLS_PATH = f"{BRONZE_PREFIX}/{KAGGLE_FILE}"

# ---------------------------
# Função: baixar do Kaggle
# ---------------------------
def download_from_kaggle(dataset: str, filename: str, out_dir: Path):
    print(f"[1/3] Baixando do Kaggle: {dataset} → {filename}")
    api = KaggleApi()
    api.authenticate()  # usa C:\\Users\\<vc>\\.kaggle\\kaggle.json
    api.dataset_download_file(dataset=dataset, file_name=filename, path=str(out_dir), force=True)

    # Se veio zip, extrair
    zip_path = out_dir / f"{filename}.zip"
    if zip_path.exists():
        import zipfile
        with zipfile.ZipFile(zip_path, "r") as zf:
            zf.extractall(out_dir)
        zip_path.unlink()

    print(f"[OK] Arquivo salvo em: {out_dir/filename}")

# ---------------------------
# Função: upload para ADLS
# ---------------------------
def upload_to_adls(storage_account: str, filesystem: str, local_file: Path, dest_path: str):
    print(f"[2/3] Enviando para ADLS: abfss://{filesystem}@{storage_account}.dfs.core.windows.net/{dest_path}")

    credential = DefaultAzureCredential(exclude_shared_token_cache_credential=True)
    service_client = DataLakeServiceClient(
        account_url=f"https://{storage_account}.dfs.core.windows.net",
        credential=credential
    )

    fs_client = service_client.get_file_system_client(filesystem)

    # Cria diretório se não existir
    dir_name = os.path.dirname(dest_path).replace("\\", "/")
    if dir_name and dir_name != ".":
        try:
            fs_client.create_directory(dir_name)
        except Exception:
            pass  # já existe

    # Upload (sobrescreve se já existir)
    file_client = fs_client.get_file_client(dest_path)
    with open(local_file, "rb") as data:
        file_client.upload_data(data, overwrite=True)

    print("[OK] Upload concluído.")

# ---------------------------
# Main
# ---------------------------
if __name__ == "__main__":
    download_from_kaggle(KAGGLE_DATASET, KAGGLE_FILE, WORKDIR)
    upload_to_adls(AZURE_STORAGE_ACCOUNT, AZURE_FILESYSTEM, LOCAL_FILE, ADLS_PATH)

    adls_uri = f"abfss://{AZURE_FILESYSTEM}@{AZURE_STORAGE_ACCOUNT}.dfs.core.windows.net/{ADLS_PATH}"
    print(f"[3/3] Pronto! Arquivo disponível em:\n{adls_uri}")

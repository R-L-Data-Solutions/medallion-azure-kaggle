# Arquitetura Medallion no Azure (Do Zero ao Um)

Este projeto implementa uma arquitetura **Medallion (Bronze → Silver → Gold)** no **Azure Databricks + Data Lake + ADF**, usando dados públicos do Kaggle.

## 🚀 Etapas do Projeto

1. **Conector Kaggle**  
   - Uso da API do Kaggle para ingestão de dataset público.  
   - Script `scripts/kaggle_to_bronze.py`.

2. **Ingestão (Bronze)**  
   - Dados brutos enviados para o **ADLS Gen2** no container *bronze*.  
   - Notebook `01_bronze_ingestao_churn`.

3. **Tratamento (Silver)**  
   - Limpeza, normalização e tratamento de tipos.  
   - Notebook `02_silver_tratamento_churn`.

4. **Apresentação (Gold)**  
   - Dados prontos para consumo analítico e BI.  
   - Notebook `03_gold_apresentacao_churn`.

5. **Governança & Permissões**  
   - Configuração de **IAM, RBAC e Unity Catalog**.  
   - Controle de acesso a schemas e external locations.

6. **Quotas & Compute**  
   - Erros de cluster e ajustes de quota enfrentados durante execução.

7. **Orquestração (ADF)**  
   - Pipeline no Azure Data Factory chamando notebooks do Databricks.  
   - Arquivo `pipelines/adf_pipeline.json`.

8. **Rastreabilidade (Purview)**  
   - Catalogação e lineage para acompanhamento ponta a ponta.  

---

## ⚡ Aprendizados

- Configuração de **roles e grants** foi essencial para liberar acesso.  
- Ajuste de **quotas de compute** no Azure foi necessário para evitar falhas de cluster.  
- Integração Databricks ↔ ADF trouxe orquestração real para o fluxo.  
- Cada erro de permissão/quota fez parte do aprendizado prático.  

---

## 📊 Diagrama

![Arquitetura Medallion](docs/arquitetura_medallion.png)

---

## 🔗 Dataset

- **Telco Customer Churn**: [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

---

## 📌 Como reproduzir

1. Clone o repositório:  
   ```bash
   git clone https://github.com/seuusuario/medallion-azure-kaggle.git

Configure a API do Kaggle (~/.kaggle/kaggle.json).

Ajuste variáveis de ambiente do Azure (.env).

Execute os scripts e notebooks na ordem Bronze → Silver → Gold.

Importe o pipeline do ADF

👤 Autor

Ronaldo Pereira
42 anos | Data Architect & Data Engineer

https://www.linkedin.com/in/ronaldo-pereira-2a71b914a/

E-mail: ronaldooliveira499@gmail.com


---

👉 Esse README já está no ponto pra você jogar no **GitHub**.  
Depois é só:  

```bash
git init
git add .
git commit -m "Projeto Arquitetura Medallion no Azure"
git branch -M main
git remote add origin https://github.com/seuusuario/medallion-azure-kaggle.git
git push -u origin main

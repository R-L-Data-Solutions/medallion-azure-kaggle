-- Permissões Unity Catalog para schemas Bronze, Silver e Gold

-- Uso dos schemas
GRANT USAGE ON SCHEMA architecture_medallion.bronze TO `rldatasolutions@hotmail.com`;
GRANT USAGE ON SCHEMA architecture_medallion.silver TO `rldatasolutions@hotmail.com`;
GRANT USAGE ON SCHEMA architecture_medallion.gold TO `rldatasolutions@hotmail.com`;

-- Operações de leitura/escrita
GRANT SELECT, MODIFY ON SCHEMA architecture_medallion.bronze TO `rldatasolutions@hotmail.com`;
GRANT SELECT, MODIFY ON SCHEMA architecture_medallion.silver TO `rldatasolutions@hotmail.com`;
GRANT SELECT, MODIFY ON SCHEMA architecture_medallion.gold TO `rldatasolutions@hotmail.com`;

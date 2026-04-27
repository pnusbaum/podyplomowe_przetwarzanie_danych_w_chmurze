-- cw5 Stwórz nową tabele Glue w Twoje bazie danych Processed, bucket Processed o
-- następującej strukturze (zwróć uwagę na dodatkowy parametr na końcu -
-- 'useGlueParquetWriter'='true'):
CREATE EXTERNAL TABLE `datalake_processed_147433834225_pn_1203144`.processed_stockdata(
transaction_date timestamp,
price double,
amount double,
dollar_amount double,
type string,
trans_id bigint)
PARTITIONED BY (
symbol string,
year integer,
month integer,
day integer,
hour integer
)
ROW FORMAT SERDE
'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
's3://datalake-processed-147433834225-pn-1203144/stockdata/'
TBLPROPERTIES (
'useGlueParquetWriter'='true');
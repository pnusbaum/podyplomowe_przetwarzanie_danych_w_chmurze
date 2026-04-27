--Wykorzystaj dane zmaterializowane w poprzednim ćwiczeniu - tabela stockdata z
--bazy processed
--2. Utwórz tabelę z agreagacjami jak poniżej
CREATE EXTERNAL TABLE `datalake_processed_147433834225_pn_1203144`.agg_stockdata(
total_volume double,
total_dollars double,
total_cnt_of_transactions int,
type string
)
PARTITIONED BY (
symbol string,
year int,
month int,
day int)
ROW FORMAT SERDE
'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
's3://datalake-processed-147433834225-pn-1203144/agg_stockdata'

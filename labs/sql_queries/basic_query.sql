select * from "datalake_raw_147433834225_pn_1203144"."crawler_stockdata" 
WHERE type IN ('buy', 'sell')
limit 10;
#AWS Glue job exercise 5 proces curation
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1774093633335 = glueContext.create_dynamic_frame.from_catalog(database="datalake_raw_147433834225_pn_1203144", table_name="crawler_stockdata", transformation_ctx="AWSGlueDataCatalog_node1774093633335")

# Script generated for node SQL Query
SqlQuery0 = '''
select 
year(cast(transaction_ts as timestamp)) as year,
month(cast(transaction_ts as timestamp)) as month,
day(cast(transaction_ts as timestamp)) as day,
hour(cast(transaction_ts as timestamp)) as hour,
symbol, price, amount, dollar_amount, type, trans_id
from myDataSource
'''
SQLQuery_node1774093751512 = sparkSqlQuery(glueContext, query = SqlQuery0, mapping = {"myDataSource":AWSGlueDataCatalog_node1774093633335}, transformation_ctx = "SQLQuery_node1774093751512")

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1774094234500 = glueContext.write_dynamic_frame.from_catalog(frame=SQLQuery_node1774093751512, database="datalake_processed_147433834225_pn_1203144", table_name="processed_stockdata", additional_options={"enableUpdateCatalog": True, "updateBehavior": "UPDATE_IN_DATABASE", "partitionKeys": ["symbol", "year", "month", "day", "hour"]}, transformation_ctx="AWSGlueDataCatalog_node1774094234500")

job.commit()
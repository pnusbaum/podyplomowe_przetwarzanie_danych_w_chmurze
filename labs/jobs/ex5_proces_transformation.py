#AWS Glue job exercise 5 proces transformation
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame
import boto3

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
AWSGlueDataCatalog_node1777060579361 = glueContext.create_dynamic_frame.from_catalog(database="datalake_processed_147433834225_pn_1203144", table_name="processed_stockdata", transformation_ctx="AWSGlueDataCatalog_node1777060579361")

# Script generated for node SQL Query
SqlQuery1545 = '''
SELECT
    SUM(amount) AS total_volume,
    SUM(dollar_amount) AS total_dollars,
    CAST(COUNT(*) AS int) AS total_cnt_of_transactions,
    type,
    symbol,
    year,
    month,
    day
FROM myDataSource
GROUP BY
    symbol,
    year,
    month,
    day,
    type
ORDER BY
    symbol,
    year,
    month,
    day,
    type
'''
SQLQuery_node1777060593109 = sparkSqlQuery(glueContext, query = SqlQuery1545, mapping = {"myDataSource":AWSGlueDataCatalog_node1777060579361}, transformation_ctx = "SQLQuery_node1777060593109")

# wyczyszczenie poprzednich wyników
s3 = boto3.resource("s3")
bucket = s3.Bucket("datalake-processed-147433834225-pn-1203144")
bucket.objects.filter(Prefix="agg_stockdata/").delete()

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1777061337012 = glueContext.write_dynamic_frame.from_catalog(frame=SQLQuery_node1777060593109, database="datalake_processed_147433834225_pn_1203144", table_name="agg_stockdata", additional_options={"enableUpdateCatalog": True, "updateBehavior": "UPDATE_IN_DATABASE", "partitionKeys": ["symbol", "year", "month", "day"]}, transformation_ctx="AWSGlueDataCatalog_node1777061337012")

job.commit()
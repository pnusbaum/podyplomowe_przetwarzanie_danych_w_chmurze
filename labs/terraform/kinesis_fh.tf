resource "aws_kinesis_firehose_delivery_stream" "stock_delivery_stream" {
    name = "firehose-${var.account_number}-${var.student_initials}-${var.student_index_no}"
    destination = "extended_s3"
    
    kinesis_source_configuration {
        kinesis_stream_arn = aws_kinesis_stream.cryptostock_stream.arn
        role_arn = var.lab_role_arn
    }
    extended_s3_configuration {
        role_arn = var.lab_role_arn
        bucket_arn = aws_s3_bucket.raw_bucket.arn
        buffering_size = 1
        buffering_interval = 60
        prefix = "raw-zone/stockdata/year=!{timestamp:yyyy}/month=!{timestamp:MM}/day=!{timestamp:dd}/hour=!{timestamp:HH}/"
        error_output_prefix = "${"raw-zone/stockdata_errors/!{firehose:error-output-type}/year=!{timestamp:yyyy}"}${"/month=!{timestamp:MM}/day=!{timestamp:dd}/hour=!{timestamp:HH}"}/"
    }
}
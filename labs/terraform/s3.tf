resource "aws_s3_bucket" "raw_bucket" {
    bucket = "datalake-raw-${var.account_number}-${var.student_initials}-${var.student_index_no}"
    force_destroy = true
    tags = {
        Purpose = "UAM Cloud Data Processing"
        Environment = "DEV"
    }
}

resource "aws_s3_bucket" "processed_bucket" {
    bucket = "datalake-processed-${var.account_number}-${var.student_initials}-${var.student_index_no}"
    force_destroy = true
    tags = {
        Purpose = "UAM Cloud Data Processing"
        Environment = "DEV"
    }
}
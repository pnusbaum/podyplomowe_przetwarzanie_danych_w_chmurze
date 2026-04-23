resource "aws_ssm_parameter" "example" {
  name  = "bucket_name"
  type  = "String"
  value = "datalake-processed-${var.account_number}-${var.student_initials}-${var.student_index_no}"
}
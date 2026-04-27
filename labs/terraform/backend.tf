terraform {
  backend "s3" {
    bucket  = "bucket-state-147433834225-pn-1203144"
    key     = "terraform/terraform.tfstate"
    region  = "us-east-1"
    encrypt = true
  }
}
import boto3

# utworzenie klienta SSM
ssm = boto3.client("ssm")

# 1. podejrzenie istniejących parametrów
response = ssm.describe_parameters()
print("Istniejące parametry:")
for param in response.get("Parameters", []):
    print(param["Name"])

# 2. utworzenie nowego parametru foo = bar
put_response = ssm.put_parameter(
    Name="foo",
    Value="bar",
    Type="String",
    Overwrite=True
)

print("Parametr został utworzony lub nadpisany.")
print(put_response)

#3. odczytaj utworzona zmienna z terraforma

response = ssm.get_parameter(Name="bucket_name")
bucket = response["Parameter"]["Value"]
print("bucket_name:"+bucket)


#4. a teraz odczytaj nieistniejaca zmienna - ciekawe co sie wydarzy
response = ssm.get_parameter(Name="not_existing")
not_existing  = response["Parameter"]["Value"]
print("not_existing:"+not_existing)


# Przetwarzanie danych w chmurze publicznej 
## Wstęp do Data lakes
### Struktura projektu ###

* jupyter - notebooki z ćwiczeniami
* labs - skrypty do laboratorium - testowe dane, generator i podstawowe pliki terraform (starter)
* pdf - prezentacja i materiały do ćwiczeń 
* testing-stack - docker compose z definicjami Kafka, Kafka-Connect

### Wymagania wstępne ###
Instalacja środowiska zgodnie z instrukcją w : 

`./pdf/LABS Setup - Przetwarzanie Danych w chmurze publicznej.pdf`


## 🧾 Notatki / Szczegóły implementacyjne (PN)

- Dodałem backend S3 dla Terraform state `./labs/terraform/backend.tf` ( state jest poza kontrolą GITa)
- Cw4 Pkt6 
    * Stworzylem parametr z użyciem kodu pythona 
    `./labs/parameters/parameter_store.py`
    * Stworzylem parametr z użyciem kodu pythona 
    `./labs/parameters/parameter_store.py`
    * Cw4 Pkt6 Stworzylem parametr 'bucket_name' w 
    `terraform/parameter.tf`
    * Zmienilem kod lambdy by wczytywal bucket_name docelowy z parametru
- Cw5 
    * skrypty AWS Glue Jobs zapisalem 
        - `./labs/jobs/ex5_proces_curation.py`
        - `./labs/jobs/ex5_proces_transformation.py`
- Naprawiłem problem z idempotencją Glue joba (czyszczenie S3 z użyciem boto3)

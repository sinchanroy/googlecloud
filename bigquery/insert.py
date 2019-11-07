#! /usr/bin/env python 

from google.cloud import bigquery
from google.oauth2 import service_account
key_path = "/Users/si.roy/Documents/go-de-internal-siroy-e9cef2b81292.json"

credentials = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

bigquery_client = bigquery.Client(
    credentials=credentials,
    project=credentials.project_id,
)



#CREATE TABLE LOGIC

try:
 dataset_ref = bigquery_client.dataset('mydataset')
 table_ref = dataset_ref.table('mytable5')
 bigquery_client.get_table(table_ref)
except NotFound:
 #schema = [bigquery.SchemaField('name', 'STRING', mode='REQUIRED'), bigquery.SchemaField('age', 'INTEGER', mode='REQUIRED')]
 #table = bigquery.Table(table_ref, schema=schema)
 #table = bigquery_client.create_table(table)
 #print('table {} created.'.format(table.table_id))

#Insert Logic

 rows_to_insert = [(u'Phred Phlyntstone', 32),(u'Wylma Phlyntstone', 29)]
 errors = bigquery_client.insert_rows(table_ref, rows_to_insert)
 assert errors == []


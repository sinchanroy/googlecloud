#! /usr/bin/env python 

from google.cloud import bigquery
client = bigquery.Client()

filename = '/Users/si.roy/PycharmProjects/googlecloud/bigquery/biostats.csv'

dataset_id = 'mydataset'

table_id = 'load2'

dataset_ref = client.dataset(dataset_id)
table_ref = dataset_ref.table(table_id)

job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.CSV
job_config.skip_leading = 1
job_config.autodetect = True

with open(filename, "rb") as source_file:
	job = client.load_table_from_file(source_file, table_ref, job_config=job_config)

job.result()

print("Loaded")


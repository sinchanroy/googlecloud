#! /usr/bin/env python 


from google.cloud import bigquery
client = bigquery.Client()
dataset_id = 'mydataset'

dataset_ref = client.dataset(dataset_id)
job_config = bigquery.LoadJobConfig()

job_config.source_format = bigquery.SourceFormat.AVRO
uri = "gs://siroy-dataset/Avro/10k.variants.avro"

load_job = client.load_table_from_uri(uri, dataset_ref.table("amyavrotable2"), job_config=job_config) 
print("Starting job {}".format(load_job.job_id))

load_job.result() 
print("Job finished.")

destination_table = client.get_table(dataset_ref.table("amyavrotable2"))
print("Loaded {} rows.".format(destination_table.num_rows))


#! /usr/bin/env python 

from google.cloud import bigquery
client = bigquery.Client()
job_id = 'bq-job-123x456-123y123z123c'  # replace with your job ID
location = 'us'                         # replace with your location

job = client.cancel_job(job_id, location=location)

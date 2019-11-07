#! /usr/bin/env python 

# TODO(developer): Uncomment the lines below and replace with your values.

from google.cloud import bigquery
client = bigquery.Client()
job_id = 'job_dVDGeCWf6h9tjFJyDOG7h63mENpU'  # replace with your job ID
location = 'us'                         # replace with your location

job = client.get_job(job_id, location=location)  # API request

# Print selected job properties
print("Details for job {} running in {}:".format(job_id, location))
print(
    "\tType: {}\n\tState: {}\n\tCreated: {}".format(
        job.job_type, job.state, job.created
    )
)


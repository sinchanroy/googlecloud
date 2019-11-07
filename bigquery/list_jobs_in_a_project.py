#! /usr/bin/env python

from google.cloud import bigquery
project = 'go-de-internal-siroy'  # replace with your project ID
client = bigquery.Client(project=project)
import datetime

# List the 10 most recent jobs in reverse chronological order.
# Omit the max_results parameter to list jobs from the past 6 months.
print("Last 10 jobs:")
for job in client.list_jobs(max_results=10):  # API request(s)
    print(job.job_id)

# The following are examples of additional optional parameters:

# Use min_creation_time and/or max_creation_time to specify a time window.
print("Jobs from the last ten minutes:")
ten_mins_ago = datetime.datetime.utcnow() - datetime.timedelta(minutes=10)
for job in client.list_jobs(min_creation_time=ten_mins_ago):
    print(job.job_id)

# Use all_users to include jobs run by all users in the project.
print("Last 10 jobs run by all users:")
for job in client.list_jobs(max_results=10, all_users=True):
    print("{} run by user: {}".format(job.job_id, job.user_email))

# Use state_filter to filter by job state.
print("Jobs currently running:")
for job in client.list_jobs(state_filter="RUNNING"):
    print(job.job_id)


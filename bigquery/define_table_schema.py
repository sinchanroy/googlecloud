#! /usr/bin/env python 

import sys
from google.cloud import bigquery
client = bigquery.Client()

tablename=sys.argv[1]
table_id = f"go-de-internal-siroy.mydataset.{tablename}"

print ("Modified Table is %s", table_id)
schema = [
	bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
	bigquery.SchemaField("Age", "INTEGER", mode="REQUIRED" )
	]

table = bigquery.Table(table_id, schema = schema)

table = client.create_table(table)

print("Created Table")

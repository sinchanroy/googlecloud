#! /usr/bin/env python


import csv
import argparse
import re
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


class CSVtoDict:

	def parse_method(self, record):
	

	# 'Name':'Sinchan', 'Class':12, 'Sub':'Maths'

		values = re.split(",",re.sub('\r\n', '', re.sub(u'"', '', record)))
		row = dict(zip(('state', 'gender', 'year', 'name', 'number', 'created_date'),values))
		return row



def run(argv=None):
	
	parser = argparse.ArgumentParser()
	
	parser.add_argument('--input', dest='input', required=False, help="Input File")
	parser.add_argument('--output', dest='output', required=True, help="Output File")
	
	pipeline_args = parser.parse_known_args(argv)

	csv2dict = CSVtoDict()

	p = beam.Pipeline(options = PipelineOptions(pipeline_args))

	(p
	 | 'Read from a File' >> beam.io.ReadFromText(pipeline_args.input, skip_header_lines=1)
	 | 'String To BigQuery Row' >> beam.io.Write(
				beam.io.BigQuerySink(
					pipeline_args.output,
					schema = 'state:STRING,gender:STRING,year:STRING,name:STRING,number:STRING,created_date:STRING',
	 				create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
					write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE
				)

	 )
	)

	p.run().wait_until_finish()


if __name__ == '__main__':
	run()



	
	

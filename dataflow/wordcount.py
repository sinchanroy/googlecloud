#! /usr/bin/env python

import apache_beam as beam
import argparse
import io
import logging
import datetime

def run(argv = None, save_main_session = True):
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="Input file to process", dest="input")
    parser.add_argument("--output", help="Output file to write output", required=True)

    known_args, pipeline_args = parser.parse_known_args(argv)

    pipeline_options = PipelineOptions(pipeline_args)

    p = beam.Pipeline(options = pipeline_options)

    # READ TEXT File into PCollection

    lines = p | 'read' >> ReadFromText(known_args.input)

    # Count total number of words


#! /usr/bin/env python


import csv
import argparse
import re
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


if __name__ == '__main__':
    run()


def run(argv=None):

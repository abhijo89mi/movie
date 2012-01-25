#!/bin/sh

#PYTHON_PATH = /usr/local/bin/python2.7
export PYTHONPATH=/usr/local/django/sites/movie/

cd /usr/local/django/sites/movie/
output_filename=output/output-`date +%Y%m%d-%H.%M.%S`.txt
python2.7 muvidb.py > $output_filename

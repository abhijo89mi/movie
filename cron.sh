#!/bin/sh

cd /usr/local/django/sites/movie/
output_filename=output/output-`date +%Y%m%d-%H.%M.%S`.txt
python2.7 muvidb.py > $output_filename

#!/usr/bin/env python
from extractor_base import *
import os, sys, getopt, cStringIO

def main():
	catogory='B' 
	page=0
	limit=0
	def show_usage():
		print "eg : python extractor.py  -p 1 -c B -l 50"
		
	try:
		opts, args = getopt.getopt(sys.argv[1:], "c:l:p:h", ["category=","limit=", "page=",])
	except getopt.GetoptError, err:
		print str(err)
		show_usage()
		sys.exit(2)
	for o, a in opts:
		if o in ('-c', '--carogery'):
			catogory=a
		elif o in ('-l','--limit'):
			limit=a
		elif o in ('-p','--page'):
			page=a
		else :
			show_usage()
	e=Extractor_utils()
	e.get_country_code_and_load_json(catogory , page, limit)
	return 0

if __name__ == '__main__':
	main()


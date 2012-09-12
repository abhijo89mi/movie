#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       untitled.py
#       
#       Copyright 2012 MIS14 <mis14@mis14-A780L3L>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
#       
#!/usr/bin/env python
PYTHON_BIN = "/usr/local/bin/python2.7"
import os, sys, getopt, cStringIO
from imdb import IMDb
sys.path[0:0] = [
		os.path.dirname(__file__) + '/eggs/ipython-0.10.2-py2.7.egg',
		os.path.dirname(__file__) + '/eggs/South-0.7.1-py2.7.egg',
		os.path.dirname(__file__) + '/eggs/django_markitup-0.5.2-py2.7.egg',
		os.path.dirname(__file__) + '/eggs/django_robots-0.7.0-py2.7.egg',
		os.path.dirname(__file__) + '/eggs/sorl_thumbnail-11.01-py2.7.egg',
		os.path.dirname(__file__) + '/eggs/BeautifulSoup-3.2.0-py2.7.egg',
		os.path.dirname(__file__) + '/eggs/Markdown-2.0.3-py2.7.egg',
		os.path.dirname(__file__) + '/eggs/djangorecipe-0.99-py2.7.egg',
		os.path.dirname(__file__) + '/eggs/Django-1.2.1-py2.7.egg',
		os.path.dirname(__file__) + '/eggs/zc.recipe.egg-1.3.2-py2.7.egg',
		os.path.dirname(__file__) + '/eggs/zc.buildout-1.5.2-py2.7.egg',
		os.path.dirname(__file__) + '/eggs/setuptools-0.6c12dev_r88846-py2.7.egg',
		os.path.dirname(__file__) + '/parts/django',
		os.path.dirname(__file__),
		]

os.environ['DJANGO_SETTINGS_MODULE'] = 'movie.development'
from django.conf import settings
from movie.main.models import *
from datetime import datetime


from sendsmspy import main_fun
def main():
	total_movie = Movie.objects.count()
	person = Person.objects.count()
	company = Company.objects.count()
	genre = Genre.objects.count()
	countries = Countries.objects.count()
	languages = Languages.objects.count()
	
	msg = "Total Move :%s , Person :%s,Company :%s,Genre :%s ,Countries :%s ,Languages :%s, For more information visit www.muvidb.com"%(total_movie,person,company,genre,countries,languages)
	main_fun('9632928652',msg)
	return 0

if __name__ == '__main__':
	main()


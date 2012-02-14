import os, sys, getopt, cStringIO

sys.path[0:0] = [
		os.path.dirname(__file__)+'/eggs/ipython-0.10.2-py2.7.egg',
		os.path.dirname(__file__)+'/eggs/South-0.7.1-py2.7.egg',
		os.path.dirname(__file__)+'/eggs/django_markitup-0.5.2-py2.7.egg',
		os.path.dirname(__file__)+'/eggs/django_robots-0.7.0-py2.7.egg',
		os.path.dirname(__file__)+'/eggs/sorl_thumbnail-11.01-py2.7.egg',
		os.path.dirname(__file__)+'/eggs/BeautifulSoup-3.2.0-py2.7.egg',
		os.path.dirname(__file__)+'/eggs/Markdown-2.0.3-py2.7.egg',
		os.path.dirname(__file__)+'/eggs/djangorecipe-0.99-py2.7.egg',
		os.path.dirname(__file__)+'/eggs/Django-1.2.1-py2.7.egg',
		os.path.dirname(__file__)+'/eggs/zc.recipe.egg-1.3.2-py2.7.egg',
		os.path.dirname(__file__)+'/eggs/zc.buildout-1.5.2-py2.7.egg',
		os.path.dirname(__file__)+'/eggs/setuptools-0.6c12dev_r88846-py2.7.egg',
		os.path.dirname(__file__)+'/parts/django',
		os.path.dirname(__file__),
		]


os.environ['DJANGO_SETTINGS_MODULE'] = 'movie.settings'

from BeautifulSoup import BeautifulSoup
import re
import urllib2, urllib
from django.core.files import File  # you need this somewhere
from django.template.defaultfilters import slugify
from urlparse import urlparse
from django.conf import settings
from movie.main.models import *
from datetime import datetime

BROWSER_HEADER = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
hit_url='http:/www.imdb.com/search/title?genres=action&sort=moviemeter,asc&start=1&title_type=feature'


def parseurl(url):
	hit_no=0

	request = urllib2.Request(url)
	request.add_header('User-agent', BROWSER_HEADER)
	request.add_header('Host', 'www.imdb.com')
	request.add_header('Accept', 'html')
	request.add_header('Accept-Language', 'en-us,en')
	#request.add_header('Accept-Encoding', 'gzip, deflate')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8')
	request.add_header('Connection', 'keep-alive')
	request.add_header('Referer', 'http:/www.imdb.com/search/title?genres=action&sort=moviemeter,asc&start=51&title_type=feature')
	handle = urllib2.urlopen(request)
	html = handle.read()
	soup = BeautifulSoup(html)
	return soup
def HTMLFM(data):
	return re.sub("(&#*\w+;)","",data)
  
def main():
	count=0
	if (len(sys.argv) > 1):
		genres=sys.argv[1]
		print "===",genres
		totalhit=Genre.objects.filter(name=genres).get().total_movie
		genres_id=Genre.objects.filter(name=genres).get().id
		try :
			count=movieurl.objects.filter(filter_based_on__name=genres_id).count()
			url_start_id=movieurl.objects.filter(filter_based_on__name=genres_id).order_by('-id')[:1].get().id
			end=movieurl.objects.filter(filter_based_on__name=genres_id).order_by('id')[:1].get().id
			print "====== Summory ======"
			print "Start :",end
			print "End   :",url_start_id
			print "Total count :",count
			print "Geres   :",genres
			print "Total Movie:",totalhit
			print "====================="


		except Exception as e:
			print e
			url_start_id=0
			pass
		url_end_id=0
	else:
		exit(0)
		
	genre=Genre.objects.get(name=genres)
	for page_no in xrange(count,totalhit,50):
		url='http://www.imdb.com/search/title?genres='+str(genre)+'&sort=moviemeter,asc&start='+str(page_no)+'&title_type=feature'
		print url
		try :
			html=parseurl(url)
			result_table=html.find('table',{'class':'results'})
			title_td=result_table.findAll('td',{'class':'title'})
			for a in title_td:
			  x=a.find('a',{'class':None})
			  movie_name=HTMLFM(x.find(text=True).strip())
			  m_url="http://www.imdb.com"+ x['href']
			  imdbid_list=m_url.split('/')
			  imdbid=imdbid_list[-2:-1][0]
			  run_date=datetime.now()
			  try :
				movie, created = movieurl.objects.get_or_create(imdbid=imdbid,movie_name=movie_name,url=m_url,filter_based_on=genre,run_date=run_date,)
				#print 'Movie url'+m_url+' Saved '+'Start from  :'+str(page_no)
			  except Exception as e:
				  print e
				  pass
		except Exception as e:
		  error, created = Errorlog.objects.get_or_create(function_name='Imdburlparser',message=e,date=datetime.now())
		  print 'Error :'+str(e)
		  pass
		#url_end_id =movieurl.objects.order_by('-id')[:1].get().id
		#log, created = Urllog.objects.get_or_create(start_url_id=url_start_id,end_url_id=url_end_id,end_date=datetime.now())

	return 0


if __name__ == '__main__':
	main()

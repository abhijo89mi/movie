
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
os.environ['DJANGO_SETTINGS_MODULE'] = 'movie.development'

from BeautifulSoup import BeautifulSoup
import re
import urllib2, urllib
from movie.main.models import *
from django.core.files import File  # you need this somewhere
from django.template.defaultfilters import slugify
from urlparse import urlparse
from django.conf import settings
import os

Total=50000
last_case_fname='person.txt'

def HTMLFM(data):
        return re.sub("(&#*\w+;)","",data)        
def main():
  with open(last_case_fname, 'r') as f:
    start_num = int(f.read())
  persons=Person.objects.filter(id__lt=start_num+Total,id__gt=start_num)
  for person in persons :
    url='http://www.imdb.com/name/nm'+person.personID+'/bio'
    page_url = urllib2.Request(url)
    response = urllib2.urlopen(page_url)
    html = response.read()
    soup = BeautifulSoup(html)
    
    base=soup.findAll("div" , {"id":"tn15" , "class" : "bio"}) # getting <td class="title"> from the html page
    if base :
            print "got url and finding elements"
            for temp in base :
                    find_image =temp.findAll("div",{"id":"tn15lhs"})
                    for temp in find_image :
                            imgtag=temp.find('img')
                            if imgtag :
                                  try:
                                      imageurl= imgtag['src'] # got image 
                                      name=imageurl.split('/')[5]
                                      os.system("wget "+imageurl+" --directory-prefix=./movie/media/actors/")
                                      print 'file saved locally'
                                      tlbphoto,c=Photo.objects.get_or_create(url=name)
                                      person.photo.add(tlbphoto)
                                      person.save()
                                  except:
                                    print "No Photo found !!"
                                    pass
            
            
            for datatag in base :
                    data=datatag.findAll("div",{"id":"tn15content"})
                    for d in data :
                            a= d.find('a')
                            if a :
                                    dob=a.find(text=True)
                                    try :
                                            if re.findall('\d+', dob) : 
                                                    date_of_birth= dob 
                                    except:
                                            print "***ERROR***"
                                            date_of_birth= ''
                                            pass
                                            
                            bio= d.findAll('p')
                            w=''
                            for b in bio:
                                    
                                    w=w+b.find(text=True)
                            biodata= HTMLFM(w)
                            
    flag =Person.objects.filter(id=person.id).update(biodata=biodata)
    if flag :
      with open(last_case_fname, 'w') as f:
				#signals next resume not to continue..
				f.write("%d" % (person.id+1))
      print person.name+" got updated !"

  return 0

if __name__ == '__main__':
        main()


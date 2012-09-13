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
import re
import urllib2, urllib
from BeautifulSoup import BeautifulSoup

from ftplib import FTP
import sys
from sendsmspy import main_fun

Total=50000
last_case_fname='person.txt'
SMS_NUMBER = "7204785003"
def HTMLFM(data):
        return re.sub("(&#*\w+;)","",data)
    
def  main():
    with open(last_case_fname, 'r') as f:
            start_num = int(f.read())
    try:
        ftp = FTP("www.muvidb.com")
        ftp.login('python@muvidb.com', 'python')
    except Exception as e:
            message = "Unable to login to the remote server"
            main_fun(SMS_NUMBER,message) 
            sys.exit()       
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
                                        print 'file saved locally and connecting to remote server...'
                                        f = open("./movie/media/actors/"+name, "rb")
                                        ftp.storbinary("STOR "+name,f)
                                        print "File saved in remote server, deleting the local file ..."
                                        os.system("rm ./movie/media/actors/"+name)
                                        tlbphoto,c=Photo.objects.get_or_create(url=name)
                                        person.photo.add(tlbphoto)
                                        person.save()
                                    except IndexError:
                                       pass
              
              date_of_birth= ''
              for datatag in base :
                      data=datatag.findAll("div",{"id":"tn15content"})
                      for d in data :
                              a= d.find('a')
                              if a :
                                      dob=a.find(text=True)
                                      try :
                                              if re.findall('\d+', dob) : 
                                                      #db = datetime.strptime (dob,'%Y-%m-%d')
                                                      #print "========================", db
                                                      date_of_birth= dob 
                                      except:
                                              print "***ERROR***"
                                              
                                              pass
                                              
                              bio= d.findAll('p')
                              w=''
                              for b in bio:
                                      
                                      w=w+b.find(text=True)
                              biodata= HTMLFM(w)
                              
      flag = Person.objects.filter(id=person.id).update(biodata=biodata,date_of_birth=date_of_birth)
      if flag :
        with open(last_case_fname, 'w') as f:
                  #signals next resume not to continue..
                  f.write("%d" % (person.id+1))
        print person.name+" got updated !"

    return 0

if __name__ == '__main__':
    main()

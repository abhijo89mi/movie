#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sendsms.py
#  
#  Copyright 2012 Abhilash <abhi.jo89@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import urllib
import urllib2
import cookielib
import simplejson as json
from  BeautifulSoup import BeautifulSoup
import random
BROWSER_HEADER = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"

def main_fun(mobnumber,msg):
		cj = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		opener.addheaders = [('User-agent', BROWSER_HEADER)]
		handle = opener.open("http://ontextme.com/share/?version=1.0.1&partner=firefox")
		html = handle.read()
		url = "http://ontextme.com/exchange/ajax/auth/login/"
		handle = opener.open(url,'mobile=9035026637&password=mundiathadukka&rememberMe=1')
		html = handle.read()
		toMobile = mobnumber #raw_input("Enter Mobile Number : ")

		
		handle = opener.open("http://ontextme.com/share/?version=1.0.1&partner=firefox")
		html = handle.read()
		soup = BeautifulSoup(html)
		exchangeId = soup.find('input',{'name':'exchangeId'})['value']
		exchangeToken = soup.find('input',{'name':'exchangeToken'})['value']
		
		message = msg

		
		post_values = {
			'exchangeId':exchangeId,
			'exchangeToken':exchangeToken,
			'toMobile':toMobile,
			'message':message
		}
		#sleep(60000)
		data = urllib.urlencode(post_values)
		handle = opener.open("http://ontextme.com/exchange/ajax/validate/",data)
		html = handle.read()
		print html
			
		return 0

if __name__ == '__main__':
	main_fun('7204785003')


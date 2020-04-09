#!/usr/bin/env python
# coding: utf-8

import requests
import wget
from datetime import datetime, timedelta
import pathlib


date = '2020-01-01'
pathh = pathlib.Path(__file__).parent

try:
	f = open(f'{pathh}\log.txt','r')
	file = eval(f.read())
	date = file['Date']
except:
	f = open(f'{pathh}\log.txt','w+')
	f.write('{"Date":,"Days":}')
	f.close()
	
url = 'https://api.nasa.gov/planetary/apod?api_key=OR2B99R4cf5diubS5HA4AUMqK5Gf9eg0Qj5eYejp'

try:
        for x in range(file['Days']):
            tag = requests.get(url,params={'hd':'True','date':date})
            
            contents = eval(tag.text)
            try:
                img = contents['url']
                wget.download(img, out=str(pathh))
                print('Success',date)
            except:
                print('Fail',date)
            
            date = (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
except:
        for x in range(10):
            tag = requests.get(url,params={'hd':'True','date':date})
            
            contents = eval(tag.text)
            try:
                img = contents['url']
                wget.download(img, out=str(pathh))
                print('Success',date)
            except:
                print('Fail',date)
            
            date = (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
        


f.close()

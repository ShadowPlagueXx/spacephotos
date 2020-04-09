#!/usr/bin/env python
# coding: utf-8

import requests
import wget
from datetime import datetime, timedelta
import pathlib

choice = input('Starting date? (YYYY-MM-DD): ')
choice2 = int(input('How many days? '))
choice3= input('Path? ')

url = 'https://api.nasa.gov/planetary/apod?api_key=OR2B99R4cf5diubS5HA4AUMqK5Gf9eg0Qj5eYejp'
date = str(choice)

for x in range(choice2):
    tag = requests.get(url,params={'hd':'True','date':date})
    
    contents = eval(tag.text)
    try:
        img = contents['url']
        wget.download(img, out=str(choice3))
        print('Success',date)
    except:
        print('Fail',date)
    
    date = (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')


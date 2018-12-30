# -*- coding: utf-8 -*-
"""
CloudEngine project
Django 1.10.1
Python 2.7.6

Author: Ramesh Kumar K

Demo: http://CloudEngine.pythonanywhere.com
Source: https://github.com/CloudEngine/CloudEngine

https://CloudEngine.com/
http://CloudEngine.com

Licensed under the Apache License, Version 2.0 (the "License").
You may not use this file except in compliance with the License.
A copy of the License is located at

http://www.apache.org/licenses/
"""

import requests
import json

url = 'http://localhost:8000/api/v1/datas/'

datas = {'api_key':'311b9c68f7e64bdfb77aab1e4d53aaf04378a463',
        'element_id_1':'a', 'value_1':10,
        'element_id_2':'b', 'value_2':20}

auth=('admin', 'Aa1234567890')

response = requests.post(url, data=datas, auth=auth)
print response

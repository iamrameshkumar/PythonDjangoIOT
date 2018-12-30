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
import time


headers = {'Content-type': 'application/json'}

# url = 'http://localhost:8000/api/v1/datas/'
url = 'http://CloudEngine.pythonanywhere.com/api/v1/datas/'


auth=('admin', 'Aa1234567890')

for i in range(100):
    data={
        'api_key':'befb1ce654864a0ebf6ca1d0e901c2374d308e99',
        'value_1':i*10,
        }

    data_json = json.dumps(data)
    response = requests.post(url, data=data_json, headers=headers, auth=auth)
    print(response)
    print(response.json())
    time.sleep(5)

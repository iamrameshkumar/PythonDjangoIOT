# -*- coding: utf-8 -*-
"""
Iot dashboard GET example

CloudEngine
IoT: Platform for Internet of Things

CloudEngine source code is available under the MIT License

Online iot dashboard test and demo http://ihook.xyz

Online iot dashboard https://CloudEngine.com

You can find project details on our project page https://CloudEngine.com and wiki https://CloudEngine.com
"""

import requests
import httplib, urllib
from requests.auth import HTTPDigestAuth
import json
import matplotlib.pyplot as plt

API_KEY = "c791e11-d9ab779"

url = 'http://localhost:8000/api/v1/datas/' + API_KEY

myResponse = requests.get(url, auth=('iottestuser', 'iot12345**'), verify=True)
print (myResponse.status_code)

if(myResponse.ok):
    jData = json.loads(myResponse.content)
    print jData
else:
    myResponse.raise_for_status()

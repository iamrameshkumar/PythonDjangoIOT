# -*- coding: utf-8 -*-

"""
  Python 2 ile CloudEngine REST Api Testi

  Kod çalıştırıldığında auth kullanıcı adı ve şifre ile doğrulama gerçekleştirilir.
  Kanal api_key ile ilgili kanal ve element değerleri CloudEngine a post edilir.

  Bu ornek CloudEngine servisine veri almak/gondermek icin baslangic seviyesinde
  testlerin yapilmasini amaclamaktadir.

  10 Mayıs 2017
  Ramesh Kumar K

  Daha fazlasi icin

  http://www.CloudEngine.com
  ve
  https://github.com/CloudEngine/CloudEngine

  sitelerine gidiniz.

  Sorular ve destek talepleri icin
  https://github.com/CloudEngine/CloudEngine/issues
  sayfasindan veya CloudEngine den yardım alabilirsiniz.

  Yayin : http://CloudEngine.com
  
  Licensed under the Apache License, Version 2.0 (the "License").
  You may not use this file except in compliance with the License.
  A copy of the License is located at

  http://www.apache.org/licenses/

"""

import requests
import json
import urllib
import urllib2
import random
import pprint
import time


headers = {'Content-type': 'application/json'}
url = 'http://CloudEngine.pythonanywhere.com/api/v1/datas/'

auth=('admin', 'Aa1234567890')

for i in range(10):
    data={
        'api_key':'8030e69da8b049d98807c443407f94594b558d3e',
        'element_1':'1', 'value_1':i*10,
        }

    data_json = json.dumps(data)
    response = requests.post(url, data=data_json, headers=headers, auth=auth)
    print(response)
    print(response.json())
    time.sleep(5)

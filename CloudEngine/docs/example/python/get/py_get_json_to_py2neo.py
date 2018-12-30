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

API_KEY = "0cd76eb-5f3b179"
url = 'http://localhost:8000/api/v1/datas/' + API_KEY

# response = requests.get(url, auth=('admin', 'Aa12345**'))
# data = response.json()
# print data


# from py2neo import Graph, Path
# graph = Graph()
#
# tx = graph.cypher.begin()
# for name in ["Alice", "Bob", "Carol"]:
#     tx.append("CREATE (person:Person {name:{name}}) RETURN person", name=name)
# alice, bob, carol = [result.one for result in tx.commit()]
#
# friends = Path(alice, "KNOWS", bob, "KNOWS", carol)
# graph.create(friends)


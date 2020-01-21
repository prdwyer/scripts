import sys
import requests
import json
import os 
import argparse
import configparser
from harpoon.commands.base import Command
from harpoon.lib.utils import json_serial, unbracket

#urlinfo = "https://pulsedive.com/api/info.php?iid=466961&pretty=1&sanitize=1&key="
urlinfo = "https://pulsedive.com/api/info.php"
urlsearch = "https://pulsedive.com/api/search.php"
urlanalyze = "https://pulsedive.com/api/search.php"


class PulseDiveError(Exception):
	pass

class PulseDiveNotFound(PulseDiveError):
	pass



class PulseDive(Command):
	'''
	pulsedive api wrapper
	urlinfo = "https://pulsedive.com/api/info.php"
	urlinfo = "https://pulsedive.com/api/info.php"
	'''
	name = "pulsedive"
	description = "search pulsedive for indicator"
	config = {'pulsedive': ['token']}

	def set_params(inputs):

		PARAMS = {"pretty":"true","indicator": "danislenefc.info"}


	def run(self, user, key):
		self.user = user
		self.key = key
		self.base_url = "https://pulsedive.com/api/info.php"


	def _query(self, query):
		return requests.get(self.base_url, query)

	def search(self, query):


		start = 0 
		end = False
		result = {}
		while not end:
			res = self._query('{"indicator": "'+query+'"}')
			if res.status_code != 200:
				raise PulseDiveError()
			else:
				root = ET.fromstring(res.text)
				if start == 0:
					result = root.find('result')
					results = {
						'total': int(result.attrib('numFound']),
						'results': [a.text for a in root.findall('.//result/doc/')]
					}
					start += len(results['results'])
					if start >= results['total']:
						return results

				else:
					docs = root.findall('.//result/doc/')
					for a in docs:
						results['results'].append(a.text)
					start += len(docs)
					if start >= results['total']:
						return results


		#here is my code					

		parser = argparse.ArgumentParser(description='pulsedive')
		parser.add_argument("-i","--ioc", dest="ioc", default=None, help="ioc search ")
		args = parser.parse_args()
		PARAMS = set_params(args.ioc)

		r = requests.get(url = urlinfo, params = PARAMS)

		data = r.json()
		#print(str(data))

		if data.get("error"):
			print("error indicator not found")
			exit
		else:

			#print(dir(data.items))
			print("indicator:  "+data.get("indicator"))
			print("rated risk:  "+data.get("risk"))
			#print(data.get("type"))
			print("=============================================================")
			print("ports:")
			for p in data.get("attributes").get("port"):
				print("         " + p)

			print("=============================================================")
			print("geo:  ")
			geodat= data.get("properties").get("geo")
			for d in geodat:
				print("         " + d + " : "+ str(geodat[d]) )

			print("ssl:  ")
			ssldat = data.get("properties").get("ssl")
			for d in ssldat:
				print("         " + d + " : " + ssldat[d])

			print("=============================================================")
			print("threat report: ")
			threatdat = data.get("threats")
			for d in threatdat:
				print(d.get("name"))

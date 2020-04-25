import requests
import json
import argparse



#parser = argparse.ArgumentParser(description='specify what your stuff is')


#parser.add_argument("-i","--infile", dest="infile", default=None, help="csv input file")
#parser.add_argument('infile', metavar='N', type=str, nargs='+', help='csv input file')



# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/check'

ipfile = open('fraud_ip_addresses.txt')


json_object=""

for x in ipfile:
	x=x.strip()
	print(x)
	querystring = {
		'ipAddress': x,
		'maxAgeInDays': '90'
	}
	headers = {
		'Accept': 'application/json',
		'Key': 'keeeeeeygohere'
	}

	response = requests.request(method='GET', url=url, headers=headers, params=querystring)

	# Formatted output
	decodedResponse = json.loads(response.text)
	json_object+=json.dumps(decodedResponse, sort_keys=True, indent=4)

with open("output.json", "w") as outfile: 
	outfile.write(json_object) 


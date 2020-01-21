import argparse
import csv
import os
import dns.resolver
import dns.query
import sys
import re




def strip_ip(string):
	pat = re.compile('(([2][5][0-5]\.)|([2][0-4][0-9]\.)|([0-1]?[0-9]?[0-9]\.))(([2][5][0-5])|([2][0-4][0-9])|([0-1]?[0-9]?[0-9]))')
	match = pat.search(string)
	if match:
		return match.group(0)

def is_ip(string):
	pat = re.compile('(([2][5][0-5]\.)|([2][0-4][0-9]\.)|([0-1]?[0-9]?[0-9]\.))(([2][5][0-5])|([2][0-4][0-9])|([0-1]?[0-9]?[0-9]))')
	match = pat.search(string)
	if match:
		return True
	else:
		return False

def strip_col(f, col):
	ofile = open('singlecol.txt', "w")
	writer = csv.writer(ofile, delimiter=',',quoting=csv.QUOTE_ALL)
	with open(f) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			answer=row[int(col)]
			if answer != None:
				ofile.write(answer+ "\n")

	

def remove_blanks(row):
	row = filter(None, row)
	return row


def is_email(string):
	if string.contains("@"):
		return True
	else:
		return False



def host2CNAME( hostname ):
	try:
		myResolver = dns.resolver.Resolver()
		#TXT, CNAME, SOA
		answers = myResolver.query(hostname,'CNAME')
		for rdata in answers:
			return rdata

	except dns.resolver.NXDOMAIN:
		print("No such domain %s" % hostname)
	except dns.resolver.Timeout:
		print("Timed out while resolving %s" % hostname)
	except dns.exception.DNSException:
		print ("Unhandled exception")



def host2ip( hostname ):
	try:
		myResolver = dns.resolver.Resolver()
		answers = myResolver.query(hostname)
		for rdata in answers:
			return rdata

	except dns.resolver.NXDOMAIN:
		print("No such domain %s" % hostname)
	except dns.resolver.Timeout:
		print("Timed out while resolving %s" % hostname)
	except dns.exception.DNSException:
		print ("Unhandled exception")

'''
	answers = myResolver.query(hostname)
	return answers

	for rdata in answers:
	    print rdata
	    '''

def ip2host( ip ):
	#ip = "88.99.169.165"
	req = '.'.join(reversed(ip.split("."))) + ".in-addr.arpa"
	try:
		myResolver = dns.resolver.Resolver()
		answer = myResolver.query(req, "PTR")
		for rdata in answer:
			return rdata

	except dns.resolver.NXDOMAIN:
		print("No such domain %s" % ip)
	except dns.resolver.Timeout:
		print("Timed out while resolving %s" % ip)
	except dns.exception.DNSException:
		print("Unhandled exception")



def file_process_h2ip(f,o):
	ofile = open(o, "w")
	writer = csv.writer(ofile, delimiter=',',quoting=csv.QUOTE_ALL)
	with open(f) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			answer=host2ip(row[0])
			if answer != None:
				row.append(answer)
				row=remove_blanks(row)
				writer.writerow(row)


def file_process_h2CNAME(f,o):
	ofile = open(o, "w")
	writer = csv.writer(ofile, delimiter=',',quoting=csv.QUOTE_ALL)
	with open(f) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			answer=host2ip(row[0])
			if answer != None:
				row.append(answer)
				row=remove_blanks(row)
				writer.writerow(row)


def file_process_ip2h(f,o):
	ofile = open(o, "w")
	writer = csv.writer(ofile, delimiter=',',quoting=csv.QUOTE_ALL)
	with open(f) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			answer=ip2host(row[0])
			if answer != None:
				print(answer)
				row.append(answer)
				row=remove_blanks(row)
				print(row)
				writer.writerow(row)



def file_clean(f):
	ofile = open('ttest.csv', "w")
	writer = csv.writer(ofile, delimiter=',',quoting=csv.QUOTE_ALL)
	with open(f) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
				row=remove_blanks(row)
				writer.writerow(row)





if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='specify what your stuff is')

	parser.add_argument("-o","--operation", dest="operation", default=None, help="operation to perform on an input file")
	#parser.add_argument('operation', metavar='N', type=str, nargs='+', help='operation to perform on input file')

	parser.add_argument("-i","--infile", dest="infile", default=None, help="csv input file")
	#parser.add_argument('infile', metavar='N', type=str, nargs='+', help='csv input file')

	parser.add_argument("-f","--outfile", dest="outfile", default=None, help="csv output file")
	#parser.add_argument('outfile', metavar='N', type=str, nargs='+', default='output.csv', help='csv output file')

	parser.add_argument("-c","--column", dest="column" , default=None, type=int, nargs='?', help='csv column')
	#parser.add_argument('column', metavar='N', type=int, nargs='?', help='csv column')

	args = parser.parse_args()

	print(args)
	print("".join(args.operation))
	print(str(args.infile))
	print(str(args.outfile))

	#SCRIPT STARTS HERE
	#print(cmd)
	#print(f)
	#cmd = sys.argv[1]
	#f = sys.argv[2]
	cmd = "".join(args.operation)
	f = "".join(args.infile)
	o = "".join(args.outfile)

	col = ""+str(args.column)



	myResolver = dns.resolver.Resolver()

	if cmd == "host2ip":
		print("host")
		file_process_h2ip(f,o)
	elif cmd == "host2CNAME":
		print("host")
		file_process_h2CNAME(f,o)
	elif cmd == "ip2host":
		print("test")
		file_process_ip2h(f,o)
	elif cmd == "clean":
		print("cleanup")
		file_clean(f)
	elif cmd == "stripcol":
		print("stripcol")
		strip_col(f,col)
	else:
		print ("host2ip or ip2host")



from netaddr import *
import re





def parseIP(line):

	if "-" in line:

		#print "range"
		line = "".join(line.split())
		range_list = line.split("-")
		#print range_list
		return IPRange(range_list[0], range_list[1])
	else:

		#print "Ssssssssssssssssssssssssssssssssssingle"
		line = "".join(line.split())
		#print "XXX"+line
		#return line
		return IPAddress(line)


#below turn to MAIN


f = open("scan.conf")
lines = f.readlines()
for x in lines[:]:
	x="".join(x.split())
big = filter(None, lines)
lines = [a for a in big if a != '\n']

master = list()

for x in lines[:]:
	if x=='':
		print "hit"
		pass
	if "#" in x:
		reference_frame=x 
		#print x
		current_set=IPSet()
		master.append(current_set)
	else: 
		#print reference_frame
		#print parseIP(x)
		current_set.add(parseIP(x))
		#IPSet()



#print master[0]-master[-1]

d1 = master[0]-master[-1]
d2 = master[1]-master[-1]

print d1
f1 = open('testout.txt','w+')
for ip in d1:
	f1.write(str(ip)+"\n")

f1.close()
#print d2 



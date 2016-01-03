#!/usr/bin/python


import re

path = './web.log'

#regex = '([(\w\_\-\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (\d*)'
regex = '([(\w\-\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (\d*)'
#regex = '([(\w\-\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (\d+)'
#regex = '([(\w\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (\d+)'
#regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) - "(.*?)" "(.*?)"'


logdata = []
#f = open(path)
fo = open("OUTLOG", "w")
with open(path) as f:
  logdata = f.readlines()
  f.close()
results = {}
for entry in logdata:
  match =  re.match(regex, entry)
  host = match.group(1)
  g2 = match.group(2)
  g3 = match.group(3)
  g4 = match.group(4)
  g5 = match.group(5)
  count = g5
  strcount = str(count)
  (shortdate,tz) = re.split(' ',g2)
  strshortdate = str(shortdate)

  if entry[0] not in results:
   results[entry[0]] = {'mhost': host} 
   results[entry[0]] = {'lastdate': strshortdate} 
   results[entry[0]] = {'mcount': 0} 
#   results[entry[0]] = {'lastdate':strshortdate} 

  results[entry[0]]['mhost'] = host
  results[entry[0]]['mcount'] += 1
  results[entry[0]]['lastdate'] = shortdate


for mhost in results:
#  print ip
#  print results[mhost]  
#   print results[mhost]
   ohost = results[mhost]['mhost']
   ocount = str(results[mhost]['mcount'])
   odate = results[mhost]['lastdate']
   print ohost + ' - ' + ocount + ' - ' + odate
#   fo.write( ohost + ' - ' + ocount + ' - ' + odate)

  
#  results['host'] = host
#  results['host'].count = strcount
#  results['host'].lastaccess = strshortdate

#  results['count'] = strcount
#  results['lastaccess'] = strshortdate

#  print host + ' - ' + g5 + ' - ' + shortdate
#  if entry['host'] not in results:
#    results[entry['host']]['count'] += 1
#    results[entry['host']]['lastaccess'] = shortdate

#for item in results:
#  print item + ' - ' + results[item['host']['count']] + ' - ' + results[item['host']['lastaccess']]

#logdb = {'host':'10.10.10.10', 'hcount':1, 'lastaccess':'Sat Jan  2 00:42:59 PST 2016'}

  
#print logdb['host']
#print logdb['hcount']
#print logdb['lastaccess']



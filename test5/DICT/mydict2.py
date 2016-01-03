
D = {'Composer': {'firstname':'Johann', 'lastname':'Brahms'}, 'period': 'Romantic', 'Symphony': 1}

D['Symphony'] += 1
print D

ED =[]
ED = {'host':'10.10.10.10',  'count': 1, 'lastaccess': 'jan 1'}
print ED

if ED['host'] == '10.10.10.10':
  print 'FOUND node' + ED['host'] 
  host = ED['host']
  ED['host']['count'] += 1 
  ED['host']['lastaccess'] = 'jan 2' 
  
print ED

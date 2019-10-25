import pprint
cats=[{'name':'zophie', 'desc':'chuby'},{'name':'pooka', 'desc':'fluffy'}]
pprint.pformat(cats)
fileObject=open('mydogs.py','w')
fileObject.write('cats='+pprint.pformat(cats)+'\n' )
pprint.pprint(cats)
fileObject.close()

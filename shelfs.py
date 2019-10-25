#snimanje promenljivih pomocu modula shelve
import shelve
shelfFile=shelve.open('mydata')
cats=['zophie', 'pooka', 'simon']
shelfFile['cats']=cats
#kao local storage u js shelf file je sacuvao pod keyem cats promenljivu cats
shelfFile.close()

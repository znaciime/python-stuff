import os
for folder, sub, file in os.walk('C:\\Users\\aca87\\Desktop\\World of Warcraft 1.12'):
   print('folder is:'+folder)
   for sub in sub:
       print('subfolder is:'+sub)
       for file in file:
           print('files are:'+file)

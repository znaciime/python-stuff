import os
print(os.path.abspath('.'))
print(os.path.abspath('.\isPhonenumber.py'))
print(os.path.relpath('c:'))
print(os.getcwd())
myFiles=['account.txt', 'detail.csv', 'text.doc']
for files in myFiles:
    print(os.path.join('C:\\Users\\CONGA\\', files))
print(os.path.getsize(r'C:\Users\aca87\Documents\python'))
print(os.path.exists('D:\\'))

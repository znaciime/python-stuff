eggs=[1, 3, 45, 44, 2, 23]
eggs.sort()
print(eggs)
zbz=['pera', 'zika', 'joca', 'mica']
zbz.sort()
print(zbz)
new=eggs+zbz
print(new)
print(zbz.index('pera'))
print(new.index('pera'))
print(len(zbz))
zbz.insert(4, 'deki')
print(zbz)
print(zbz)
for i in range(0, len(zbz)):
    print(zbz[i])
zbz.sort(reverse=True)
print(zbz)
for i in range(0, len(zbz)):
    print(zbz[i]+ str(i))
niz='ketamangedae'
niz2=niz[0:5]+'in'
print(niz2)

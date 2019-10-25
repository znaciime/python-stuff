import copy

bag={'gold coin':42, 'rope':1}
dragonLoot=['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def newBag(oldBag, loot):
    temp=0
    vtemp=0
    nebag=copy.copy(oldBag)
    for i in range(len(loot)):
        
        
        for k, v in oldBag.items():
            if loot[i] != k:
               nebag.setdefault(loot[i], 1)
               
               
            if k==loot[i]:
               temp+=1 
               v+=temp
               vtemp=v
               
               nebag[k]=v
    print(nebag)           
    return nebag                
print(bag)
print(dragonLoot)
newBag(bag, dragonLoot)

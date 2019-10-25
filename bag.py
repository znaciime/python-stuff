import pprint
stuff={'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}
pprint.pprint(stuff)
def displayInventory(inventory):
    print('inventory:')
    item_total=0
    for k, v in inventory.items():
        print(k,':', v)
    for v in inventory.values():
         item_total=item_total+v
    print(item_total)
displayInventory(stuff)

def printPicnic(itemz, leftWidth, rightWidth):
    print('Picnic Items'.center(leftWidth+rightWidth, '-'))
    for k, v in itemz.items():
        print(k.ljust(leftWidth, '.')+str(v).rjust(rightWidth))
picnicItems = {'apples':3, 'bannanas':2, 'zerg':345, 'protos':122,}
printPicnic(picnicItems, 30, 0)

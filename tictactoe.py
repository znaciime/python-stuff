theBoard={
    'top-L':' ', 'top-M':' ', 'top-R':' ',
    'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
    'low-L':' ', 'low-M':' ', 'low-R':' ',
    }
def printBoard(board):
    print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
    print('-+-+-')
    print(board['low-L']+'|'+board['low-M']+'|'+board['low-R'])
turn='X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for'+ turn+ '.Move to which space:')
    move=input()
    theBoard[move]=turn
    if turn=='X':
        turn='O'
    else:
        turn='X'
    if theBoard['top-L']==theBoard['top-M'] and theBoard['top-M']==theBoard['top-R']:
        print('The winner is :'+ theBoard['top-L'])
        
    elif theBoard['mid-L']==theBoard['mid-M'] and theBoard['mid-M']==theBoard['mid-R']:
        print('The winner is :'+theBoard['mid-L'])
        
    elif theBoard['low-R']==theBoard['low-M'] and theBoard['low-M']==theBoard['low=R']:
        print('the winner is :'+theBoardp['low-L'])
        
    elif theBoard['top-L']==theBoard['mid-M'] and theBoard['mid-M']==theBoard['low-R']:
        print('The winner is :'+theBoard['top-L'])
       
    elif theBoard['low-L']==theBoard['mid-M'] and theBoard['mid-M']==theBoard['top-R']:
        print('The winner is :'+theBoard['low-L'])
       
printBoard(theBoard)


def collatz():
    for i in range(11):
        print('unesite broj')
        numz=int(input())
        if numz%2==0:
            print(numz/2)
            continue
        elif numz%2==1:
            print(3*numz+1)
            continue
        elif numz==str(numz):
            print('its not a number')
            break
collatz()

def isPhoneNumber(text):
    if len(text) !=12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] !='-':
        return False
    if text[7] !='-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True
message='call me at 514-444-1001 tomorrow'
for i in range(len(message)):
    chunk=message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found '+chunk)
        print('done')
print(isPhoneNumber('444-555-6666'))

    

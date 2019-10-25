import re, pyperclip
phoneRegex=re.compile(r'''(
    (\d{3}|\(\d{3}\))? 
    (\s|-|\.)?
    (\d{2})?
    (\s|-|\.)?
    (\d{4})
    (\s|-|\.)?
    (\d{3,4})?
    )''', re.VERBOSE)
emailRegex=re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''',re.VERBOSE)
text=str(pyperclip.paste())
matches=[]
for groups in phoneRegex.findall(text):
    phoneNum='-'.join([groups[1], groups[3], groups[5], groups[7]])
    if groups[6] !='':
        phoneNum+=' x'+ groups[6]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard:')
    print('\n'.join(matches))
else:
    print('no phone numbers or emils found.')


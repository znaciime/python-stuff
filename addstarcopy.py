#program to add star (*) at the begining of the line of the copied text
#first copy text to clipboard then run program!
#text must be decoded to use it since python 3

import pyperclip
text=pyperclip.paste()
lines=text.decode('utf8').split('\n')
for i in range(len(lines)):
    lines[i]='*'+lines[i]
text='\n'.join(lines)
pyperclip.copy(text)
print(text)

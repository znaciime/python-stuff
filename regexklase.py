#regex klase
import re
xmasRegex=re.compile(r'\d\s\w+')
mo=xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo)
#\d cifre, \Dkarakteri koji nisu cifre, \w slova cifre donja crta, \W znakovi, \s space nova linija tab, \Ssve osim space taba i nove linije

#kreiranje sopstvenih klasa [] pretraga samoglasnika npr
vowelReg=re.compile(r'[aeiouAEIOU]')
mo2=vowelReg.findall('tanananana batman')
print(mo2)
#sa ^ ispred pretrage dobija suprotne karaktere od prosledjenih suglasnike npr
vowelReg3=re.compile(r'[^aeiouAEIOU]')
mo3=vowelReg3.findall('tanananana batman')
print(mo3)

beginswithhello=re.compile(r'^Hello')
mo4=beginswithhello.findall('Hello World')
print(mo4)
# $ se koristi na kraju prosledjenih argumenata da nadjemo karakter na kraju niza
endsWithNumb=re.compile(r'\d$')
mo5=endsWithNumb.findall('Your Number is 42')
print(mo5)
#whole string number
wholeStringNumb=re.compile(r'^\d+$')
moc=wholeStringNumb.findall('1234567890')
print(moc)
wholeStringNumb1=re.compile(r'\d{5}\D\D\d{4}')
moc1=wholeStringNumb1.findall('123456cx7890')
print(moc1)
wholeStringNumb2=re.compile(r'^\d+\D+\d+$')
moc2=wholeStringNumb2.findall('43opao34')
print(moc2)
# . znak podudaranja sa svim osim sa \n
atRegex=re.compile(r'.at')
mox=atRegex.findall('The cat sat i n the hat at the flat mat')
print(mox)
#pretraga svega .* tacka sve a zvezdica nista sto prethodi tekstu
nameRegex=re.compile(r'First name:(.*) Last name:(.*)')
moa=nameRegex.findall('First name: All Last name: Sweigart')
print(moa)
# pretrage .* pretrazuje gramzivo sto duze podudaranje ? ogranicava na najkraci odgovarajuci niz

noGready=re.compile(r'Ha')
mog=noGready.findall('HaHaHaHahaha Ha HaHa HA ')
print(mog)
# ignorisanje velicine slova u pretrazi re.I ili re.IGNORECASE
robocop=re.compile(r'robocop', re.I)
moi=robocop.search('RobocOp is part man   Part Machine')
print(moi.group(0))
#Zamena delova teksta u nizu metodom sub()
nameReg=re.compile(r'Agent \w+')
mol=nameReg.sub('CENSORED', 'Agent Alice gave Agent Bill a 600000 dollars')
print(mol)


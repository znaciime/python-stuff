import pprint
def servis():
    izbor1="da"
    izbor2="ne"
    print('Da li dodajete novi servis?')
    odgovor=input()
    if (odgovor.lower() == izbor1):
        print('Unesite ime i prezime korisnika:')
        imeiprezime=input()
        if imeiprezime=='':
            print("Niste uneli ime i prezime korisnika!")
            imeiprezime=input()
        print('Unesite marku automobila:')
        marka=input()
        if marka=='':
            print('Niste uneli marku automobila!')
            marka=input()
        print('Unesite model auta:')
        modelz=input()
        if modelz=='':
            print('Niste uneli model auta!')
            modelz=input()
        print("Unesite broj motora(opciono):")
        motorje=input()
        print("Unesite broj sasije(opciono):")
        sasija=input()
        print("Unesite snagu motora(KW):")
        snaga=input()
        print("Godina proizvodnje:")
        god=input()
        print("Kubikaza auta:")
        kubika=input()
        print("Nasuto ulja(opciono):")
        ulje=input()
        print("Unesite datum servisa:")
        datum=input()
        print("Sta je zamenjeno na servisu:")
        detaljno=input()
        baza=open('MarkovicServis.txt', 'a')
        bazaserv={'Redni broj servisa:':'1' or len(baza),'Ime i prezime:':imeiprezime , 'Marka automobila:':marka ,'Model auta:':modelz , 'Broj motora:':motorje , 'Broj sasije:':sasija ,'Snaga KW/KS:':snaga+'Kw,'+str(int(snaga)*1.36)+'Ks' , 'Godina proizvodnje:':god, 'Kubikaza:':kubika, 'Nasuto ulja litara:':ulje, 'Datum servisa:':datum, 'Sta je uradjeno na servisu:':detaljno}
        baza.write(str(bazaserv))
        baza.close()
    if (odgovor == izbor2.lower()):
        print("Da li zelite listu svih servisa?")
        izbor3='da'
        odgovor2=input()
        if (odgovor2.lower() == izbor3):
            baza2=open('MarkovicServis.txt', 'r')
            baza3=baza2.read()
            pprint.pprint(str(baza3).split(','))
            baza2.close()
        if (odgovor2.lower()=='ne'):
            print('Pretraga servisa:')
            baza4=open('MarkovicServis.txt', 'r')
            pretraga=input()
            x=str(baza4.read()).split("'")
            z=x.index(pretraga)
            i=0
            while i < 41:
                if (i%2==0):
                    print(x[z+i])
                i+=1
            baza4.close()
        
servis()

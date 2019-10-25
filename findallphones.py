#findall method
import re
phoneNumbReg=re.compile(f'\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneNumbReg.findall('cel 000-111-2222, at work 222-333-4444')
print(mo)

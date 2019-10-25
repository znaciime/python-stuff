#visestruko podudaranje u zagradama odvojeno uspravnom crtom
import re
phoneNumberRe=re.compile(r'Bat(man|mobile|woman)')
mo=phoneNumberRe.search('The Amazing Batmobile')
print(mo.group(0))
#opciono podudaranje upitnikom
phoneNumberRe2=re.compile(r'Bat(wo)?man')
mo1=phoneNumberRe.search('The Amazing Batwoman')
print(mo1.group(0))
#podudaranje sa zvezdicom vise istih grupa
phoneNumberRe3=re.compile(r'Bat(wo)*man')
mo3=phoneNumberRe3.search('The Amazing Batwowowowowoman')
print(mo3.group(0))

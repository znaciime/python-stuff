import smtplib
smtpObj=smtplib.SMTP('smtp-mail.outlook.com', 587)
smtpObj.ehlo()
print(smtpObj.ehlo())
#greet server message
smtpObj.starttls()
#start encripted conection
smtpObj.login('example@hotmail.com', 'passswooord')

smtpObj.sendmail('example@hotmail.com', 'receiver@hotmail.com', 'Subject: SOME TEXT')
smtpObj.quit()

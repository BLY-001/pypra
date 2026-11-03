THIS CODE HAS NOT BEEN RAN YET SUBJECT TO FURTHER RESEARCH
#SENDING EMAILS WITH PYTHON
#simple mail transfer protocol(SMTP)
#i will need to do more research on the smtplib in python


# this lecture will be mainly about how to send email using python it is common for an application to send emails automatically,
#some usecases are to send a confirmation email after a user has created an account and send an otp when authenticating to a secure service, send a report or a log summmary etc

#THE protocol used to send email is called SMTP(Simple Mail Transfer Protocol) there is a python standard library called smtplib that can be imported and used for this purpose , in this lecture first how to send text email will be taught

#inorder to send an email you need an email server,the python script will act as anm smtp or email client that will authenticate to the email server which will inturn send the message to the recipient
# nb: if you have a gmail account the next step is to allow less secure apps in the security tab of your gmail
#this is necessary to allow the python application to access the google account if you dont want to allow less secure app access(which are all the application that do not meet google's security standards to access your gmail account then you can use the gmail API for python and oAuth2)

#sending simple text email
import smtplib
from email.message import EmailMessage

email = EmailMessage() #creating a email of type EmailMessage

#the next steps are to set the sender, the recipient and the subject of the email
#you set all of these like the values of a dictionary

email['from'] = 'pythoon <masterpythonprogramming@gmail.com' #mail of the sender
email['to'] = 'andrei.cma@protonmail.com'
email['subject'] = 'Good job Python!'

email.set_content('Wow! Congratulations!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp: # you can search for simple mail transfer protocol
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login("masterpythonprogramming@gmail.com", 'GdSrjmas7')
    smtp.send_message(email)
    print('the mail was sent')

    # NB: DO NOT NAME YOUR PYTHON FILES AS A PYTHON MODULE OR YOU WILL GET AN ERROR

    
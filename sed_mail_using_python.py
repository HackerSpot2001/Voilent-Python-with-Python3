#!/usr/bin/python3
import smtplib
from email.mime.text import MIMEText

# myMail = "abhisheksagar2856@gmail.com"
# toMail = "abhisheksagar513@gmail.com"
# s = smtplib.SMTP('smtp.gmail.com',587)
# s.starttls()
# s.login(myMail,"9643561451")
# message = "This is me and testing Mail"
# s.sendmail(myMail,toMail,message)

def sendMail(your_email,email_passwd,target_email,message,subject):
    msg = MIMEText(message)
    msg['From'] = your_email
    msg['To'] = target_email
    msg['Subject'] = subject
    try:
        smtpServer = smtplib.SMTP('smtp.gmail.com',587)
        print("[+] Connecting to Mail Server.")
        smtpServer.ehlo()
        print("[+] Starting Encrypted Session.")
        smtpServer.starttls()
        smtpServer.ehlo()
        print("[+] Loggining into Mail Server.")
        smtpServer.login(your_email,email_passwd)
        print("[+] Sending Message to {}.".format(target_email))
        smtpServer.sendmail(your_email,target_email,msg.as_string())
        smtpServer.close()
        print("[+] Mail sent Successfully.")
    
    except Exception as e:
        print("[!] Error: {}".format(e))

if __name__ == "__main__":
    myMail = 'abhisheksagar2856@gmail.com'
    password = '9643561451'
    target = 'abhisheksagar513@gmail.com'
    msg = 'i am Abhisek. If you got this Mail successfully. Then Whatsapp me. ' 
    subject = "Python testing mail Service."
    sendMail(myMail,password,target,msg,subject)

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class GmailMailer():
    def getPassword(self):
        file=open('password','r')
        return file.readline()
    def add(self,a,b):
        return a+b

    def sendMail(self, emailAddress, subject='Testing', body="Whe just checked"):
        fromaddr = "loggerdemon@gmail.com"  # Your Email Address
        toaddr = emailAddress  # whom you want to send to
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = subject
        # body = "Hi all this was an automation done by me + Python with core SMTP libraries"
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, '2607Overdose')
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        print("an email with subject was sent successfully ")




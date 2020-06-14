from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from urllib.request import urlopen
from bs4 import BeautifulSoup

s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('Your Email ID','Your Password')
print('Login Successful')
def mail_sender(data = []): 
    #msg="Hello"
    #s.sendmail('From Email',' To EMail',msg)
    #print("Message sent Successfully")
    msg = MIMEMultipart()
    msg['from'] = 'Sender_email'
    msg['to'] = 'Receiver_email'
    msg['subject'] = 'This is test'
    #body1 = scrap_data('https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India')
    for i in data:
        msg.attach(MIMEText(i + "\n", 'plain'))
    try:
        s.sendmail('from_Email','to_Email',str(msg))
        print("Message Sent Successful")
    except AttributeError:
        print("Attribute Error")
#mail_sender()
def scrap_data(link):
    """ Returns data reside in <tag> from the link user provides"""
    content = urlopen(link)
    soup= BeautifulSoup(content,'html.parser')
    title = soup.find('title')
    for i in soup.find_all('a'):
        hyperlinks = i.get('href')
    # Add many more tags for the data you need
    return title.string

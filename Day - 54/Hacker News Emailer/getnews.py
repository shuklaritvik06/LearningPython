import requests
from bs4 import BeautifulSoup
import smtplib
import datetime as dt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

class GetNews:
    def __init__(self):
        self.date = dt.datetime.now()
        self.url = 'https://news.ycombinator.com/'
        self.content = []
        self.username = os.environ.get('EMAIL')
        self.password = os.environ.get('EMAIL_PASSWORD')
        self.FROM = os.environ.get('EMAIL')
        self.TO = os.environ.get('EMAIL')
    def get_content(self):
        response = requests.get(self.url)
        content = response.content
        soup = BeautifulSoup(content,'html.parser')
        title = soup.find_all('a',class_="titlelink")
        link = soup.find_all('span',class_="sitestr")
        try:
            j = 0
            for i,tag in enumerate(title):
                text = tag.text
                cnt = f"{i+1}- {text} <em><a href={link[j].text}>See more</a></em>"
                if cnt!="More":
                    data = ''
                    data+=cnt
                    j+=1
                    self.content.append(data)
        except:
            j=1
            for i,tag in enumerate(title):
                if i!=0 and j<len(title):
                    text = tag.text
                    cnt = f"{i}- {text} <em><a href={link[j].text}>See more</a></em>"
                    if cnt!="More":
                        data = ''
                        data+=cnt
                        j+=1
                        self.content.append(data)

    def sendmail(self):

        message = '<b>Top HN Stories</b><br><br>'
        for i in self.content:
            message+=i+"<br>"
        msg = MIMEMultipart()
        msg['Subject'] = f"Top HN Stories for {self.date.day}-{self.date.month}-{self.date.year}"
        msg['From']= self.FROM
        msg['To']= self.TO
        msg.attach(MIMEText(message,'html'))
        Connection = smtplib.SMTP("smtp.gmail.com")
        Connection.starttls()
        Connection.login(self.username, self.password)
        print('Sending mail......')
        try:
            Connection.sendmail(from_addr=self.FROM,to_addrs= self.TO,msg=msg.as_string())
            print("Mail Sent!")
        except Exception as e:
            print('ERROR',e)
        Connection.quit()

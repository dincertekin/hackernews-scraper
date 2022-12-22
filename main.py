import requests
import bs4
import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_mail = "greejolly@gmail.com"
sender_password = "xqirehabrrbknemr"
receiver_mail = "lawnless@protonmail.com"
content_string = ""

content_string += "Here is the latest Hacker News:\n<br>"
response = requests.get('https://news.ycombinator.com/newest')
soup = bs4.BeautifulSoup(response.content, 'html.parser')
for i, tag in  enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
    if tag.text != 'More':
        content_string += ('<b>'+str(i+1)+')</b> <a href="'+tag.a.get('href')+'">'+tag.text+'</a>\n<br>')
content_string += "\n------------<br>"
content_string += "\nEnd of the Message<br>"
content_string += '\nMade by <a href="https://www.dincertekin.com">Dinçer Tekin</a> with ❤'

now = datetime.datetime.now()

message = MIMEMultipart()
message['Subject'] = 'Top New Stories HackerNews [Automated Email]'+' '+str(now.day)+'/'+str(now.month)+'/'+str(now.year)+' '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
message['From'] = sender_mail
message['To'] = receiver_mail
message.attach(MIMEText(content_string, 'html'))

server = smtplib.SMTP('smtp.gmail.com', 587);
server.starttls();
server.login(sender_mail, sender_password);
print("Login success!")
server.sendmail(sender_mail, receiver_mail, message.as_string())
print("Email sent!")
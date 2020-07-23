# /send.py
# If you get an error when logging in, turn this setting on: https://myaccount.google.com/lesssecureapps
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config as cfg
import requests
import smtplib
import ssl


# Gets information from config file
SENDER_EMAIL = cfg.email['sender']
RECEIVER_EMAIL = cfg.email['receiver']
SMTP_SERVER = cfg.email['smtp']
PASSWORD = cfg.pwd['sender_pwd']


# Get word of the day
try:
    page = requests.get("https://www.dictionary.com/e/word-of-the-day/")
except:
    print('Couldn\'t fetch from dictionary.com. Most likely a connection issue.')
    exit(1)
soup = BeautifulSoup(page.content, 'html.parser')

wotd_item = soup.find('div', class_='wotd-item')

word = wotd_item.find(class_='otd-item-headword__word').get_text().split('\n')[1]
headword = list(filter(None, wotd_item.find(class_='otd-item-headword__pos').get_text().split('\n')))
pos_word, def_word = headword[0], headword[1]
# print(f'Word: {word}\nPart of speech: {pos_word}\nDefinition: {def_word}')


# Create email content
message = MIMEMultipart("alternative")
message["Subject"] = f"Word of the Day! {word}"
message["From"] = SENDER_EMAIL
message["To"] = RECEIVER_EMAIL

# Create the HTML of the message
html = f"""\
<html>
    <body>
        <h1>{word}</h1>
        <hr>
        <p><i>{pos_word}</i></p>
        <p style="font-size: 150%">{def_word}</p>
        <h5><a href="https://www.google.com/search?q={word}">Lookup "{word}" for more info.</a></h5>
    </body>
</html>
"""
message.attach(MIMEText(html, "html"))

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL(SMTP_SERVER, 465, context=context) as server:
    server.login(SENDER_EMAIL, PASSWORD)
    server.sendmail(
        SENDER_EMAIL, RECEIVER_EMAIL, message.as_string()
    )

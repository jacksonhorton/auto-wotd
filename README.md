# auto-wotd
Emails you the current word-of-the-day from dictionary.com in some *fancy* HTML!

# Use
You can use auto-wotd by simply running the *send.py* file. **However**, you have to setup the config.py file first.

## Setup
Just change the information already in the config.py to suit your needs.

```
  email = {
      'sender': 'myemail@gmail.com',
      'receiver': 'johndoe@yahoo.com',
      'smtp': 'smtp.gmail.com'
  }
  pwd = {
      'sender_pwd': 'password'
  }
```

The *'sender'* and *'receiver'* addresses can be the same. Also, if you need help finding the smtp server of your *'sender'* email address, check [HERE](https://www.arclab.com/en/kb/email/list-of-smtp-and-pop3-servers-mailserver-list.html) and make sure to pick the smtp server with SSL if available!

# Dependencies
The following modules are required for this to work:
`
beautifulsoup4
requests
smtplib
ssl
MIMEMultipart
MIMEText
`

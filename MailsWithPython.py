import smtplib #Simple Mail Transfer Protocol
from email.message import EmailMessage

email = EmailMessage()
email['from'] = '...'
email['to'] = '...'
email['subject'] = '...'
email.set_content('...')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp: #you can use port 465
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email','password')
    smtp.send_message(email)
    print('The message was sent!')

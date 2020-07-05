import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Guna Bhushan'
email['to'] = 'gunabhushan111@gmail.com'
email['subject'] = 'qwerty'
email.set_content(html.substitute(name='Guna'),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('dummyacco129009@gmail.com','qwerasdf123!@#')
	smtp.send_message(email)
	print('all done')
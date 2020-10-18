import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())



email = EmailMessage()
email['from']='Nerio Gonzalez'
email['to']='neriogonzalez@gmail.com'
email['subject']='correo de prueba desde python'

email.set_content(html.substitute(name = 'Tintin'), 'html')
#email.set_content('Este es mi primer email desde python')
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('dummyneriogonzalez@gmail.com', 'Dummy1248357')
    smtp.send_message(email)
    print('Enviado')


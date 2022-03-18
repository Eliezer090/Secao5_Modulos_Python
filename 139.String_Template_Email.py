from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from email import policy

email = input('Email: ')
senha = input('Senha: ')


with open('template.html', 'r') as html:
    template = Template(html.read())
    data = datetime.now().strftime('%d/%m/%Y')
    corpo_mgs = template.safe_substitute(nome='Eliézer', data=data)

msg = MIMEMultipart(policy=policy.default)
# Quem está enviando a msg
msg['from'] = 'Eliézer'
# Para quem está indo a msg
msg['to'] = email
# Assunto do e-mail
msg['subject'] = 'E-mail de testes'

corpo = MIMEText(corpo_mgs, 'html')
msg.attach(corpo)

with open('imagem.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email, senha)
        smtp.send_message(msg)

        print('Email enviado')
    except Exception as e:
        print('Erro: ', e)

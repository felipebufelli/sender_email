import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr

# Parameters
host = "smtp.gmail.com"
port = 587
#------
authentication_email = "example@gmail.com"
password = "****"
#------
from_email = "From Email <from_email@gmail.com>"
receiver_email = "to_email@gmail.com"

# Create message object and atributte informations
message = MIMEMultipart()
message["Subject"] = "Recuperação de Senha"
message["From"] = from_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Testando envio de e-mails com python
"""

# Turn these into plain MIMEText objects
part1 = MIMEText(text, "plain")


# The email client will try to render the last part first
message.attach(part1)
# message.attach(part2)


# Create secure connection with server and send email
context = ssl.create_default_context()

with smtplib.SMTP(host= host, port= port) as server:
    
    try:
        server.ehlo()
        server.starttls()

        print("Iniciando login...")
        server.login(authentication_email, password)
        print("Login concluído\n")

        print("Iniciando envio do email...")
        server.sendmail(
            from_addr= from_email, 
            to_addrs= receiver_email,
            msg= message.as_string(),
        )
        print("Enviou de e-mail concluído\n")
    
    except Exception as error:
        print("\n\nERRO: ", error)

    server.quit()

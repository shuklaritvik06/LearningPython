import smtplib
from email.message import EmailMessage

mesg = EmailMessage()

mesg['subject'] = ""
mesg['From'] = ""
mesg['To'] = ""

mesg.add_alternative('''
<!DOCTYPE html>
<html lang="en">
  <head>
  </head>
  <body>
    <h1 style="color:red;">Hi I am HTML Email</h1>
  </body>
</html>
''','html')

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user="", password="")
    connection.send_message(mesg)
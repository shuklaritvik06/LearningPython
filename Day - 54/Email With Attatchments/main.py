import smtplib
import imghdr
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = "HI RS"
msg['From'] = ""
msg['To'] = ""
msg.set_content("Hey this is a attatchment email")

# FOR IMAGE

with open("Wallpaper.png","rb") as f:
    filedata = f.read()
    filename = f.name
    filtype = imghdr.what(filename)
msg.add_attachment(filedata,maintype='image',subtype=filtype,filename=filename)


# FOR PDF

# with open("file.pdf","rb") as f:
#     filedata = f.read()
#     filename = f.name
# msg.add_attachment(filedata,maintype='application',subtype="octet-stream",filename=filename)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user="", password="")
    connection.send_message(msg)
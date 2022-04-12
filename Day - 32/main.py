import smtplib
myemail = ""
mypasswd = ""
# Connect to SMTP mail server of your proivder
with smtplib.SMTP("smtp.gmail.com") as connection:
    # Encrypts the message and make it hard for anyone to hack and read, just to make connection secure
    connection.starttls()
    # Login to the email provider
    connection.login(user=myemail, password=mypasswd)
    connection.sendmail(from_addr=myemail,
                        to_addrs="", msg="Subject:Hello\n\nHi Happy Birthday")

import smtplib
import random
import datetime as dt
myemail = ""
password = ""
time = dt.datetime.now()
with smtplib.SMTP("smtp.gmail.com") as connection, open("quotes.txt") as file:
    quote = file.readlines()
    data = random.choice(quote)
    quote_message = data.strip().replace('\"', '')
    connection.starttls()
    connection.login(user=myemail, password=password)
    if time.weekday() == 4:
        print("Sending an email....")
        connection.sendmail(from_addr=myemail,
                            to_addrs="", msg=f"Subject:You can do it!\n\n{quote_message}")

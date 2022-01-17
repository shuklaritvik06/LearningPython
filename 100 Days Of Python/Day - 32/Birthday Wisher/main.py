import pandas
import datetime as dt
import random
import smtplib
MYEMAIL = ""
MYPASSWORD = ""
data = pandas.read_csv("birthdays.csv")
for index, row in data.iterrows():
    if row.day == dt.datetime.now().day and row.month == dt.datetime.now().month:
        bd_day = row.day
        bd_month = row.month
        bd_name = row.Name
        bd_email = row.email
num = random.randint(1, 3)
with smtplib.SMTP("smtp.gmail.com") as connection, open(f"letter_templates/letter_{num}.txt") as file, open(f"Output_Mail_data/message_{bd_name}.txt", "w") as output:
    connection.starttls()
    connection.login(user=MYEMAIL, password=MYPASSWORD)
    my_data = file.read()
    my_replace = {"[MONTH]": f"{bd_month}",
                  "[DAY]": f"{bd_day}", "[NAME]": bd_name}
    for key, value in my_replace.items():
        my_data = my_data.replace(key, value)
    today = dt.datetime.now()
    print("Sending an email.....")
    try:
        connection.sendmail(from_addr=MYEMAIL, to_addrs=f"{bd_email}",
                            msg="Subject:Happy Birthday!\n\n"+my_data)
    except Exception as e:
        output.write(e)
    else:
        output.write(f"{today}\n{my_data}")

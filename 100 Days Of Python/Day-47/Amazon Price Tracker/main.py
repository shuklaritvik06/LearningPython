from bs4 import BeautifulSoup
import smtplib
import os
import requests
headers ={
    "Accept-Language":"en-US",
    "User-Agent":"Mozilla"
}
response = requests.get(url="https://www.amazon.com/Garmin-Instinct-Solar-Powered-Smartwatch-Monitoring/dp/B089YVVLSW/?_encoding=UTF8&pd_rd_w=6q4Cv&pf_rd_p=bb36b0f2-940b-4dee-bad4-0ca8e4acea61&pf_rd_r=G203P9J2R2JZGDA4DR0V&pd_rd_r=3b2d9073-a01b-4b8f-b277-8e786c2141c8&pd_rd_wg=2SxOX&ref_=pd_gw_exports_top_sellers_unrec&th=1",headers=headers)
data = response.text
soup = BeautifulSoup(data,'lxml')
price = soup.select_one(selector="span.apexPriceToPay span").get_text()[1:]
title = soup.find(name='span',id="productTitle").get_text().strip(' ')
print(title)
if float(price)<250:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=os.environ.get('USERNAME'), password=os.environ.get('PASSWORD'))
        connection.sendmail(from_addr=os.environ.get('MYMAIL'), to_addr=os.environ.get('DESTMAIL'),mesg=f"Subject:Amazon Price Alert!!\n\nHey! Today the price of {title} is {price}, lower than your max budget, go buy now!")

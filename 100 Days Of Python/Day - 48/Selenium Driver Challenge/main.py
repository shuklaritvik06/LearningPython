from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
service = Service("/home/ritvik/Documents/Development/geckodriver")
driver = webdriver.Firefox(service=service)
driver.get("https://www.python.org/")
times_list = driver.find_elements(By.CSS_SELECTOR,".event-widget ul.menu li time")
title_list =  driver.find_elements(By.CSS_SELECTOR,".event-widget ul.menu li a")
date_list = [item.text for item in times_list]
event_list = [item.text for item in title_list]
mydict = {}
result_dict= {}
number = len(event_list)
for i in range(number):
    date = date_list[i]
    event = event_list[i]
    mydict[f"{i}"]={
        'time': f"{date}",
        'event':f"{event}"
    }
print(mydict)
driver.quit()
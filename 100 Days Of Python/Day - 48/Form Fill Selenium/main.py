from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
service = Service("/home/ritvik/Documents/Development/geckodriver")
driver = webdriver.Firefox(service=service)
driver.get("http://secure-retreat-92358.herokuapp.com/")
fName = driver.find_element(By.NAME,"fName")
lName = driver.find_element(By.NAME,"lName")
email = driver.find_element(By.NAME,"email")
fName.send_keys("Ramesh")
lName.send_keys("Babu")
email.send_keys("ramesh.babu@email.com")
button = driver.find_element(By.CLASS_NAME,"btn")
button.click()

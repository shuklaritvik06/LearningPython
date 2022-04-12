from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
import os

service = Service("/home/ritvik/Documents/Development/geckodriver")
driver = webdriver.Firefox(service=service)
driver.get("https://tinder.com/")
time.sleep(2)
cookies = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[1]/button')
cookies.click()
button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/div[3]/div/div[2]/button')
button.click()
time.sleep(3)
login_button = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button")
login_button.click()
time.sleep(2)
google_login_window = driver.window_handles[1]
driver.switch_to.window(google_login_window)
login_username = driver.find_element(By.CSS_SELECTOR,'input#email')
time.sleep(2)
login_username.send_keys(os.environ.get("NUM"))
passwd = driver.find_element(By.CSS_SELECTOR,'input#pass')
passwd.send_keys(os.environ.get('PASSWORD'))
login  = driver.find_element(By.NAME,'login')
login.click()
time.sleep(2)
access = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div')
access.click()

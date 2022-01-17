from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import os
import time

service = Service("/home/ritvik/Documents/Development/geckodriver")
driver = webdriver.Firefox(service=service)
driver.get("https://www.linkedin.com/home")
text = driver.find_element(By.LINK_TEXT,"Sign in")
text.click()
username = driver.find_element(By.ID,"username")
passwd = driver.find_element(By.ID,"password")
button = driver.find_element(By.CSS_SELECTOR,".login__form_action_container button")
username.send_keys(os.environ.get("USERNAME"))
passwd.send_keys(os.environ.get("PASSWD"))
button.click()
jobs_tab = driver.find_element(By.LINK_TEXT,"Jobs")
jobs_tab.click()
search = driver.find_element(By.CLASS_NAME,'jobs-search-box__keyboard-text-input')
search.send_keys("Python")
search_button = driver.find_element(By.XPATH,'/html/body/div[6]/header/div/div/div/div[2]/button[1]')
search_button.click()
time.sleep(4)
easy_apply = driver.find_element(By.CLASS_NAME,'search-reusables__filter-binary-toggle')
easy_apply.click()
time.sleep(3)
job_listings = driver.find_elements(By.CLASS_NAME,"job-card-container")
apply_button = driver.find_element(By.CLASS_NAME,"jobs-apply-button")
apply_button.click()
phone_num = driver.find_element(By.CLASS_NAME,"fb-single-line-text__input")
phone_num.send_keys(os.environ.get("PHONE_NUM"))
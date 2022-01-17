from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
import os

ORIGINAL_DOWN = 150.00
ORIGINAL_UP = 90.00

service = Service("/home/ritvik/Documents/Development/geckodriver")
driver = webdriver.Firefox(service=service)

i=0
urls= ["https://www.speedtest.net/","https://twitter.com"]
for url in urls:
    if i==0:
        driver.get(urls[0])
        button = driver.find_element(By.CLASS_NAME,'start-text')
        button.click()
        time.sleep(45)
        upload = driver.find_element(By.CLASS_NAME,'upload-speed').text
        download = driver.find_element(By.CLASS_NAME,'download-speed').text
    else:
        driver.get(urls[1])
        time.sleep(2)
        button = driver.find_element(By.XPATH,'/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/div[5]/a/div')
        button.click()
        time.sleep(7)
        username_input = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        username_input.send_keys(os.environ.get('USERNAME'))
        next_button = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div')
        next_button.click()
        time.sleep(7)
        password = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(os.environ.get("PASSWORD"))
        login_button = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')
        login_button.click()
        time.sleep(4)
        input_tweet = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        input_tweet.click()
        time.sleep(2)
        if upload!=str(ORIGINAL_UP) or download!= str(ORIGINAL_DOWN):
            input_tweet.send_keys(f"This is a test for my today's project, Tweeted by a bot.\n\nHey Internet Provider the net speed is low today {download} down and {upload} up while I pay for {ORIGINAL_DOWN} down and {ORIGINAL_UP} up")
            tweet_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
            tweet_button.click()
    i+=1
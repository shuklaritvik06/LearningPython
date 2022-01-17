import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class InstaFollower:
    def __init__(self):
        self.username = os.environ.get('INSTAUSERNAME')
        self.password = os.environ.get('INSTAPASSWORD')
        self.targetUsername = os.environ.get('TARGET')

    def login(self):
        service = Service("/home/ritvik/Documents/Development/geckodriver")
        self.driver = webdriver.Firefox(service=service)
        self.driver.get("https://instagram.com")
        time.sleep(4)
        username = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        password = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        button = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
        username.send_keys(self.username)
        password.send_keys(self.password)
        button.click()
        time.sleep(5)
        save_info = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/section/main/div/div/div/section/div/button')
        save_info.click()
        time.sleep(5)
        notif= self.driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div[3]/button[2]')
        notif.click()

    def search(self):
        time.sleep(5)
        input_element = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/section/nav/div[2]/div/div/div[2]')
        input_element.click()
        time.sleep(5)
        input_data = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/section/nav/div[2]/div/div/div[2]/input')
        input_data.send_keys(self.targetUsername)
        time.sleep(2)
        goal = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')
        goal.click()
    
    def Followfollowers(self):
        time.sleep(3)
        followers = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(3)
        try:
            while True:
                follow_button = self.driver.find_elements(By.CLASS_NAME,'y3zKF')
                try:
                    for follow in follow_button:
                        follow.click()
                        time.sleep(5)
                except:
                    follow.send_keys(Keys.END)
                    time.sleep(5)
        except:
            print("Followed all followers!!")
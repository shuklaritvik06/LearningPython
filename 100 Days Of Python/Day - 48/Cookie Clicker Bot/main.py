from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

service = Service("/home/ritvik/Documents/Development/geckodriver")
driver = webdriver.Firefox(service=service)
driver.get("https://orteil.dashnet.org/cookieclicker/")
cookie = driver.find_element(By.CSS_SELECTOR,"#bigCookie")
while True:
    ActionChains(driver).move_to_element(cookie).click().perform()

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
service = Service("/home/ritvik/Documents/Development/geckodriver")
driver = webdriver.Firefox(service=service)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
# all_portals = driver.find_element(By.LINK_TEXT,"All portals")
# all_portals.click()
search = driver.find_element(By.NAME,"search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

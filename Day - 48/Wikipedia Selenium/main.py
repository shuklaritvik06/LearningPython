from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
service = Service("/home/ritvik/Documents/Development/geckodriver")
driver = webdriver.Firefox(service=service)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
wiki_stats = driver.find_element(By.CSS_SELECTOR,"#articlecount a")
print(wiki_stats.text)
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
service = Service("/home/ritvik/Documents/Development/geckodriver")
driver = webdriver.Firefox(service=service)
driver.maximize_window()
driver.get("https://www.python.org/")
element = driver.find_element(By.XPATH,"/html/body/div/footer/div[2]/div/ul/li[3]/a")
print(element.text)
driver.quit()
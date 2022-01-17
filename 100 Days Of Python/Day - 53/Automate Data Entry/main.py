from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("/home/ritvik/Documents/Development/geckodriver")
driver = webdriver.Firefox(service=service)

header = {
    "User-Agent": "Mozilla",
    "Accept-Language": "en-US"
}
data = requests.get(url="https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",headers=header)

soup = BeautifulSoup(data.text,'html.parser')
address = []
links = []
prices = []
address_scrap = soup.select('.list-card-addr')
link_scrap = soup.select('.list-card-top a')
price_scrap = soup.select('.list-card-price')
for addr in address_scrap:
    address.append(addr.get_text())
for link in link_scrap:
    link = link["href"]
    if "http" not in link:
        link = f"https://www.zillow.com/{link}"
    else:
        links.append(link)
for price in price_scrap:
    price = price.get_text()
    prices.append(price)

for i in range(len(links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSd9Gk1_bMKNGyqgb-sOaDSqZdGFd5KYLhzXN_SPNvF_LJLFnQ/viewform?usp=sf_link")
    time.sleep(4)
    ques1 = driver.find_element(By.CSS_SELECTOR,'div.freebirdFormviewerViewNumberedItemContainer:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
    ques1.send_keys(address[i])
    ques2 = driver.find_element(By.CSS_SELECTOR,'div.freebirdFormviewerViewNumberedItemContainer:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
    ques2.send_keys(prices[i])
    ques3 = driver.find_element(By.CSS_SELECTOR,'div.freebirdFormviewerViewNumberedItemContainer:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
    ques3.send_keys(links[i])
    button = driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    button.click()
    time.sleep(5)
driver.quit()


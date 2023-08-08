import math
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://yohoho.cc/"
browser = webdriver.Chrome()
browser.get(link)

time.sleep(3)

h1 = browser.find_element(By.XPATH, '//*[@id="yohoho"]/div[1]')
h1 = h1.text

assert 'Yohoho' == h1
print('Good')

search = browser.find_element(By.XPATH, '//*[@id="search-title"]')
search.send_keys('Ностальгия')

click1 = browser.find_element(By.XPATH, '//*[@id="search"]')
click1.click()

time.sleep(3)
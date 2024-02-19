from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from time import sleep
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
url = 'https://www.walissonsilva.com/blog'
navegador.get(url)

driver.implicitly_wait(0.5)

navegador.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div/div[1]/div/input')
navegador.send("Selenium")




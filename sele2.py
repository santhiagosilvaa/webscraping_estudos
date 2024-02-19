import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options #definir tamanho da janela
from time import sleep

options = Options()
options.add_argument('window-size=400,800')

navegagor = webdriver.Chrome(options)

navegagor.get('https://www.airbnb.com.br/')
navegagor.implicitly_wait(0.5)
sleep(2)

button = navegagor.find_element(by=By.XPATH, value='//*[@id="react-application"]/div/div/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[1]/button')
button.click()
sleep(2)
button = navegagor.find_element(by=By.XPATH, value='//*[@id="accordion-body-/homes-where"]/section/div[1]/button/span/span[2]')
button.click()
sleep(2)
button = navegagor.find_element(by=By.XPATH, value='//*[@id="/homes-where-input"]')
button.click()
button.send_keys('Goiania')
sleep(2)
button = navegagor.find_element(by=By.XPATH, value='//*[@id="/homes-where-suggestion-0"]')
button.click()
sleep(2)



#continuar, aula 07 26min



#site = BeautifulSoup(navegagor.page_source, 'html.parser')

#print(site.prettify())
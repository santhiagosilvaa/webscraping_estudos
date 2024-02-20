import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options #definir tamanho da janela
from time import sleep

options = Options()
options.add_argument('window-size=400,800')

navegador = webdriver.Chrome(options)

navegador.get('https://www.airbnb.com.br/')
navegador.implicitly_wait(0.5)
sleep(2)

#button = navegagor.find_element(by=By.XPATH, value='//*[@id="react-application"]/div/div/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[1]/button')
button = navegador.find_element(by=By.CSS_SELECTOR, value='button')
button.click() #caixa de pesquisa
sleep(2)
button = navegador.find_element(by=By.XPATH, value='//*[@id="accordion-body-/homes-where"]/section/div[1]/button/span/span[2]')
button.click() #caixa de pesquisa
sleep(2)
button = navegador.find_element(by=By.XPATH, value='//*[@id="/homes-where-input"]')
#button.click() #caixa de pesquisa
button.send_keys('Goiania')
sleep(2)
button = navegador.find_element(by=By.XPATH, value='//*[@id="/homes-where-suggestion-0"]')
button.click() #name city
sleep(2)
button = navegador.find_element(by=By.XPATH, value='//*[@id="accordion-body-/homes-when"]/section/div/footer/button[2]')
button.click() #proximo
sleep(2)
button = navegador.find_element(by=By.XPATH, value='//*[@id="vertical-tabs"]/div[3]/footer/button[2]/span[1]/span').click()
sleep(2) #buscar

#pega um print do html dessa pagina
page_content = navegador.page_source

site = BeautifulSoup(page_content, 'html.parser')
print(site.prettify())
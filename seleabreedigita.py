from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Inicialize o WebDriver (ChromeDriver)
navegador = webdriver.Chrome()

# Abra a URL no navegador
url = 'https://www.walissonsilva.com/blog'
navegador.get(url)

# Defina um tempo de espera implícito para o navegador
navegador.implicitly_wait(0.5)

# Encontre a caixa de entrada usando XPath e clique nela
caixa = navegador.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div/div[1]/div/input')
caixa.click()

# Envie as teclas "data" para a caixa de entrada
caixa.send_keys('data')

# Aguarde 10 segundos (apenas para fins de demonstração)
sleep(10)

# Feche o navegador após a execução
navegador.quit()

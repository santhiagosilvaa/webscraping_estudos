import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_produtos = []

produto_nome = str(input('Qual produto você deseja pesquisar? '))
url = 'https://lista.mercadolivre.com.br/'
response = requests.get(url + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('li', attrs={'class': 'ui-search-layout__item shops__layout-item ui-search-layout__stack'})

for produto in produtos:
    titulo = produto.find('a', attrs='ui-search-item__group__element ui-search-link__title-card ui-search-link')
   # print(titulo.text) #titulo / nome do produto
    preco = produto.find('span', attrs='andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript')
   # print(preco.text) #preço do produto
   # print(titulo['href']) #link do produto
    lista_produtos.append([titulo.text, preco.text, titulo['href']])

prod = pd.DataFrame(lista_produtos, columns=['NOME', 'PREÇO', 'LINK'])
print(prod)




#print(produtos)
#print(site.prettify)
import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com/')
content = response.content #conteudo html do site

#converte conteudo html para beautiful soup
site = BeautifulSoup(content, 'html.parser')

#entra no site e encontre uma div com classe xxx
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
    #na noticia encontre a com atributo xxx e printa o texto
    titulo = noticia.find('a', attrs='feed-post-link')
   # print(titulo.text)
   # print(titulo['href'])
  #  print()

    lista_noticias.append([titulo.text, titulo['href']])

#print(lista_noticias)
news = pd.DataFrame(lista_noticias, columns=['TITULO', 'LINK'])
news.to_excel('noticias.xlsx', index=False)

print(news)
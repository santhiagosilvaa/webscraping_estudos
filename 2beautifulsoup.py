import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')
content = response.content #conteudo html do site

#converte conteudo html para beautiful soup
site = BeautifulSoup(content, 'html.parser')

#entra no site e encontre uma div com classe xxx
noticia = site.find('div', attrs={'class': 'feed-post-body'})

#na noticia encontre a com atributo xxx e printa o texto
titulo = noticia.find('a', attrs='feed-post-link')
print(titulo.text)
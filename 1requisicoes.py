import requests

response = requests.get('https://www.google.com.br')

#código de status
print(f'Status code: \n\n\n{response.status_code}')

#cabeçalho - informações
print(f'\n\n\n HEADER --- \n\n\n{response.headers}')

#conteudo da pagina - html
print(f'\n\n\n CONTEUDO --- {response.content}')
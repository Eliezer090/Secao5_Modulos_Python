'''
    Ler uma pagina WEB e pagar o conteudo dela
'''

import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/search?q=pyhton'
response = requests.get(url)
# print(response.text)
html = BeautifulSoup(response.text, 'html.parser')

for pergunta in html.select('.question-summary'):
    titulo = pergunta.select_one('.question-hyperlink')
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.vote-count-post')

    print('Titulo: ', titulo.text.replace('P:', '').strip())
    print('Data: ', data.text)
    print('Votos: ', votos.text)
    print('--------------------')

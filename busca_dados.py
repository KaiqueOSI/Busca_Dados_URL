import requests as rq

#Importando documentação do BeautifulSoup, se tiver dúvidas pesquise no google BeautifulSoup para mais informações.
from  bs4 import BeautifulSoup as BS
cabeçalho = {'User-agent': ''}

# Utilizando a url do site em que deseja buscar a informação.
url = 'https://www.exemplo.br/'
requisição = rq.get(url, headers=cabeçalho)

#Decodificando dados
requisição.encoding = requisição.apparent_encoding
conteudo = BS(requisição.text)

#Formato de lista
cursos = list()

#Buscando a classe ou tag onde estão as informações no site, se tiver dúvidas inspecione o site para achar a tag em que está a informação.
for titulo in conteudo.find_all('ul' and 'li' and 'a'):
    cursos.append(titulo.get_text().strip())
print(cursos)
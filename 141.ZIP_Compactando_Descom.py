from zipfile import ZipFile
import os

caminho = '/Users/es19237/Desktop/Python/vercel-django-example/'
# Gera o zip
with ZipFile('arquivos.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)
# Lê os arquivos dentro do zip sem precisar extrair
with ZipFile('arquivos.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)
# Extrai os arquivos do zip
with ZipFile('arquivos.zip', 'r') as zip:
    zip.extractall('descompactado')

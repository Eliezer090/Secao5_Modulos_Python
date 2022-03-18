# Como rodar pelo terminal, cuidar pois muda de sistema para sistema.
# Mostrado também como passar parametros muito importante
from ast import arguments
import sys
import os
argumentos = sys.argv
print(argumentos)
qtd_args = len(argumentos)
if qtd_args <= 1:
    print('Falta argumentos')
    print('-a', 'Listar todos os arquivos da pasta')
    print('-d', 'Listar todos os diretórios desta pasta')
    sys.exit()
else:
    for arquivo in os.listdir('.'):
        if '-a' in argumentos:
            if os.path.isfile(arquivo):
                print('Arquivos', arquivo)
        if '-d' in argumentos:
            if os.path.isdir(arquivo):
                print('Diretorios', arquivo)

if '-d=Meu nome' in argumentos:
    print('Meu nome')

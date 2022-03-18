from collections import deque
from time import sleep
# Lifo - Last In First Out
# ultimo a entrar, primeiro a sair
"""
livros = list()
livros.append('Livro 1')
livros.append('Livro 2')
livros.append('Livro 3')
livros.append('Livro 4')
livros.append('Livro 5')
print(livros)
livro_removido = livros.pop()
print(livros)
print('Pego o Livro: {}'.format(livro_removido))
"""
# Fila - First In First Out
# Primeiro a entrar, primeiro a sair
"""
fila = deque()
print(fila)
fila.append('Joao')
fila.append('Maria')
fila.append('Jose')
fila.append('Pedro')
fila.append('Ana')

print('Saiu {}'.format(fila.popleft()))
print('Saiu {}'.format(fila.popleft()))
print('Saiu {}'.format(fila.popleft()))
print(fila)
"""

# Mantem os ultimos 10 elementos na minha fila
fila = deque(maxlen=10)
for i in range(100):
    fila.append(i)
    sleep(1)
    print(fila)

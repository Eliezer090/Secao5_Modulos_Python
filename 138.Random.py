import random
import string
inteiro = random.randint(10, 20)
print(inteiro)
# Gera numero aleatório usando a range()
inteiro = random.randrange(900, 1000, 10)
print(inteiro)

flutuante = random.uniform(10, 20)
print(flutuante)
# Gera un numero flutuante entre 0 e 1
flutuante = random.random()
print(flutuante)

lista = [
    'luiz', 'otavio', 'maia', 'rose', 'felipe', 'joao'
]
# Unico item
#sorteio = random.choice(lista)
# Mais de um item, pode repetir o mesmo item
sorteio = random.choices(lista, k=2)
# Mais de um item, mas nao repete
sorteio = random.sample(lista, k=2)
print(sorteio)

# Embaralha a lista
random.shuffle(lista)
print(lista)


# Gera senha aleatoria
letras = string.ascii_letters  # Minuscula e maiuscula
digitos = string.digits
caracteres = '!@$#%&*(()_+.,'

geral = letras+digitos+caracteres
# Join junta os valores, pois o choives retorna uma lista
senha = "".join(random.choices(geral, k=20))
print(senha)

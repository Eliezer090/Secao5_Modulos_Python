from threading import Thread, Lock
from time import sleep
"""
#Maneira 1
class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread('Thread 1', 5)
t1.start()

t2 = MeuThread('Thread 2', 1)
t2.start()

t3 = MeuThread('Thread 3', 2)
t3.start()


for i in range(10):
    print(i)
    sleep(1)

"""

"""
# Maneira 2
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t = Thread(target=vai_demorar, args=('Thread 4', 5))
t.start()

# Forçando o codigo esperar a thread acabar
while t.is_alive():
    print('Esperando a thread 4 terminar')
    sleep(1)
# ou para esperar a thread acabar pode usar o join
# t.join()

for i in range(10):
    print(i)
    sleep(1)
"""

# Problema ao usar thead


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, nome, qtd):

        self.lock.acquire()
        print('Executando a thread {nome} com {qtd} ingressos'.format(
            nome=nome, qtd=qtd))
        if self.estoque > 0:

            if self.estoque >= qtd:
                self.estoque -= qtd
                print('Comprou {qtd} ingresso(s)'.format(qtd=qtd))
                print('Ainda restam {qtd} ingresso(s)'.format(
                    qtd=self.estoque))
            else:
                comprou = self.estoque
                faltou = qtd - comprou
                self.estoque = 0
                print('Aprovou a compra de {qtd} ingresso(s)'.format(
                    qtd=comprou))
                print('Sem estoque disponivel para a compra dos {qtd} ingresso(s)'.format(
                    qtd=faltou))
            sleep(2)
        else:
            print('Sem ingressos')
        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)
    for i in range(1, 10):
        t = Thread(target=ingressos.comprar, args=('T1', i,))
        t.start()
        t2 = Thread(target=ingressos.comprar, args=('T2', i+3,))
        t2.start()
        t3 = Thread(target=ingressos.comprar, args=('T3', i+1,))
        t3.start()

import csv
"""
Como ler o arquivo de 2 formas
with open('clientes.csv', 'r') as arquivo:
    # Retorna em forma de arays: []
    # dados = csv.reader(arquivo)
    # Retorna em forma de dicionario {}
    dados = csv.DictReader(arquivo)
    # next(dados)
    for dado in dados:
        # Quando é dado o reader que retorna []
        # print(dado[1],dado[2])
        print(dado['Nome'], dado['Sobrenome'])

"""
# Como ler o arquivo e passar para outro arquivo, pode ser usado para trabalhar com os dados para limpar eles por exemplo
with open('clientes.csv', 'r') as arquivo:
    # Converte aqui para poder acessar de fora estes dados
    dados = [x for x in csv.DictReader(arquivo)]

# Como criar o nosso arquivo
with open('clientes2.csv', 'w') as arquivo:
    # Definindo qual vai ser a extrutura do nosso arquivo csv
    escreve = csv.writer(
        arquivo,
        delimiter=',',  # Qual é a nossa quebra
        quotechar='"',  # parece ser tipo algo de escape
        # Coloca aspas nos valores ou seja: "luiz", "otavio","miranha", fica mais seguro para trabalhar
        quoting=csv.QUOTE_ALL
    )

    """
    Somente teste para ver como poderia pegar os values de um dict_values
    print(dados[0].keys())
    d = list(dados[0].values())
    print(d[0])
    for v in d:
        print(v)
    """

    """
    Forma que o professor passou
    escreve.writerow([
        chaves[0], chaves[1], chaves[2], chaves[3]
    ])

    for dado in dados:
        # print(dado['Nome'], dado['Sobrenome'])
        escreve.writerow([
            dado['Nome'], dado['Sobrenome'], dado['E-mail'], dado['Telefone']
        ])
"""
    """
        Forma dinamica para montar o csv, util se o DB devolve json e precisamos montar um csv.
    """
    # Preenche cabeçalho
    escreve.writerow(
        list(dados[0].keys())
    )
    # Preenche dados
    for indx, dado in enumerate(dados):
        escreve.writerow(
            list(dados[indx].values())
        )

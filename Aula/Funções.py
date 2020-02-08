#-*- coding: utf-8 -*-

# produtos = []

# #função sempre inicia com 'def'

# def cadastraProduto(produto:
#     global produtos
#     produtos.append(produto)
 

# cadastraProduto('Batata')
# print(produtos)

# def listarProdutos():
#     global produtos
#     print(produtos)

# def deletarProdutos(produto):
#     global produtos
#     produtos.remove(produto)

#crie funções que receba x e y e retorne a soma e subtração


# n1 = int(input('Digite o primeiro valor: '))
# n2 = int(input('Digite o segundo valor: '))

# def soma(x, y):

#     return x + y

# def sub(x, y):

#     return x - y

# tsoma = soma(n1, n2)
# tsub = sub(n1, n2)

# print(f'a soma dos numeros é: {tsoma}')
# print(f'a subtração dos numeros é: {tsub}')

#faça uma função que receba 2 valores como parametro e imprima o maior

# n1 = int(input('Digite o primeiro valor: '))
# n2 = int(input('Digite o segundo valor: '))

# def RetM (x, y):

#     if n1 > n2:
#         print(n1)
#     else:
#         print(n2)


# RetM(n1, n2)

#*args
# def maior (*valores):
#     print(max(valores))


# maior(1, 2, 3)

#Ordena numero

# def maior (*valores):
#     print(sorted(valores))


# maior(2, 1, 3)

# import requests

# def api (**valores):
#     req = requests.get(valores['URL'])
#     print(valores)
#     return req

# print(api(URL='http://xpto.com.br', code_status = 200, retorno = 'ok'))

# from functools import reduce
# soma = reduce((lambda x,y: x+y), [1,2,3,4,5,6,7,8,9])
# print(soma)


class Passaro():
    def __init__(self):
        self.asas = 2
        self.bico = True
        self.pena = True
    def voar(self):
        print('voando...')
    def pousar(self):
        print('pousando...')
    def dormir(self):
        print('dormindo')

sabiá = Passaro()

sabiá.voar()
sabiá.voar()
sabiá.dormir()
print(sabiá.dormir)
    
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


n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

def soma(x, y):

    return x + y

def sub(x, y):

    return x - y

tsoma = soma(n1, n2)
tsub = sub(n1, n2)

print(f'a soma dos numeros é {tsoma}')
print(f'a subtração dos numeros é {tsub}')
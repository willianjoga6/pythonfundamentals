# faça um programa que receba 4 notas de alunos
# some e divida por 4

# n1 = int(input('Digite a primeira nota: '))
# n2 = int(input('Digite a segunda nota: '))
# n3 = int(input('Digite a terceira nota: '))
# n4 = int(input('Digite a quarta nota: '))


# nota_final = (n1 + n2 + n3 + n4) / 4

# print(nota_final)

lista = ['Corinthians', [1, 2, 3, 4, 5], 'Palmeiras', 'Sao Paulo', [10, 11, 12, 13, 14], 'Flamengo', 'Vasco']

# # print 3, 13, vasco
# print(lista[1][2], lista[4][3], lista[6])
# # print 4, Sao Paulo, 14
# print(lista[1][3], lista[3], lista[4][4])
# # print Corinthians, 2, 10, 14
# print(lista[0], lista[1][1], lista[4][0], lista[4][4])

# print(lista.index('Vasco'))

lista.append('Bragantino')
lista.insert(1,'Sport')
lista.remove('Vasco')
lista.pop(0)

print(lista)

list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.sort()
print ("list now : ", list1)

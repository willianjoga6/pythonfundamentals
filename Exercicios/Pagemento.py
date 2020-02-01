#-*- coding: utf-8 -*-



##Entrada de dados
valorhora = float(input('Digite o valor da hora: '))
quantidadehrs = float(input('Digite a quantidade de horas trabalhadas: '))

##Salário Bruto
salariobruto = (valorhora * quantidadehrs)

##Variaveis
salario1 = (1900)
salario2 = (2800)
salario3 = (3700)
salario4 = (4600)
ir = float(0)
sindicato = float(0)
fgts = float(0)
salarioliquido = float(0)
totaldesconto = float(0)


##Testa qual será o desconto do salário
if salariobruto > salario4:
    ir = (salariobruto * 0.27)
elif salariobruto > salario3:
    ir =(salariobruto * 0.22)
elif salariobruto > salario2:
    ir = (salariobruto * 0.15)
elif salariobruto > salario1:
    ir = (salariobruto * 0.07)
else:
    ir = 0

##Encontra desconto
sindicato = (salariobruto * 0.03)
fgts = (salariobruto * 0.11)
totaldesconto = (sindicato + ir)
salarioliquido = (salariobruto - totaldesconto)

##Imprime Na tela valores
print (f'O salário bruto é: {salariobruto}\n')
print(f'O valor de desconto de IR é: {ir}\n')
print(f'O valor de desconto de sindicato é: {sindicato}\n')
print(f'O valor de desconto de FGTS é: {fgts}\n')
print(f'O total de desconto é: {totaldesconto}\n')
print(f'O salário liquído é: {salarioliquido}\n')



#-*- coding: utf-8 -*-

# class Carro():
#     def __init__(self):
#         rodas = 4
#         motor = True
#     def ligar(self):
#         print('ligando...')

# palio = Carro()
# palio.ligar()

class Servidor():
    def __init__(self, servico, disco, processador, memoria):
        self.servico = servico
        self.disco = disco
        self.processador = processador
        self.memoria = memoria

    def addMemoria(self, am):
        self.memoria += am

    def addArmazenamento(self, aa):
        self.disco += aa

    def mudaServico(self, ms):
        self.servico = ms

servidorWeb = Servidor('Nginx', 250, 'i7 9Geração', 16)
am = int(input('Digite a quantidade de momória a Add: '))
servidorWeb.addMemoria(am)

aa = int(input('Digite a quantidade de armazenamento a Add: '))
servidorWeb.addArmazenamento(aa)

ms = input('Digite o serviço: ')
servidorWeb.mudaServico(ms)

print(servidorWeb.memoria)
print(servidorWeb.disco)
print(servidorWeb.servico)

# # # #!/usr/bin/python3
# # # #
# # # #
# # # #

# # # # Tipos de Dados
# # # # Inteiro
# # # # 1, 2, 3(Numeros não quebrados)

# # # #Float
# # # #1.2, 1.3 (Numeros Quebrados)

# # # # String
# # # # Texto entre ''

# # # #Bool
# # # #True
# # # #False

# # # # Comentarios = #

# # # # Variaveis
# # # # Variaveis são alocações de valores de "tipos de Dados"
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #

# # # #Entrada de dados
# # # #input soh recebe string
# # # # usuario = input('DIGITE SEU NOME: ')
# # # #
# # # #Para converter input para inteiro, usa int(imput(''))
# # # #Para converter input para string, usa str(imput(''))
# # # #Para converter input para boleano, usa bool(imput(''))
# # # #Para converter input para float, usa float(imput(''))


# # # #Saida de Dados
# # # # print(usuario)

# # # #função
# # # # nome = input('Digite seu nome: ')
# # # # sobrenome = input('Digite o seu sobrenome: ')
# # # # #Usar f e {}
# # # # print(f'O nome é {nome} e o sobrenome é {sobrenome}')

# # # #para acessar um metodo se usa o .(ponto)

# # # # palavra = 'nome'
# # # # print(palavra.upper())
# # # # palavra.re

# # # # #Comparação

# # # # var1 = 10
# # # # var2 = 50

# # # # print(var1 == var2)

# # # #Lista sempre usa [] e as colunas começam contar no zero

# # lista = ['abacaxi', 503, 30.3, 'cachorro', {'chave': 1}]
# # print(lista[-1])


# ling_favorita = {'Joao': 'Java', 'Daniel': 'Python', 'Will':'SQL'}
# print(ling_favorita ['Will'])

# time_favorito = {'Joao': 'Corinthians', 'Rafael': 'Vasco', 'Camila': 'Palmeiras'}

# print(time_favorito['Camila'])

# time_favorito['Rafael'] = 'Flamengo'
# time_favorito.update({'Camila':'PALMEIRAS'})

# print(time_favorito)

cpf = input('Digite o CPF: ')

cliente =   {'cliente' :    {'cl001':   {   'nome':'Rafael da Silva', 
                                            'idade': 25, 
                                            'telefone':'011976030848'
                                        },
                            'cl002':   {   'nome':'Willian', 
                                            'idade': 28, 
                                            'telefone':'011976030848'
                                        },
                            'cl003':   {   'nome':'Sergio', 
                                            'idade': 28, 
                                            'telefone':'011976030848'
                                        },
                            'cl004':   {   'nome':'Pedro', 
                                            'idade': 28, 
                                            'telefone':'011976030848'
                                        }
                                        
                            }
            }

print   (   cliente['cliente' ][cpf]['nome'], 
            cliente['cliente' ][cpf]['idade']
        )
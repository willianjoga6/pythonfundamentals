#-*- coding: utf-8 -*-

dado =  {
            'estado':   {
                            'sp':   {
                                        'nome': 'São Paulo',
                                        'municipio': 92,
                                        'população': 16.72

                                    },
                            'rj':   {
                                        'nome': 'Rio de Janeiro',
                                        'municipio': 645,
                                        'população': 44.04

                                    },
                            'mg':   {
                                        'nome': 'Minas Gerais',
                                        'municipio': 31,
                                        'população': 20.87

                                    },

                        }

        }

# Imprima as seguintes informações

# 1- Nome dos estado
# 2- Nome dos estados e sua população em milhoes
# 3- Nome dos estados e quantidade de municipios

# for i in dado['estado'].keys():
#     print(f"Nome dos Estados: {dado['estado'][i]['nome']}")
# print('\n=========================\n')
# for i in dado['estado'].keys():
#     print(f"Nome dos Estados: {dado['estado'][i]['nome']}", f"População: {dado['estado'][i]['população']}",'Milhões')
# print('\n=========================\n')
# for i in dado['estado'].keys():
#     print(f"Nome dos Estados: {dado['estado'][i]['nome']}", f"População: {dado['estado'][i]['municipio']}")
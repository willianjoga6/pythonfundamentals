# import psycopg2

# try:
#     con = psycopg2.connect("host=localhost dbname=projeto user=admin password = 4linux")

#     cur = con.cursor()
#     cur.execute("insert into script(nome, conteudo) values ('testetry.py', \
#            'teste try')")

#     con.commit()

# except Exception as e:
#     print('Erro: {}'.format(e))
#     print('Fszendo rollback')
#     con.rollback()

# finally:
#     print("finalizando conexão")
#     con.close()


#mong

from pymongo import MongoClient

client = MongoClient('localhost')
db = client['dexterops']

def inserir_dados():
    try:
        db.fila.insert({"_id":1, "empresa":"4linux","cursos":[{"nome":"python fundamentals",
                                                                "carga horaria":40},
                                                                {"nome":"linunx",
                                                                "carga horaria": 40}]})
    except Exception as e:
        print('Erro:{}'.format(e))

# inserir_dados()

def buscar_dados():
    for r in db.fila.find():
        print('empresa: {}'.format(r['empresa']))
        for c in r['cursos']:
            print(20*'=')
            print('nome: {} \n carga horaria: {}'. format(c['nome'], c['carga horaria']))

# buscar_dados()

# def adicionar_sub():
#     db.fila.update({"_id":1}, {"$addToSet":{'instrutores':{'nome':'Mariana',
#                                                             'email':'teste@teste.com.br'}}})
# adicionar_sub()

# def update_sub():
#     db.fila.update({"_id": 1, "instrutores.nome": "Mariana"},
#                    {"$set": {"instrutores.$.nome": "Marcia"}})
# update_sub()

# def update_email():
#     db.fila.update({"_id": 1, "instrutores.email": "teste@teste.com.br"},
#                    {"$set": {"instrutores.$.email": "teste2@teste2.com.br"}})
# update_email()
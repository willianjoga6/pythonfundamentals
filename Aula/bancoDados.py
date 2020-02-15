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

def iserir_dados():
    try:
        db.fila.insert({"_id":1, "empresa":"4linux","cursos":[{"nome":"python fundamentals",
                                                                "carga horaria":40},
                                                                {"nome":"linunx",
                                                                "carga horaria": 40}]})
    except Exception as e:
        print('Erro:{}'.format(e))

iserir_dados()
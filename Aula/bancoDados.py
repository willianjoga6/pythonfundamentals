import psycopg2

try:
    con = psycopg2.connect("host=localhost dbname=projeto user=admin password = 4linux")

    cur = con.cursor()
    cur.execute("insert into script(nome, conteudo) values ('testetry.py', \
           'teste try')")

    con.commit()

except Exception as e:
    print('Erro: {}'.format(e))
    print('Fszendo rollback')
    con.rollback()

finally:
    print("finalizando conexão")
    con.close()
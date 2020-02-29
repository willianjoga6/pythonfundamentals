from sqlalchemy import update
from core import user_table, engine

con = engine.connect()

def atualiza_nome(na, nn):
    atualizar = update(user_table).where(user_table.c.nome == na)
    atualizar = atualizar.values(nome=nn)
    result = con.execute(atualizar)
    print(result.rowcount)

atualiza_nome( '|Serjao', 'Willian')

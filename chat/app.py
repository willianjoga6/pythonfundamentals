import modules.banco as banco
import threading

if __name__ == "__main__":
    db = banco.BancoMongo()
    user = input("Nome: ")
    try:
        f = threading.Thread(target=db.visualizar)
        f.start()
    except Exception as e:
        print('Falha ao criar thread: {}'.format(e))
    while f.is_alive:
        mens = input()
        db.cadastrar(user, mens)
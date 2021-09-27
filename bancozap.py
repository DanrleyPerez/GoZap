import sqlite3
from sqlite3 import Error


def conexao(banco):
    caminho = "C:\\Users\\danrl\\PycharmProjects\\pythonProject\\GoZap\\database\\"+banco+".db"

    try:
        con = sqlite3.connect(caminho)
        return con
    except Error as er:
        print(er)


def criacao(connection, comando_sql):
    try:
        c = connection.cursor()
        c.execute(comando_sql)
        print("criado com sucesso!")

    except Error as er:
        print(er)





from GoZap.bancozap import conexao
from sqlite3 import Error


def retorna_opcoes(conexao, comando_sql):
    c = conexao.cursor()
    c.execute(comando_sql)
    lista = c.fetchall()
    return lista


def edita_opcoes(conex, comando_sql):
    try:
        c = conex.cursor()
        c.execute(comando_sql)
        conex.commit()
    except Error as er:
        print(er)


def adicao_valores(banco, a, b):
    try:
        c = conexao(banco)
        edita_opcoes(c, """INSERT INTO MACControle(Nome, MAC) VALUES('"""+a+"""', '"""+b+"""')""")
    except Error as er:
        print(er, "ja existe a tabela : ")
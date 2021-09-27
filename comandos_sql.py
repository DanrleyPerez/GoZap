
#criacao banco de dados das conversas.

lista_de_comandos = { 'sqla' : """ CREATE TABLE A 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1)); """
,
'sqlb1' : """ CREATE TABLE AB1 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1)); """
,
'sqlb2' : """ CREATE TABLE AB2 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1)); """
,
'sqlb3' : """ CREATE TABLE AB3 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1)); """
,
'sqlb4' : """ CREATE TABLE AB4 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1)); """
,
'sqlb5': """ CREATE TABLE AB5 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1)); """
,

'sqlb1c1' : """ CREATE TABLE AB1C1 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1));"""
,
'sqlb1c2': """ CREATE TABLE AB1C2
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1)); """
,
'sqlb1c3' : """ CREATE TABLE AB1C3 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1)); """
,
'sqlb1c4' : """ CREATE TABLE AB1C4 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1)); """
,
'sqlb1c5' : """ CREATE TABLE AB1C5 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1)); """
,
'sqlb2c1' : """ CREATE TABLE AB2C1 
        (Pergunta1 STRING(1),  Pergunta2 STRING(20), Pergunta3 STRING(20), Pergunta4 STRING(20), Pergunta5 STRING(20));"""
,
'sqlb2c2' : """ CREATE TABLE AB2C2
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1));"""
,
'sqlb2c3' : """ CREATE TABLE AB2C3 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1));"""
,
'sqlb2c4' : """ CREATE TABLE AB2C4 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1));"""
,
'sqlb2c5' : """ CREATE TABLE AB2C5 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1)); """
,
'sqlb3c1' : """ CREATE TABLE AB3C1 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1));"""
,
'sqlb3c2' : """ CREATE TABLE AB3C2
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1));"""
,
'sqlb3c3' : """ CREATE TABLE AB3C3 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1));"""
,
'sqlb3c4' : """ CREATE TABLE AB3C4 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1));"""
,
'sqlb3c5' : """ CREATE TABLE AB3C5 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1));"""
,
'sqlb4c1' : """ CREATE TABLE AB4C1 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1)); """
,
'sqlb4c2' : """ CREATE TABLE AB4C2
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1));"""
,
'sqlb4c3' : """ CREATE TABLE AB4C3 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1)); """
,
'sqlb4c4' : """ CREATE TABLE AB4C4 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1)); """
,
'sqlb4c5' : """ CREATE TABLE AB4C5 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1)); """
,
'sqlb5c1' : """ CREATE TABLE AB5C1 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1)); """
,
'sqlb5c2' : """ CREATE TABLE AB5C2
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1)); """
,
'sqlb5c3' : """ CREATE TABLE AB5C3 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1)); """
,
'sqlb5c4' : """ CREATE TABLE AB5C4 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1)); """
,
'sqlb5c5' : """ CREATE TABLE AB5C5 
        (Pergunta1 STRING(1),  Pergunta2 STRING(1), Pergunta3 STRING(1), Pergunta4 STRING(1), Pergunta5 STRING(1)); """
                      }


dados_padroes = """INSERT INTO"""


# pegar opcoes banco de dados

# opcoes da tabela A

capta_opcoes_tabela_A = """SELECT * from A"""

capta_opcoes_tabela_B1 = """SELECT * from AB1"""

capta_opcoes_tabela_B2 = """SELECT * from AB2"""

capta_opcoes_tabela_B3 = """SELECT * from AB3"""

capta_opcoes_tabela_B4 = """SELECT * from AB4"""

capta_opcoes_tabela_B1C1 = """SELECT * from AB1C1"""

capta_opcoes_tabela_B1C2 = """SELECT * from AB1C2"""

capta_opcoes_tabela_B1C3 = """SELECT * from AB1C3"""

capta_opcoes_tabela_B1C4 = """SELECT * from AB1C4"""

capta_opcoes_tabela_B1C5 = """SELECT * from AB1C5"""

capta_opcoes_tabela_B2C1 = """SELECT * from AB2C1"""

capta_opcoes_tabela_B2C2 = """SELECT * from AB2C2"""

capta_opcoes_tabela_B2C3 = """SELECT * from AB2C3"""

capta_opcoes_tabela_B2C4 = """SELECT * from AB2C4"""

capta_opcoes_tabela_B2C5 = """SELECT * from AB2C5"""

capta_opcoes_tabela_B3C1 = """SELECT * from AB3C1"""

capta_opcoes_tabela_B3C2 = """SELECT * from AB3C2"""

capta_opcoes_tabela_B3C3 = """SELECT * from AB3C3"""

capta_opcoes_tabela_B3C4 = """SELECT * from AB3C4"""

capta_opcoes_tabela_B3C5 = """SELECT * from AB3C5"""

capta_opcoes_tabela_B4C1 = """SELECT * from AB4C1"""

capta_opcoes_tabela_B4C2 = """SELECT * from AB4C2"""

capta_opcoes_tabela_B4C3 = """SELECT * from AB4C3"""

capta_opcoes_tabela_B4C4 = """SELECT * from AB4C4"""

capta_opcoes_tabela_B4C5 = """SELECT * from AB4C5"""

capta_opcoes_tabela_B5C1 = """SELECT * from AB5C1"""

capta_opcoes_tabela_B5C2 = """SELECT * from AB5C2"""

capta_opcoes_tabela_B5C3 = """SELECT * from AB5C3"""

capta_opcoes_tabela_B5C4 = """SELECT * from AB5C4"""

capta_opcoes_tabela_B5C5 = """SELECT * from AB5C5"""


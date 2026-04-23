import mariadb

conexao = mariadb.connect(
    host="localhost",
    user="root",
    password="",
    database="loja"
)

cursor = conexao.cursor()

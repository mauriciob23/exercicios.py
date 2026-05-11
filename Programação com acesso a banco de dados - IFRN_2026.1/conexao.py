import mariadb

conexao = mariadb.connect(
    host="localhost",
    user="root",
    password="",
    database="escola"   

)

cursor = conexao.cursor()

# cursor.commit()       (confirma os valores informados para gravar no banco)
# cursor.close()        (Feca a conexão)
# cursor.fetchall       (transfere os dados do cursor)
# cursor.rowcont        (conta os resultados encontrados - precisa de um 'for')

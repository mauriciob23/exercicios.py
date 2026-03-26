import mariadb

conexao = mariadb.connect(host="localhost",
                          user="root",
                          password="",
                          database="escola")

cursor = conexao.cursor()

#### LISTAGEM DE DADOS #########

cursor.execute("SELECT * FROM alunos")

for linha in cursor :
    print(linha)
    print("Codigo:", linha[0])
    print("Nome:", linha[1])
    print("Curso:", linha[2])
    print("Serie:", linha[3])
    print("------------------")
    
    
cursor.close()
conexao.close()

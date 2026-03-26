import mariadb

#################################################################
conexao = mariadb.connect(host="localhost",
                          user="root",
                          password="",
                          database="escola")

cursor = conexao.cursor()
#################################################################

print("====PESQUISA POR NOME====")
nome = input("Nome do aluno: ")
print("====================")

############################## COMANDOS ###########################
sql = f'''SELECT * FROM alunos WHERE nome LIKE '%{nome}%' '''
cursor.execute(sql)


######################## LISTAGEM DE DADOS #######################

for linha in cursor :
    # print(linha)
    print("Codigo:", linha[0])
    print("Nome:", linha[1])
    print("Curso:", linha[2])
    print("Serie:", linha[3])
    print("------------------")
    
    
cursor.close()
conexao.close()

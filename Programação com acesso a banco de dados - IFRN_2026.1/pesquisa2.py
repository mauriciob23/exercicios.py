import mariadb

#################################################################
conexao = mariadb.connect(host="localhost",
                          user="root",
                          password="",
                          database="escola")

cursor = conexao.cursor()
#################################################################

print("====PESQUISA POR NOME====")
nome = input("Pesquise por nome, curso ou serie: ")
print("==========================")

############################## COMANDOS ###########################
sql = f'''
        SELECT * FROM alunos WHERE nome LIKE '%{nome}%' 
        OR curso LIKE '%{nome}%'
        OR serie = '{nome}'
    '''
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

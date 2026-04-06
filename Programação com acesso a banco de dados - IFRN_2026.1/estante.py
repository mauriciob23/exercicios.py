import mariadb

conexao = mariadb.connect(
    host="localhost", user="root", password="", database="estante"
)

cursor = conexao.cursor()


def cadastrar():
    print("###### CADASTRAR LIVRO ######")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    sql = f""" INSERT INTO livros VALUES (null, '{titulo}', '{autor}'); """
    cursor.execute(sql)
    conexao.commit()
    print("INSERIDO COM SUCESSO!\n")


def pesquisar():
    print("##### PESQUISAR LIVRO #####")
    pesq = input("Digite a pesquisa: ")
    sql = f""" SELECT * FROM livros WHERE autor LIKE '%{pesq}%' OR titulo LIKE '%{pesq}%' """
    cursor.execute(sql)

    if cursor.rowcount == 0:
        print("NÃO ENCONTRADO\n")

    else:
        for linha in cursor:
            print("Código: ", linha[0])
            print("Titulo: ", linha[1])
            print("Autor: ", linha[2], "\n")


def delete():
    print("###### EXCLUIR LIVRO ######")
    op = input("Código do livro: ")
    sql = "SELECT * FROM livros WHERE codigo = " + op
    cursor.execute(sql)

    if cursor.rowcount == 0:
        print("NÃO ENCONTRADO!\n")

    else:
        for linha in cursor:
            print(linha)

        resp = input("Excluir? (s/n)").lower
        if resp == "s":
            cursor.execute("DELETE FROM livros WHERE codigo = " + op)
            conexao.commit()
            print("EXCLUÍDO COM SUCESSO!")

def alterar():
    print("#### Alterar Dados #####")
    cod = input("Digite o codigo do livro: ")
    sql1 = "SELECT * FROM livros WHERE codigo = " + cod
    cursor.execute(sql1)

    if cursor.rowcount == 0:
        print("Não encontrado!")

    else:
        for linha in cursor:
            print(linha)

        resp = input("Alterar? (s/n)")
        if resp == "s":
            coluna = input("Qual coluna? (titulo/autor)\n")
            info = input("Nova informação: \n")
            sql = f'''UPDATE livros
                     SET {coluna} = '{info}'
                     WHERE codigo = {cod}
                '''
        cursor.execute(sql)
        conexao.commit()
        print("ALTERADO COM SUCESSO!\n")


while True:
    print("##### SISTEMA ESTANTE VIRTUAL #####")
    op = int(input("1 - Cadastrar\n2 - Pesquisar\n3 - Deletar\n4 - Alterar\n5 - Sair\nOpção? "))
    if op == 1:
        cadastrar()

    elif op == 2:
        pesquisar()

    elif op == 3:
        delete()

    elif op == 4:
        alterar()

    elif op == 5:
        break

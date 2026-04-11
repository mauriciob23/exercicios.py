# Disciplina: Programação com acesso a banco de dados - IFRN - 2026.1
# Discentes: Gizelly Patrícia Martins Ferreira
#            Mauricio Jose Barros de Oliveira

import mariadb

conexao = mariadb.connect(
    host="127.0.0.1",
    user="root",
    password="",
    port=3306,
    database="cadastro_de_veiculos",
)


cursor = conexao.cursor()


def listar():
    sql_print = "SELECT * FROM veiculos"
    cursor.execute(sql_print)

    tabela_dos_cadastrados = cursor.fetchall()

    if not tabela_dos_cadastrados:
        print("\n*Nenhum veículo cadastrado no momento!*\n")

    else:
        for linhas in tabela_dos_cadastrados:
            print(f"\n{linhas}\n")


def cadastrar():
    print("========== CADASTRAR VEÍCULO ==========")
    tipo = input(
        "Tipo do veiculo (Carro | Moto | Bicicleta | Outros...) *OBRIGATÓRIO*:\n"
    )
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    cor = input("Cor: ")
    combustivel = input("Tipo de combustivel: ")
    placa = input("Placa: ")
    ano = input("Ano: ")

    sql = f""" INSERT INTO veiculos VALUES (null, '{tipo}', '{marca}', '{modelo}', '{cor}',  '{combustivel}', '{placa}', '{ano}');"""
    cursor.execute(sql)
    conexao.commit()
    print("INSERIDO COM SUCESSO!\n")


def pesquisar():
    print("========== PESQUISAR VEÍCULO ==========")
    pesq = input("Digite a pesquisa: ")
    sql = f""" SELECT * FROM veiculos WHERE 
                tipo LIKE '%{pesq}%' 
                OR marca LIKE '%{pesq}%' 
                OR modelo LIKE '%{pesq}%' 
                OR cor LIKE '%{pesq}%' 
                OR combustivel LIKE '%{pesq}%' 
                OR placa LIKE '%{pesq}%' 
                OR ano LIKE '%{pesq}%'"""
    cursor.execute(sql)

    if cursor.rowcount == 0:
        print("NÃO ENCONTRADO\n")

    else:
        for linha in cursor:
            print("Código: ", linha[0])
            print("Tipo: ", linha[1])
            print("Marca: ", linha[2])
            print("Modelo: ", linha[3])
            print("Cor: ", linha[4])
            print("Combustivel: ", linha[5])
            print("Placa: ", linha[6])
            print("Ano: ", linha[7])


def alterar():
    print("========== ALTERAR CADASTRO DE VEÍCULO ==========")
    cod_veic = input("Selecione o código do veiculo para alterar: ")
    sql = f"SELECT * FROM veiculos  WHERE id = {cod_veic}"
    cursor.execute(sql)

    if cursor.rowcount == 0:
        print("Veículo não encontrado!")

    else:
        for selecao in cursor:
            print(f"\nVeículo selecionado:\n{selecao}")

        resp = input("Alterar? (s/n) ").lower()
        if resp == "s":
            coluna = input(
                "Qual infomação(coluna) deseja alterar?\n(tipo | marca | modelo | cor | combustivel | placa | ano)\n"
            )
            info = input("Nova informação: \n")
            sql1 = f"""
                UPDATE veiculos  
                SET {coluna} = '{info}'
                WHERE id = {cod_veic}
                """
            
            cursor.execute(sql1)
            conexao.commit()
            print("\n**ALTERADO COM SUCESSO**\n")


def excluir():
    print("========== EXCLUIR VEÍCULO ==========")
    selec = input("Digite o código (id) do veículo a ser excluído: ")
    sql = f"SELECT * FROM veiculos WHERE id = {selec}"
    cursor.execute(sql)

    if cursor.rowcount == 0:
        print("Veículo não encontrado!")

    else:
        for linha in cursor:
            print(linha)

        resposta = input("Deseja realmente excluir? (s/n)").lower()

        if resposta == "s":
            sql = f"""
                DELETE FROM veiculos
                WHERE id = {selec}
                """
                
            cursor.execute(sql)
            conexao.commit()
            print("\n**EXCLUÍDO COM SUCESSO!!**\n")


######### MENU #########
while True:
    print("========== CATÁLOGO DE VEÍCULOS ==========")
    op = int(
        input(
            """Escolha uma opção\n1 - Listar cadastrados\n2 - Cadastrar\n3 - Pesquisar\n4 - Alterar\n5 - Excluir\n6 - Sair\nOpção: """
        )
    )

    if op == 1:
        listar()

    elif op == 2:
        cadastrar()

    elif op == 3:
        pesquisar()

    elif op == 4:
        alterar()

    elif op == 5:
        excluir()

    elif op == 6:
        print("Saindo...")
        cursor.close()
        conexao.close()
        break


"""
CÓDIGOS DO MYSQL/MARIADB:

CREATE DATABASE cadastro_de_veiculos;

CREATE TABLE veiculos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    cor VARCHAR(50),
    combustivel VARCHAR(50),
    placa VARCHAR(50),
    ano VARCHAR(10)

);

"""

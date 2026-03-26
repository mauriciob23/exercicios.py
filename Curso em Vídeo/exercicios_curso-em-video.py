##########EXERCICIO 1 - Crie um programa que escreva "Olá mundo"
#METODO 1:
'''print("Olá Mundo")'''
#METODO 2:
'''msg = "Olá Mundo"
print(msg)'''

##########EXERCICIO 2 - Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
'''nome = str(input("Digite seu nome: "))
print(f"Seja bem vindo {nome}")'''

##########EXERCICIO 3 - Crie um programa que leia dois números e mostre a soma entre eles.
'''print("---Vamos somar dois numeros---")
n1 = int(input("Primeiro valor: "))
n2 = int(input('Segundo valor: '))

soma = n1 + n2

print(f'A soma de {n1}+{n2} é igual a {soma}')'''

##########EXERCICIO 4 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
'''algo = input("Digite algo: ")

print("O tipo primitivo desse valor é: ", type(algo)) #type: indica o tipo primitivo do que foi digitado
print("Só tem espaços?", algo.isspace()) #isspace: indica se o que foi digitado é somente espaço
print("É um numero? ", algo.isnumeric()) #isumeric: indica se é numero
print("É alfabetico? ", algo.isalpha()) #isalpha: incica se é somente alfabetico (letras)
print("é alfanumerico? ", algo.isalnum()) #isalnum: indica se é letras e numeros
print("Está em maiúsculo? ", algo.isupper()) #isupper: indica se está em maiusculo
print("Está em minúsulo? ", algo.islower()) #indica se está em minusculo 
print("Está captalizada? ", algo.istitle()) #istitle: indica se esta em maiusculo e minusculo (captalizado, para o python)'''

import math #importando a biblioteca math para utilizar algumas de suas operações aritimeticas nos proximos exercicios

##########Exercício 5 – Antecessor e Sucessor de um numero;
'''print("\t\tMostrando Sucessor e Antecessor:")

num = int(input("Selecione um valor: "))

print(f"Numero antecessor: {num - 1}\nNumero Sucessor: {num +1}")
print("Terminou!")'''

##########Exercício 6 – Dobro, Triplo, Raiz Quadrada de um numero;

'''print("\t\tMostrando Dobro, triplo e raiz quadrada")

num = int(input("Selecione um valor: "))

print(f"Dobro: {num*2}\nTriplo: {num*3}\nRaiz: {math.sqrt(num):.2f}" ) #a raiz também pode ser calculado como: num ** (1/2) e/ou pow(num, (1/2))'''

##########Exercício 7 – Média Aritmética
'''print("\t\tMédia Aritmética\n")

nota1 = float(input("Digite sua 1ª nota: "))
nota2 = float(input("Digite sua 2ª nota: "))
nota3 = float(input("Digite sua 3ª nota: "))
nota4 = float(input("Digite sua 4ª nota: "))

media = (nota1 + nota2 + nota3 + nota4)/4
print(f"Sua media foi = {media:.2f}")
print("Terminou!")'''

##########Exercício 8 – Conversor de Medidas (mm/cm/m/km)
#print("\t\tConversor de Medidas\n") #km  hm  dam  m  dm  cm  mm
'''print("\t\tConversor de medidas\n")

medida = input("Selecione a medida na qual deseja converter: mm/cm/m/km -> ").lower()
valor = float(input("Agora digite o valor que gostaria de converter:\n-> "))
if medida == 'cm' :
    print(f"\tConvertento...\nMilímetro: {valor * 10}mm\nMetros: {valor/100}m\nQuilometros: {valor/100000}km")

elif medida == 'mm' :
    print(f"\tConvertento...\nCentimetro: {valor/10}cm\nMetros: {valor/1000}m\nQuilometros: {valor/1e+6}km")
    
elif medida == 'km' :
    print(f"\tConvertento...\nMilímetro: {valor * 1e+6}mm\nCentimetros: {valor*100000}cm\nMetros: \t{valor*1000}m")
     
elif medida == 'm' :
    print(f"\tConvertento...\nMilímetro: {valor * 1000}mm\nCentimetros: {valor*100}cm\nQuilometros: {valor/1000}km")
     
else :
    print("Medida invalida, tente novamente!")

print("\n\tTERMINOU!")'''

##########Exercício 9 – Tabuada
'''print("\t\tTabuada")
num = int(input("Entre com um valor qualquer: "))
print("Imprimindo sua tabuada...")
tabuada = 1
print("-"*12)#o operando desta forma, multiplica a quantidade de caractere
while tabuada <= 10 :
    print(f"{num} x {tabuada:2} = {num * tabuada}") # o operador ":2" indica que cada numero tem 2 digitos. Isto é feito para organizar a saida
    tabuada += 1
    
print("-"*12) #o operando desta forma, multiplica a quantidade de caractere
print("Terminou")'''
##########Exercício 10 – Conversor de Moedas
'''print("\t\tConversor de Moedas\n")

valor = float(input("Entre com um valor em reais:\nR$ "))

dolar = valor/5.59 
euro = valor/6.37
peso = valor*212.44  

print("Convertendo...")
print(f"Dolar - US$: {dolar:.2f}\nEuro - €:{euro:.2f}\nPeso - ARS$: {peso:.2f}")'''

##########Exercício 11 – Pintando Parede - calcule a area da parede e a quantidade de tinta para pinta-la
#1L de tinta -> pinta 2m². Peça do usuario a altura e largura da parede
'''print("\t\tPintando Paredes\n")
altura = float(input("Entre com o valor da altura da parede: "))
largura = float(input("Digite o valor da largura da parede: "))
area = altura * largura
tinta = 2
tinta_total = area/tinta

print(f"Sua parede tem {area}m²")
print(f"Você irá precisar de {tinta_total} litros de tinta para pintar sua parede completa")

print("TERMINOU!")'''


##########Exercício 12 – Calculando Descontos
'''print("\t\tCalculando descontos\n")
#desconto de 5%
valor = float(input("Qual o valor do produto que deseja adquirir?\n -> "))
desconto = (valor*0.05) #(valor * 5/100) -> outra maneira de fazer
desc_aplic = valor - desconto #desconto (valor * 5/100) -> outra maneira de fazer

print(f"Aplicando desconto de 5% (R${desconto:.2f})\nValor com desconto: R${desc_aplic:.2f}")
print("TERMINOU")'''


##########Exercício 13 – Reajuste Salarial
'''print("\t\tReajuste Salarial\n")
#reajuste de 15%
salario = float(input("Digite o valor de seu salario: R$"))
reajuste = salario*0.15
salario_ajustado = salario + reajuste

print(f"Aplicando 15% de ajuste salarial (R$ {reajuste:.2f})\nSeu novo salario é de: R$ {salario_ajustado:.2f}")
print("TERMINOU!")'''


##########Exercício 14 – Conversor de Temperaturas
'''print("\t\tConversor de Temperaturas\n")
medida = input("Qual medida de temperatura você deseja converter? (Selecione a inicial da medida)\n(F)ahrenheiit\n(C)elsius\n(K)elvin\n-> ").lower()
valor = float(input("Agora entre com o valor no qual deseja converter: "))

if medida == 'c' :
     print(f"\tConvertento...\nFahrenheit: {(valor*9/5)+32}ºF\nKelvin: {valor+273.15}ºK\n")
    
elif medida == 'f' :
    print(f"\tConvertento...\nCelsius: {(valor-32)*5/9}ºC\nKelvin: {(valor-32)*5/9 + 273.15}ºK\n")    

elif medida == 'k' :
    print(f"\tConvertento...\nCelsius: {valor - 273.15}ºC\nFahrenheit: {(valor-273.15)*9/5 + 32}ºF\n")
    
else :
    print("Medida invalida, tente novamente!")
    
print("Terminou!")'''


##########Exercício 15 – Aluguel de Carros
#Escreva um programa que pergunte a quantidade de KM percurrido
#por um carro alugado e a quantidade de dias passou com ele
#Calcule o preço a pagar, sabendo que o carro custa:
# R$ 60 por dia e R$ 0.15 por KM rodado
'''print("\t\tAluguel de carros\n")
dias = int(input("Quantos dias você ficou com o carro? "))
km = float(input("Quantos quilometros você percorreu? "))
valor_dias = dias * 60
valor_km = km * 0.15
valor_total = valor_dias + valor_km

print(f"O valor do aluguel foi de R${valor_total:.2f}\nTERMINOU!")'''

##########Exercicio 16 - Quebrando um número
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#METODO 1:
'''numero = float(input("Digite um valor: "))
parte_inteira = int(numero)
parte_decimal = numero - parte_inteira

print(f"O valor digirado foi {numero} e sua parte inteira é {parte_inteira} e a parte decimal é {parte_decimal:.2}")'''

#METODO 2:
'''num = float(input("Digite um com numero com casa decimal: "))
print(f"O valor digitado foi {num} e sua porção inteira é {math.trunc(num)}") #O metodo 'trunc' divide a parte inteira do numero decimal'''

#METODO 3
'''from math import trunc #importando apenas o metodo trunc da biblioteca, não é preciso chamar a biblioteca antes do metodo como no "METODO 2"
num = float(input("Digite um com numero com casa decimal: "))
print(f"O valor digitado foi {num} e sua porção inteira é {trunc(num)}")'''

##########EXERCICIO 17 - Catetos e Hipotenusa
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.
#METODO 1:
'''oposto = float(input("Comprimento do cateto oposto: "))
adjacente = float(input("Comprimento do cateto adjacente: "))

adicao_dos_catetos = oposto + adjacente
subtracao_dos_catetos = oposto - adjacente 
muntiplicacao_dos_catetos = adicao_dos_catetos * subtracao_dos_catetos

hipotenusa = math.sqrt(muntiplicacao_dos_catetos)

print(f"A hiponenusa vai medir {hipotenusa:.2}")''' #o calculo desse metodo está calculando errado

#METODO 2:
'''from math import hypot #importanto apenas o metodo 'hypot'
oposto = float(input("Comprimento do cateto oposto: "))
adj = float(input("Comprimento do cateto adjacente: "))
hipotenusa = hypot(oposto, adj)
print(f"O comprimento da hipotenusa é: {hipotenusa:.2}")'''

#METODO 3: 
'''from math import sqrt
oposto = float(input("Comprimento do cateto oposto: "))
adjacente = float(input("Comprimento do cateto adjacente: "))
quadrado_oposto = oposto**2
quadrado_adjacente = adjacente**2
soma_dos_quadrados = quadrado_oposto + quadrado_adjacente
hipotenusa = sqrt(soma_dos_quadrados)

print(f"O valor da hipotenusa é {hipotenusa:.2}")'''

#########Exercício 18 – Seno, Cosseno e Tangente
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do:
#Seno, Cosseno e Tangente desse ângulo.
#observação: para utilizar as funções de 'sin', 'cos' e 'tan' é necessario converter a medida para radianos
'''from math import radians, sin, cos, tan #importando apenas os metodos "radians", "sin", "cos" e "tan" para que não seja necessário sempre chamar os metodos ulizando "math.radians"...

angulo = float(input("Digite o ângulo desejavel: "))

radianos = radians(angulo) #converte para  radianos utilizando o metódo "math.radians" para que os proximos modulos consiga identifica-lo

seno = sin(radianos)
cosseno = cos(radianos)
tangente = tan(radianos)

print(f"O Seno do ângulo digitado é: {seno:.2}")
print(f'O Cosseno do ângulo digitado é {cosseno:.2}')
print(f"A Tangente do ângulo é {tangente:.2}")
print("TERMINOU")'''

#########EXERCICIO 19 - Sorteando um item na lista
#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''import random  
nome1 = str(input("Primeiro nome: "))
nome2 = str(input("Sgundo nome: "))
nome3 = str(input("Terceiro nome: "))
nome4 = str(input("Quarto nome: "))
lista = [nome1, nome2, nome3, nome4]

escolha = random.choice(lista) #o metodo 'choice' da biblioteca 'random' escolhe um valor aleatoriamente

print(f"O aluno escolhido foi: {escolha}")'''

#########EXERCICIO 20 - Sorteando uma ordem na lista
#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''import random'''
#METODO 1:
'''n1 = str(input("Primeiro nome: "))
n2 = str(input("Segundo nome: "))
n3 = str(input("Terceiro nome: "))
n4 = str(input("Quarto nome: "))
lista = [n1, n2, n3, n4]

ordem = random.sample(lista, k =4) #o metodo sample embaralha a lista utiliza o parametro 'k' para a quantidade dos elementos que ira ser sorteado, neste caso, o tamanho da lista(com 4 nomes)

print(f"A ordem de apresentação será:\n{ordem}")'''
#METODO 2:
'''n1 = str(input("Primeiro nome: "))
n2 = str(input("Segundo nome: "))
n3 = str(input("Terceiro nome: "))
n4 = str(input("Quarto nome: "))
lista = [n1, n2, n3, n4]
random.shuffle(lista) #o metodo shuffle sorteia aleatoriamente os nomes da lista
print(f"A ordem de apresentação será:\n{lista}")'''
#########EXERCICIO 21 – Tocando um MP3
#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

'''import pygame #bliblioteca de jogos do python que é necessaria instalação: pip install pygame — utilizado para tocar o audio
pygame.init() #iniciando a biblioteca pygame
pygame.mixer.music.load("sons/ex21.mp3") #para carregar a musica
pygame.mixer.music.play() #para tocar a musica
input() #este parametro é importante para a nova versão do python que permite a musica ser carregada
pygame.event.wait()#aguarda a musica encerrar para finalizar o programa'''

########EXERCICIO 22 - (??)

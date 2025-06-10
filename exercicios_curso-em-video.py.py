import math #importando a biblioteca math para utilizar algumas de suas operações aritimeticas
#Exercício 5 – Antecessor e Sucessor de um numero;
'''print("\t\tMostrando Sucessor e Antecessor:")

num = int(input("Selecione um valor: "))

print(f"Numero antecessor: {num - 1}\nNumero Sucessor: {num +1}")
print("Terminou!")'''

#Exercício 6 – Dobro, Triplo, Raiz Quadrada de um numero;

'''print("\t\tMostrando Dobro, triplo e raiz quadrada")

num = int(input("Selecione um valor: "))

print(f"Dobro: {num*2}\nTriplo: {num*3}\nRaiz: {math.sqrt(num):.2f}" ) #a raiz também pode ser calculado como: num ** (1/2) e/ou pow(num, (1/2))'''

#Exercício 7 – Média Aritmética
'''print("\t\tMédia Aritmética\n")

nota1 = float(input("Digite sua 1ª nota: "))
nota2 = float(input("Digite sua 2ª nota: "))
nota3 = float(input("Digite sua 3ª nota: "))
nota4 = float(input("Digite sua 4ª nota: "))

media = (nota1 + nota2 + nota3 + nota4)/4
print(f"Sua media foi = {media:.2f}")
print("Terminou!")'''

#Exercício 8 – Conversor de Medidas (mm/cm/m/km)
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

#Exercício 9 – Tabuada
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
#Exercício 10 – Conversor de Moedas
'''print("\t\tConversor de Moedas\n")

valor = float(input("Entre com um valor em reais:\nR$ "))

dolar = valor/5.59 
euro = valor/6.37
peso = valor*212.44  

print("Convertendo...")
print(f"Dolar - US$: {dolar:.2f}\nEuro - €:{euro:.2f}\nPeso - ARS$: {peso:.2f}")'''

#Exercício 11 – Pintando Parede - calcule a area da parede e a quantidade de tinta para pinta-la
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


#Exercício 12 – Calculando Descontos
'''print("\t\tCalculando descontos\n")
#desconto de 5%
valor = float(input("Qual o valor do produto que deseja adquirir?\n -> "))
desconto = (valor*0.05) #(valor * 5/100) -> outra maneira de fazer
desc_aplic = valor - desconto #desconto (valor * 5/100) -> outra maneira de fazer

print(f"Aplicando desconto de 5% (R${desconto:.2f})\nValor com desconto: R${desc_aplic:.2f}")
print("TERMINOU")'''


#Exercício 13 – Reajuste Salarial
'''print("\t\tReajuste Salarial\n")
#reajuste de 15%
salario = float(input("Digite o valor de seu salario: R$"))
reajuste = salario*0.15
salario_ajustado = salario + reajuste

print(f"Aplicando 15% de ajuste salarial (R$ {reajuste:.2f})\nSeu novo salario é de: R$ {salario_ajustado:.2f}")
print("TERMINOU!")'''


#Exercício 14 – Conversor de Temperaturas
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


#Exercício 15 – Aluguel de Carros
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


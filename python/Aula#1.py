#Exercicio_1
'''dig = int(input("Digite um numero: "))
quad = dig **2
meta = dig /2
print("o quadrado de", dig, "é", quad, "e a metade é", meta)'''

#Exercicio_2
'''temp = float(input("Temperatura em Celsius: "))
F = (9 * temp + 160) / 5
print(f"A temperatura em Graus Celsius em Fahrenheeit é: {F}")'''

#Exercicio_3
'''num1 = float(input("Digite Numero1: "))
num2 = float(input("Digite Numero2: "))
num3 = float(input("Digite Numero3: "))
cal = (num1 + num2 + num3) / 3
print(f"Media dos Numeros é : {cal}")'''

#Exercicio_4
'''num1 = float(input("Digite um Numero: "))
num2 = float(input("Digite outro Numero: "))
Med = (num1 * 3 + num2 * 7) / 10
print("A sua media é:",Med )
#Med1 = (num1 * 3)
#Med2 = (num2 * 7)
#cal = (Med1 + Med2) /10
#print("A sua Mediea ée", cal)'''

#Exercicio_5
'''Nome = str(input("Digite seu nome: "))
num1 = float(input("Digite um Numero:"))
num2 = float(input("Digite outro Numero: "))
med = (num1 + num2) / 2
if num1 >= 7:
    print(f"Parabens {Nome} sua media é: {med}")
else:
    print(f"Voce ficou com media {med}")'''

#Exerecicio_6
n1 = float(input("Digite um Numero: "))
n2 = float(input("Digite outro Numero: "))

por1 = (n1) * 8 / 100
por2 = (n2) * 11 / 100

cal = n1 - (n1 * 8 / 100)
cal1 = n2 - (n2 * 11 / 100)

total = cal + cal1

print("Valor com Desconto é", por1, "e", por2)
print("Valor a ser pago é Avista é: ", total)

#Exercicio_7
'''num = int(input("Digite um numero: "))
for i in range(0, 5):
    print(i)'''

#Ecercicio_8
'''for i in range(1, 6):
    num = int(input("Digite um Numero: "))
    cal = i > num
    if num > i:
        i
    else:
        print("O Numero maior é: ", cal)'''
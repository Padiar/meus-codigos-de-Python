#Exercicio_1
'''Dolar = 4.77
num = float(input("Digite um numero em Reais: "))
converção = float(num) * float(Dolar)
print(f"Dolar Hoje em dia é: {Dolar}")
print(f"A converção é: {converção}")'''
#Exercicio_2
'''for i in range(1, 51, 2):
    print(i)'''
#Exercicio_3
'''num = float(input("Digite o primiero nemro: "))
num1 = float(input("Digite o segundo numero: "))
num2 = float(input("Digite o terceiro numero: "))
num3  = float(input("Dogite o quarto numero: "))
num4 = float(input("Digite o quinto numero: "))

media  =  num + num1 + num2 + num3 + num4 / 5
print(f"A media entre os numeros {num}, {num1}, {num2}, {num3}, {num4} é: {media}")'''
#Exercicio_4
'''num0 = float(input("Digite um  numero: "))
num1 = float(input("Digite outro numero: "))

por1 = num0 * 14/100
por2 = num1 * 17/100

cal = num0 - por1
cal1 = num1 - por2

print(f"O valor com desconto é {cal}, {cal1}")
print("O valor a ser pago sem desconto é: ", num0,",", num1)'''
#Exercidio_5
'''vogal = str(input("Digite uma caracter: "))
if vogal  == "a" or vogal == "A":
    print("Vogal")
elif vogal == "e" or vogal == "E":
    print("Vogal")
elif vogal == "i" or vogal == "I":
    print("Vogal")
elif vogal == "o" or vogal == "O":
    print("Vogal")
else:
    print("É consoante")'''
#Exercicio_6
'''num = int(input("Digite um numero: "))
if num %2 == 0:
    print("É par")
else:
    print("É impar")'''
#Exercicio_7
'''cont = 0
idade = 0
while cont < 10:
    cont += 1
    Ano = int(input("Digite seu ano de nacimento:"))
    if Ano <= 2004:
        idade += 1
print(f"No total tivemos {idade} Maior de idade")'''
#Exercicio_8
'''nome = str(input("Digite seu nome: "))
nota0 = float(input("Digite sua nota: "))
nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))

media = (nota0 + nota1 +  nota2) / 3
if media > 7:
    print(f"Parabens {nome}, voce ficou com media {media}")
elif media < 7 > 5:
    print(f"Você ficou com média {media} e está de recuperação")
elif media < 5:
    print("{nome}, você está reprovado")'''
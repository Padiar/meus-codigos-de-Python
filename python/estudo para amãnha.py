# Calculo de Juros
num = float(input("Digite um valor: "))
juros = 7 / 100
taxa = num * juros
print(f"Valor com Juros é: {taxa:.2f}")
#Quantidade de parcelas
parcela = float(input("Quantidade de parcelas: "))
print(f"Sua parcela é: {parcela + taxa:.2f} de {parcela}")

# Calculo de Imposto de renda
salary = float(input("Digite seu salario: "))
imposto = salary * 7.5 / 100
imposto1 = salary * 15 / 100
imposto2 = salary * 22.5 / 100
imposto3 = salary * 27.5 / 100
if salary < 1903.98:
    print("Seu imposto de renda é: 0              ")
elif salary > 1903.98 or salary < 2826.65:
    print(f"Seu imposto de renda é: {imposto:.2f} ")
elif salary > 2826.65 or salary < 3751.05:
    print(f"Seu imposto de renda é: {imposto1:.2f}")
elif salary > 3751.05 or salary < 4664.68:
    print(f"seu imposto de renda é: {imposto2:.2f}")
elif salary > 4664.68:
    print(f"Seu imposto de renda é: {imposto3:.2f}")

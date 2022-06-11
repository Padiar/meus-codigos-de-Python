#Estrutura de Dados - lista
'''numeros = [1, 5, 12, 13, 20, 39]

print("numeros originais")
for num in numeros:
    print(num)

print("Numeros alterados")
for num in numeros:
    print(num + 3)'''

'''numero = [1, 4, 3, 6, 2, 5]

maior = 0
for i in range(0, 6):
    print(numero[i])

    if numero[i] > maior:
        maior = numero[i]
        pos = i

print(f"O maior numero é {maior}, na posição {pos+1} da lista")'''

#metodos
frutas = ['laranja', 'amora', 'morango', 'banana', 'amora', 'mamão', 'banana']

'''for fruta in frutas:
    print(fruta)

print("Quantidade de amora: ", frutas.count('amora'))
print("Quantidade de mangas: ", frutas.count('manga'))
print("Localização do mamão: ", frutas.index('mamão'))'''

'''print("Adicionando Uva")
frutas.append('Uva')
for fruta in frutas:
    print(fruta)

print("Invertendo a lista")
frutas.reverse()
for fruta in frutas:
    print(fruta)

print("Ordernando a lista")
frutas.sort()
for fruta in frutas:
    print(fruta)'''

#Exercicio

primeiro = int(input("Digite o primeiro termo: "))
quantidade = int(input("Digite a quantidade de termos: "))
razão = int(input("Digite a razão: "))

cont = 0
total = primeiro + razão
while cont < quantidade:
    cont += 1
    print("a", cont, " ... ", total)
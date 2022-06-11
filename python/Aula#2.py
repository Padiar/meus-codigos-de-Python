'''for i in range(0, 7):
    print(i)
print("Fim")'''

'''for i in range(1, 101, 2):
    print(i)
    if i == 11:
        break
print("Fim")'''

'''import math
print(math.sqrt(25))'''
 
print("-------------------")
print("Jogo da Adivinhação")
print("-------------------")

def Aleatorio():

    import random

    segredo = random.randrange(1, 11)
    #print(segredo)

    acertou = False
    tentativas = 3

    for i in range(1, 4):
        print("Você possui", tentativas, "Tentativas de 3/n")
        numero = int(input("Digite um número entre 1 a 10: "))

        if numero == segredo:
            acertou = True 
            
        if acertou:
            print("-------------------------------")
            print("   Você Acertou!!! Parabés     ")
            print("-------------------------------")
            break

        else:
            print("Você errou! Tente novamente/n")
            tentativas -= 1
            Aleatorio()

    print("Game over")
Aleatorio()
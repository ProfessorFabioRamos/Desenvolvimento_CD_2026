'''
fruta = input("Digite o nome da fruta: ")
print("Fruta:", fruta)

fruta = fruta.lower()

match(fruta):
    case "banana":
        print("Amarelo")
    case "maça":
        print("Vermelho")
    case "abacate":
        print("Verde")
    case "açai":
        print("Roxo")
    case _:
        print("Cor indisponível")
'''

'''
from time import sleep
# incluso -> 1:10 <-exclusivo
# Timer de 60 até 0 decrescendo

tempo = int(input("Digite o tempo do timer:"))

for i in range(tempo,-1,-1):
    print(i)
    sleep(1)
'''

'''
# Fazer a soma, printar o somatório e a média
somatorio = 0
repeticoes = int(input("Digite a quantidade de repetições: "))

for i in range(repeticoes):
    numero = float(input("Digite o numero "+str(i+1)+" : "))
    somatorio += numero

print("A soma final é:",somatorio)
print("A média é:", somatorio/repeticoes)
'''

somatorio = 0

while True:
    numero = float(input("Digite um numero: "))
    if numero == 0:
        break
    somatorio += numero

print("A soma final é:",somatorio)

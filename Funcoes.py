# Funções

# Função sem argumento
def saudacao():
    print("Olá!")
    print("Tudo bem?")

#saudacao()

# Função com argumento/parâmetro
def boasvindas(nome, sobrenome):
    print("Bem-vindo(a):",nome,sobrenome)

#boasvindas("Pedro", "Machado")
#boasvindas(sobrenome="Machado",nome="Pedro")

# Função com argumento padrão
def msg(nome, mensagem = ", tudo bem?"):
    print(nome+mensagem)

#msg("João")
#msg("João",", como está?")
#msg("João",mensagem=", blz?")

# Função com retorno
def pi():
    return 3.141592653589793

p = pi()
#print(f"O valor de pi é {p}")
#print(f"O valor de pi é {pi()}")

def soma(a=0,b=0):
    return a+b

#print(soma(3,2))
#print(soma(3))
#print(soma())

'''
import random

def jogar_dados(lados):
    resultado = random.randint(1,lados)
    return resultado

# Colocar esta estrutura dentro de um while True,
# se usuario digitar 0 finaliza o programa
# se não digitar nada usar o valor 6

while True:
    entrada_input = input("Digite a quantidade de lados do dado: ")
    entrada_int = 0

    if entrada_input == None or entrada_input == "":
        entrada_int = 6
    else:
        entrada_int = int(entrada_input)

    if entrada_int == 0:
        break

    result = jogar_dados(entrada_int)
    print(f"O resultado foi: {result}")

print("Programa Finalizado")
'''
def somar(a,b):
    return a+b
def subtrair(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    return a/b

while True:
    print("Bem-vindo à calculadora CLI, digite a opção.")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")
    opcao = int(input("Digite a operação desejada: "))
    if opcao == 0:
        break

    a = int(input("Digite o primeiro numero: "))
    b = int(input("Digite o segundo numero: "))
    resultado = 0

    if opcao == 1:
        resultado = somar(a,b)
    elif opcao == 2:
        resultado = subtrair(a,b)
    elif opcao == 3:
        resultado = multiplicar(a,b)
    elif opcao == 4:
        resultado = dividir(a,b)

    print(f"O resultado é: {resultado}")

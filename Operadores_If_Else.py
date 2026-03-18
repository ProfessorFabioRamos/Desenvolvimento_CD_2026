import math
# print("Olá Mundo")

a = 3
b = 2

# OPERADORES ARITMETICOS
'''
print(a + b)        # Adição
print(a - b)        # Subtração
print(a * b)        # Multiplicação
print(a / b)        # Divisão
print(a // b)       # Divisão retornando a parte inteira
print(a % b)        # Divisão retornando o resto
print(a ** b)       # Potenciação
print(a ** 0.5)     # Raiz Quadrada
print(math.sqrt(a)) # Raiz Quadrada com biblioteca
'''
'''
# OPERADORES RELACIONAIS
print(a > b)            # Maior
print(a >= b)           # Maior ou igual
print(a < b)            # Menor
print(a <= b)           # Menor ou igual
print(a == b)           # Igual
print(a != b)           # Diferente

# OPERADORES LÓGICOS
print(a > b and a > 0)   # E(and)
print(a > b or a > 0)    # Ou(or)
print(a > b ^ a > 0)     # XOR(e/ou)
print(not a > b)         # Negação/contrário
'''

PESO_MAXIMO = 130
PESO_LIMITE = 500
PESO_MINIMO = 10

peso = float(input("Digite o peso: "))

if peso >= PESO_MAXIMO and peso <= PESO_LIMITE:
    print("Excede o limite de peso!")
elif peso < PESO_MAXIMO and peso > PESO_MINIMO:
    print("É permitido utilizar o tobogã.")
elif peso < PESO_MINIMO and peso > 0:
    print("Peso abaixo do permitido!")
else:
    print("Peso inválido")

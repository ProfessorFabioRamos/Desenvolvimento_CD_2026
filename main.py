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

peso = float(input("Digite o peso: "))

if peso >= 120:
    print("Não é permitido utilizar o tobogã!!!")
elif peso < 120 and peso > 0:
    print("É permitido utilizar o tobogã.")
else:
    print("Peso inválido")
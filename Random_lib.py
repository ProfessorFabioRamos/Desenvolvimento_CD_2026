# Biblioteca Random (aleatoriedade)
import random

# Numeros inteiros
numero_dado_20 = random.randint(1,20) # a e b são inclusivos
print("Resultado:", numero_dado_20)

# Numeros inteiros par ou impar
numero_par = random.randrange(0,100,2)
numero_impar = random.randrange(1,100,2)
print("Resultado Par:", numero_par)
print("Resultado Impar:", numero_impar)

frutas = ["Maçã","Banana","Laranja","Uva","Morango"]
# Escolhe um item da lista
fruta_aleatoria = random.choice(frutas)
print(fruta_aleatoria)
# Escolhe x itens da lista com reposição
frutas_aleatorias = random.choices(frutas,k=3)
print(frutas_aleatorias)
# Escolhe x itens da lista sem reposição (diferentes)
frutas_aleatorias_2 = random.sample(frutas,k=3)
print(frutas_aleatorias_2)

# Semente de aleatoriedade (sempre gera o mesmo resultado)
random.seed(42)
dado = random.randint(1,20) # a e b são inclusivos
print("Resultado:", dado)

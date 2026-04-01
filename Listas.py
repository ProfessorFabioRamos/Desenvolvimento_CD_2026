# Estruturas de dados lineares
# Lista = lista dinâmica, utiliza []

'''
# Declaração de lista vazia
vazio = []
vazio_2 = list()

numeros = [5,3,8,9,6]
nomes = ["Kleber","Manuela","Nicolas"]
mista = ["Kleber",26,"01234567890",1.85,142,True]

print(numeros[2])       # Acesso ao indice
print(numeros[-2])      # Começa pelo fim
print(numeros[2:4])     # Intervalo inicio:fim(exclusivo)
print(numeros[:3])      # Intervalo inciciando do indice 0
print(numeros[2:])      # Intervalo até o último indice
print(numeros[:])       # Intervalo completo inicio-fim
print(numeros[::2])     # Intervalo com step 2
print(numeros[::-1])    # Lista invertida
'''
'''
# Modificando elementos
notas = [8.2,2.3,5.6,7.9,4.8]
notas[1] = 4        # Atribuição direta
notas[3:5] = [8,5]  # Atribuição de mais de um elemento
print(notas)
'''

'''
# Adicionar elementos
carros = ["Fusca","Santana","Opala"]
print(carros)
carros.append("Maverick")               # Adiciona no fim da lista
print(carros)
carros.insert(2,"Passat") # Insere no índice indicado
print(carros)
carros.extend(["Escort","Chevette"])    # Adiciona uma nova lista no fim
print(carros)
'''

'''
# Remover elementos
tarefas = [
    "Comprar",
    "Reabastecer",
    "Limpar",
    "Ler",
    "Comprar",
    "Responder"
]
print(tarefas)
tarefas.remove("Reabastecer")   # Remove a primeira ocorrência
print(tarefas)
ultima_tarefa = tarefas.pop()   # Remove o último e pega o retorno
print(ultima_tarefa)
print(tarefas)
del tarefas[1]                  # Deleta no índice indicado
print(tarefas)

t = "Comprar"
while t in tarefas:             # Remove todas as ocorrências
    tarefas.remove(t)

print(tarefas)
tarefas.clear()                 # Remover tudo(limpar lista)
print(tarefas)
'''

# Ordenação
armas = ["Machado","Espada Larga","Nunchaku","Katana","Alabarda"]
print(armas)
armas.sort()                # Ordena em ordem alfabética
print(armas)
armas.reverse()             # Inverte a ordem da lista
print(armas)

armas.sort(reverse=True)    # Ordena e inverte (nesta ordem)
print(armas)

numeros = [56,25,1000,78,0,-2]
print(numeros)
numeros.sort()              # Ordem crescente de numeros
print(numeros)
numeros.sort(reverse=True)
print(numeros)

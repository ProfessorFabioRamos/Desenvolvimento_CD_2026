# Estruturas de dados lineares
# Tupla = lista imutável, utiliza ()

'''
nums = (5,6,25,456,32,4,-8,5)
#nums = 5,6,25,456,32,4,-8,5     #Sem parênteses

# Buscas
print(nums[2])      # Busca pelo índice
#nums[0] = -5       # Erro, não é possível alterar o valor
print(nums[7])
print(nums[-2])     # Busca pelo índice negativo (de trás pra frente)
#print(nums[8])     # Erro, índice fora de alcance(não existe)

# Sub tupla (intervalos)
# Intervalo, valor à esquerda inclusivo, valor à direita exclusivo
sub_tupla = nums[1:3]
print(sub_tupla)
indices_pares = nums[::2]   # A partir de 0 de 2 em 2
print(indices_pares)
indices_impares = nums[1::2]# A partir de 1 de 2 em 2
print(indices_impares)
sub_tupla_inicio = nums[:5] # Do início até 5-1 = 4 (exclusivo)
print(sub_tupla_inicio)
sub_tupla_fim = nums[3:]    # De 3 até o final (não aplica a regra do exclusivo)
print(sub_tupla_fim)
tupla_inteira = nums[:]     # Pegar todos os índices
print(tupla_inteira)
indices_invertidos = nums[::-1]  # Tupla invertida
print(indices_invertidos)
'''
'''
# Print com For (repetição)
# Tupla contem tipos de variáveis diferentes
cliente_1 = ("Marcos", 54, "SP", "4623897",False)
print(cliente_1)

for c in cliente_1:  # c começa do índice 0 e vai até o final
    print(c)

print("Nome:", cliente_1[0])
print("Idade:", cliente_1[1])
print("Estado:", cliente_1[2])
print("RG:", cliente_1[3])
print("Ativo:", cliente_1[4])
'''
'''
# Funções para verificação
nums2 = (5,3,5,65,223,67,-54,223)
print(len(nums2))           # len - Quantidade de elementos
print(nums2.count(5))       # Quantidade de um elementos específico
print(nums2.index(223))     # Primeiro índice de um elemento
print(sum(nums2))           # Calcula a soma dos elementos numéricos
print(sum(nums2)/len(nums2))# Calcular a média dos números
'''
# Lista de Tuplas (2D Matriz)
cliente_1 = ("Marcos", 54, "SP", "4623897",False)
cliente_2 = ("Yasmin",27,"RJ","1248965", True)

cadastro = []               # Declaração de lista vazia
cadastro.append(cliente_1)  # Adicionar tupla de cliente_1 na lista
cadastro.append(cliente_2)  # Adicionar tupla de cliente_2 na lista
print(cadastro)
print(cadastro[0])          # Printa a linha toda
print(cadastro[1][0])       # Printa elemento da linha e coluna

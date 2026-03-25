# Estruturas de dados lineares
# Tupla = lista imutável, utiliza ()

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

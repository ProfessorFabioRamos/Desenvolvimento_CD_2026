# Estruturas de dados lineares
# Tupla = lista imutável, utiliza ()

nums = (5,6,25,456,32,4,-8,5)
#nums = 5,6,25,456,32,4,-8,5     #Sem parênteses

# Buscas
print(nums[2])      # Busca pelo índice
#nums[0] = -5       # Erro, não é possível alterar o valor
print(nums[7])
print(nums[-2])     # Busca pelo índice negativo (de trás pra frente)
#print(nums[8])      # Erro, índice fora de alcance(não existe)

# Sub tupla (intervalos)
# Intervalo, valor à esquerda inclusivo, valor à direita exclusivo
sub_tupla = nums[1:3]  
print(sub_tupla)

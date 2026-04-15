# Estruturas de dados lineares
# Dicionários utiliza {} "chave" : valor (qualquer tipo)

'''
dict_vazio = {}
dict_vazio_2 = dict()

# Par chave:valor
aluno = {
    "nome":"Henrique",
    "idade":26,
    "curso":"Ciência de Dados e ML",
    "ativo": True
}
print(aluno)
print(aluno["nome"])
print(aluno["idade"])
print(aluno["curso"])
print(aluno["ativo"])
#print(aluno["semestre"]) # Gera erro se não existir a chave
name = aluno.get("nome")  # Faz a busca do valor pela chave
print(name)
semestre = aluno.get("semestre") # Retorna None se não existir
print(semestre)
'''

'''
# Criar dicionário a partir de listas
chaves = ["id","status","taxa_acerto"]
valores = [101,"ativo",0.95]
modelo_IA = dict(zip(chaves,valores))
print(modelo_IA)

# Adicionar e modificar valores
perfil_gamificacao = {"usuario":"ninja", "pontos":500}
perfil_gamificacao["nivel"] = "Senior" # Nova chave com valor
perfil_gamificacao["pontos"] = 550  # Novo valor para chave existente
# Update = adiciona novos elementos e atualiza existentes ao mesmo tempo
perfil_gamificacao.update(
    {"pontos": 1000, "ultimoLogin":"08-04-26","nivel":"Mestre"})
print(perfil_gamificacao)
'''

'''
# Removendo elementos
carrinho_loja_informatica = {
    "mouse":79.99,
    "teclado_gamer":249.99,
    "monitor":1499.00,
    "placa_RTX": 15000.75
}
print(carrinho_loja_informatica)
# Anular valor da chave
carrinho_loja_informatica["teclado_gamer"] = None
# Remove e retorna valor
preco_mouse = carrinho_loja_informatica.pop("mouse")
print(preco_mouse)
# Remove último par chave/valor como tupla
ultimo_item = carrinho_loja_informatica.popitem()
print(ultimo_item)
# Remove sem retornar
del carrinho_loja_informatica["teclado_gamer"]
# Limpar dicionario, ou seja, apaga tudo
carrinho_loja_informatica.clear()

print(carrinho_loja_informatica)
'''

'''
# Iteração (laços de repetição)
faturamento = {"jan":1000,"fev":1500,"mar":1800}

for mes in faturamento.keys():      # Iteração apenas nas chaves
    print(mes)

for fatu in faturamento.values():   # Iteração apenas nos valores
    print(fatu)

for mes, fatu in faturamento.items(): # Iteração no par chave/valor
    print(f"No mês {mes} o faturamento foi {fatu} reais.")
'''

'''
# Dicionário aninhado, similiar a JSON
banco_de_dados = {
    "cliente_1":{
        "nome":"Ana",
        "compra":["Livro","Caneta"]
    },
    "cliente_2":{
        "nome":"Bruno",
        "compra":["Caderno","Tesoura"]
    },
    "cliente_3":{
        "nome":"Caio",
        "compra":["Borracha","Livro"]
    }
}

#print(banco_de_dados)
# Dados do cliente 1
cliente_1 = banco_de_dados["cliente_1"] # Dados do cliente 1
print(cliente_1)

# Compras do cliente 1
compras_ana = banco_de_dados["cliente_1"]["compra"]
print(compras_ana)

# Item 0 da lista de compras do cliente 2
primeira_compra_bruno = banco_de_dados["cliente_2"]["compra"][0]
print(primeira_compra_bruno)

# Nome do cliente 3
nome_cliente_3 = banco_de_dados["cliente_3"]["nome"]
print(nome_cliente_3)
'''
# Mesclar dicionários
dict1 = {"a":1,"b":2,"c":3}
dict2 = {"d":4,"e":5,"f":6}

# Comando | mescla dicionários partir do Python 3.9
dict3 = dict1 | dict2
print(dict3)

# Versão antiga de mesclagem
dict4 = {**dict1, **dict2}
print(dict4)

import tkinter as tk
from tkinter import ttk

lista_cadastro = [
    "Nome: Bruno Costa, Idade: 54, Email: bruno@email.com",
    "Nome: Carla Fernandes, Idade: 27, Email: carla@email.com",
    "Nome: Francisco Mendes, Idade: 32, Email: francisco@email.com",
    "Nome: Eliz Silva, Idade: 19, Email: eliz@email.com",
]

root = tk.Tk()
root.title("Cadastro")
root.geometry("450x300")

# Criação do container (notebook) de abas
notebook = ttk.Notebook(root)

# Criação das abas (frames)
aba1 = ttk.Frame(notebook)
aba2 = ttk.Frame(notebook)
aba3 = ttk.Frame(notebook)

notebook.add(aba1, text="Cadastro")
notebook.add(aba2, text="Consulta")
notebook.add(aba3, text="Configurações")

# Empacotar o notebook na tela (root)
notebook.pack(padx=10,pady=10,expand=True, fill="both")

# Widgets da Aba 1
label_aba_1 = ttk.Label(aba1, text="Formulário de Cadastro")
label_aba_1.pack(padx=20,pady=20)
entry_nome = ttk.Entry(aba1, width=40)
entry_nome.pack(padx=20,pady=5)
button_salvar = ttk.Button(aba1,text="Salvar")
button_salvar.pack(pady=10)
# TO DO: função de salvar o nome

# Widgets da Aba 2
label_aba_2 = ttk.Label(aba2, text="Consulta")
label_aba_2.pack(padx=20, pady=20)
button_buscar = ttk.Button(aba2, text="Buscar")
#button_buscar.config(command=exibir_cadastro)
button_buscar.pack(pady=10)
# Widget caixa que recebe texto
caixa_texto = tk.Text(
                    aba2,
                    height= 20,
                    width=60,
                    wrap="word",
                    font=("Arial", 10)
                    )
caixa_texto.pack(pady=20, fill="both", expand=True)
# Inicia bloqueado por padrão
caixa_texto.config(state="disabled")

root.mainloop()

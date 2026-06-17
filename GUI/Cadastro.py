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

# Aba 3 - Novos Widgets
# Variável especial de controle do checkbox
var_check = tk.BooleanVar()
# Estado inicial do checkbox
var_check.set(False)
# Widget checkbox
check_button = ttk.Checkbutton(aba3,
                               text ="Receber Notificações?",
                               variable = var_check)
check_button.pack(padx=20,pady=30)
# Função para buscar o valor da checkbox (não usado aqui)
#check_button.getboolean()

# Frame para colocar o dropdown e slider
frame = ttk.LabelFrame(aba3, text="Opções")
frame.pack(padx=10,pady=10)

lista_estado_civil = [
    "Selecione uma opção",
    "Solteiro(a)",
    "Casado(a)",
    "Divirciado(a)",
    "Viúvo(a)"
]

# Dropdown (ComboBox)
combo_opcoes = ttk.Combobox(frame,
                            values= lista_estado_civil,
                            state="readonly")
combo_opcoes.pack(padx=5,pady=10)
# Estado incial do Combobox
combo_opcoes.current(0)
# Label com estado civil
label_estado_civil = ttk.Label(frame, text="Estado Civil:")
label_estado_civil.pack(padx=10,pady=5)
combo_opcoes.bind("<<ComboboxSelected>>", select_combo)

# Slider (Scale)
slider = ttk.Scale(frame,
                    from_ = 0,
                    to = 100,
                    orient="horizontal",
                    command= change_slider
                    )
slider.pack(padx=5, pady=10,fill="x")
# Label com valor do slider(scale)
label_slider = ttk.Label(frame, text="Volume: 0")
label_slider.pack(padx=10,pady=5)

root.mainloop()

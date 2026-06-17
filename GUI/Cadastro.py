import tkinter as tk
from tkinter import ttk

lista_cadastro = [
    "Nome: Bruno Costa, Idade: 54, Email: bruno@email.com",
    "Nome: Carla Fernandes, Idade: 27, Email: carla@email.com",
    "Nome: Francisco Mendes, Idade: 32, Email: francisco@email.com",
    "Nome: Eliz Silva, Idade: 19, Email: eliz@email.com",
]

def exibir_cadastro():
    # Modo de edição ligado
    caixa_texto.config(state="normal")
    # Limpa a caixa inteira de 1 até o final
    caixa_texto.delete("1.0", tk.END)
    # Juntar todos os elementos da lista mas adiciona uma quebra de linha
    texto_formatado = "\n".join(lista_cadastro)
    # Insere texto formatado na caixa de texto do início (END)
    caixa_texto.insert(tk.END, texto_formatado)
    # Modo de edição desligado
    caixa_texto.config(state="disabled")

def toggle_checkbox():
    valor = var_check.get()
    valor_string = "Ligado" if valor else "Desligado"
    label_checkbox.config(text=valor_string)

def select_combo(event):
    valor = combo_opcoes.get()
    if valor != "Selecione uma opção":
        label_estado_civil.config(text=f"Estado Civil: {valor}")

def change_slider(valor): # valor = string
    print(valor)
    valor_int = f"{float(valor):.0f}"
    label_slider.config(text=f"Volume: {valor_int}")

root = tk.Tk()
root.title("Cadastro")
root.geometry("450x350")

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
button_buscar.config(command=exibir_cadastro)
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
                               variable = var_check,
                               command=toggle_checkbox)
check_button.pack(padx=20,pady=20)
# Função para buscar o valor da checkbox (não usado aqui)
#check_button.getboolean()
# Label do checkbox
label_checkbox = ttk.Label(aba3, text="Desligado")
label_checkbox.pack(padx=20,pady=5)


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

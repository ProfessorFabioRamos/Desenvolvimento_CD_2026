import tkinter as tk

# Cria janela principal
root = tk.Tk()

# Titulo da janela
root.title("Aula 1 Tk")

# Tamanho da janela (largura x altura)
root.geometry("300x150")

# Cor do background (ciano)
root.configure(bg="#42f5ef")

# Função a ser chamada quando apertar o botão
def on_button_click():
    label.config(text="Bem-vindo!")

# Widget Label (rótulo)
label = tk.Label(root,text="Olá Mundo!", font = (
    ("Comic Sans MS", 14, "bold", "italic", "underline")
))

# Posiciona a label no centro, com espaçamento vertical
label.pack(pady=10)


button = tk.Button(root, text="Clique Aqui", command=on_button_click)
button.pack(pady=5)

root.mainloop()

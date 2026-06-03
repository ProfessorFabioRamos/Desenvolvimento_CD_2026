import tkinter as tk

# Cria janela principal
root = tk.Tk()

# Titulo da janela
root.title("Calculadora")

# Tamanho da janela (largura x altura)
root.geometry("300x250")

# Cor do background (azul)
root.configure(bg="#333463")

# Função a ser chamada quando apertar o botão
def calcular_soma():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    soma = num1 + num2
    label_result.config(text=f"Resultado: {soma}")

# Cria uma label fixa(sem objeto) e faz pack na mesma linha
tk.Label(root, text="CALCULADORA", font = "Arial, 16").pack(pady=5)

# Caixa de entrada de texto para numero 1
entry1 = tk.Entry(root)
entry1.pack(pady=5)

# Label para o sinal de soma (+)
tk.Label(root, text="+", font = "Arial, 12").pack(pady=5)

# Caixa de entrada de texto para numero 2
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Widget Button, precisa de uma função em command
button = tk.Button(root, text="Somar", command=calcular_soma)

# Posiciona a label no centro, com espaçamento vertical
button.pack(pady=5)

# Label de resultado final
label_result = tk.Label(root,text="Resultado: ", font="Arial, 16")
label_result.pack(pady=10)

# Loop de eventos, mantem a janela aberta esperando interações
root.mainloop()

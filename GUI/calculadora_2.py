import tkinter as tk

# Cria janela principal
root = tk.Tk()

# Titulo da janela
root.title("Calculadora 2")

# Tamanho da janela (largura x altura)
root.geometry("220x300")

# Cor do background (azul)
cor_de_fundo = "#333463"
root.configure(bg = cor_de_fundo)

# Variável global 
result = 0 

# Função a ser chamada quando apertar o botão
def operacao(op):
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    match(op):
        case 0:
            result = num1 + num2
        case 1:
            result = num1 - num2
        case 2:
            result = num1 * num2
        case 3:
            result = num1 / num2
        case _:
            result = 0
    
    label_result.config(text=f"Resultado: {result:.2f}")
    

# Cria uma label
title = tk.Label(root,
                text="CALCULADORA",
                #font = ("SEGA LOGO FONT","16"),
                font = ("Arial","16","bold"),
                bg = cor_de_fundo,
                fg = "#c90c35"
                )
title.grid(row = 0, column = 0, columnspan= 2, pady= 10)

# Caixa de entrada de texto para numero 1
entry1 = tk.Entry(root, width=10)
entry1.grid(row =1,column= 0,padx=20, pady=5, sticky='e')

# Caixa de entrada de texto para numero 2
entry2 = tk.Entry(root, width=10)
entry2.grid(row =1,column= 1,padx=20, pady=5, sticky='e')

# Botão de soma
sum_button = tk.Button(root, text="+")
sum_button.grid(row=2,column=0,padx=10,pady=10)
sum_button.config(command=lambda:operacao(0))

# Botão de subtração
sub_button = tk.Button(root, text="-")
sub_button.grid(row=2,column=1,padx=10,pady=10)
sub_button.config(command=lambda:operacao(1))

# Botão de multiplicação
mult_button = tk.Button(root, text="x")
mult_button.grid(row=3,column=0,padx=10,pady=10)
mult_button.config(command=lambda:operacao(2))

# Botão de divisão
div_button = tk.Button(root, text="/")
div_button.grid(row=3,column=1,padx=10,pady=10)
div_button.config(command=lambda:operacao(3))

# Label de resultado final
label_result = tk.Label(root,
                    text="Resultado: ",
                    font=("Arial","16"),
                    bg = cor_de_fundo,
                    fg = "#c90c35"
                    )
label_result.grid(row = 4, column=0, columnspan=2,pady=10)

# Loop de eventos, mantem a janela aberta esperando interações
root.mainloop()

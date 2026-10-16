import tkinter as tk

janela = tk.Tk()
janela.title('Painel Principal')
janela.geometry("400x300")


texto = tk.Label(janela, text=f"Seu nome: ")
texto.pack()

def resposta_botao():
    nome = entrada_texto.get()
    texto['text'] = f"Olá, {nome}"

entrada_texto = tk.Entry(janela)
entrada_texto.pack()

tk.Button(janela, text= "BOTAO", command=resposta_botao).pack()

janela.mainloop()
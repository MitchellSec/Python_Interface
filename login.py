import tkinter as tk

contas = [
    ("Mayck", "1234"),
    ("Guanabara", "gafanhoto")
]

janela = tk.Tk()
janela.title("Login")
janela.geometry("400x300")

pagina_login = tk.Frame(janela)
pagina_login.pack()

tk.Label(pagina_login, text= "Usuário").pack()
usuario_entry = tk.Entry(pagina_login)
usuario_entry.pack()

tk.Label(pagina_login, text= "Senha").pack()
senha_entry = tk.Entry(pagina_login)
senha_entry.pack()

def login():
    usuario = usuario_entry.get()
    senha  = senha_entry.get()
    if (usuario, senha) in contas:
       pagina_login.pack_forget()
       pagina_sistema.pack()
    else: 
        mensagem_label["text"] = "Login invalido"

tk.Button(pagina_login, text="Login", command=login).pack()

mensagem_label = tk.Label(pagina_login, text="")
mensagem_label.pack()

pagina_sistema = tk.Frame()
tk.Label(pagina_sistema, text="Bem vindo ao sistema").pack()


janela.mainloop()

# Sistema Integrado de Login e Painel em Python 🐍

Este projeto é uma aplicação desktop desenvolvida em **Python** utilizando a biblioteca gráfica nativa **Tkinter**. O objetivo principal é demonstrar a transição de telas e a interatividade em interfaces gráficas (GUI), unindo um sistema de autenticação de usuários a um painel interativo.

---

##  Sobre o Projeto

O sistema funciona em duas etapas principais na mesma janela:

1. **Tela de Login:** 
   * Solicita as credenciais de acesso (`Usuário` e `Senha`).
   * Valida os dados informados com uma lista de contas pré-cadastradas no código.
   * Caso o login seja bem-sucedido, oculta a tela de login e revela o painel do sistema. Se os dados estiverem incorretos, exibe uma mensagem de erro.

2. **Painel Principal (Sistema):**
   * Tela acessada apenas após a autenticação correta.
   * Possui um campo de texto (`tk.Entry`) onde o usuário pode digitar o seu nome.
   * Conta com um botão interativo que captura o nome inserido e atualiza o texto do rótulo (`tk.Label`) na tela, exibindo uma saudação personalizada.

---

## 🔑 Credenciais de Acesso (Teste)

Você pode utilizar uma das seguintes contas para testar o sistema:

* **Conta 1:**
  * **Usuário:** `Mayck`
  * **Senha:** `1234`

* **Conta 2:**
  * **Usuário:** `Guanabara`
  * **Senha:** `gafanhoto`

---

##  Tecnologias Utilizadas

* **Python** (Linguagem de programação)
* **Tkinter** (Biblioteca padrão para criação de interfaces gráficas em Python)

---

##  Como Executar

Certifique-se de ter o Python instalado em sua máquina (o Tkinter já vem instalado por padrão na grande maioria das distribuições do Python).

1. Clone este repositório ou baixe o arquivo do código-fonte para o seu computador.
2. Abra o terminal (ou prompt de comando) na pasta onde o arquivo está salvo.
3. Execute o comando abaixo:

```bash
python app.py

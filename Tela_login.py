from tkinter import *
from tkinter import messagebox #importa o modulo de caixas de mensagem do tkinter
from tkinter import ttk#importa o modulo de widgets tematicos do tkinter
from dataclasses import database#importa a classe Database do modulo DataBase

#cria a janela
jan = Tk()
jan.title("SL Sytens - Painel de Acesso")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False,height=False)

#deixar a tela transparente
jan.attributes("-alpha, 0.9")
jan.iconbitmap(default="C:/Users/caio_battisti/Documents/GitHub/foto/logo.png")#carrega a imagem da logo

#cria a Frame
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE",relief="raise")#cria a frame a esquerda
LeftFrame.pack(side=LEFT)
RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE",relief="raise")#cria a frame a direita
RightFrame.pack(side=RIGHT)

#adicionar o logo
Logolabel = Label(LeftFrame, image=Logo, bg="MIDNIGHTBLUE")#cria im label para a imgem ao lado
Logolabel.place(x=50, y=100)#posiciona o label no frame esquerdo

#aicionar campos de usuario e senha
usuarioLabel = Label(RightFrame, text="Usuario: ",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White")#cria um albel para o usuario
usuarioLabel.place(x=5, y=100)#posiciona o label no frame direito
usuarioEntry = ttk.Entry(RightFrame, width=30)#cria um campo de entrada para o usuario
usuarioEntry.place(x=120, y=115)#posiciona o campo de entrada

senhaLabel = Label(RightFrame, text="Senha: ",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White")#cria um albel para a senha
senhaLabel.place(x=5, y=150)#posiciona o label no frame direito
senhaEntry = ttk.Entry(RightFrame, width=30, show=".")#cria um campo de entrada para a senha
senhaEntry.place(x=120, y=165)#posiciona o campo de entrada

#função de login
def Login():
    usuario = usuarioEntry.get()
    senha = senhaEntry.get()

#conectar ao banco de dado
    db = database()
    db.cursor.execute("""SELECT * FROM usuario1 WHERE usuario = %s""",(usuario, senha))
    VerifiyLogin = db.cursor.fetchone()

#ferificar se o usuario foi encontrado
    if VerifiyLogin:
        messagebox.showinfo(title="Info Login", Message ="Acesso Confirmado. Bem Vindo!")
    else:
        messagebox.showinfo(title="Info Login", Message="Acesso Negado, Verifique se o cadastro esta no sistema")

#criando botões
LoginButton = ttk.Button(RightFrame, text="Login",width=15, command=Login)
LoginButton.place(x=150,y=225)

#função para registrar novo usuario
def registrar():
    #removendo botões de Login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)

#inserindo widgets de cadastro
    NomeLabel = Label(RightFrame, text="Nome:",font=("Century Gothic", 20),bg="MIDNIGHTBLUE",fg="White")
    NomeLabel.place(x=5, y=5)
    NomeEntry = ttk.Entry(RightFrame, width=30)
    NomeEntry.place(x=120, y=20)

    EmailLabel = Label(RightFrame, text="Email:",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White")
    EmailLabel.place(x=5,y=40)
    EmailEntry = ttk.Entry(RightFrame, width=30)
    EmailEntry.place(x=120,y=55)

    #
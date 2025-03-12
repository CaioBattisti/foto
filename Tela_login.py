from tkinter import *
from tkinter import messagebox #importa o modulo de caixas de mensagem do tkinter
from tkinter import ttk #importa o modulo de widgets tematicos do tkinter
from DataBase import MYSLQ_DATABASE #importa a classe Database do modulo DataBase

# Cria a janela
jan = Tk()
jan.title("SL Sytens - Painel de Acesso")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False,height=False)

#jan.iconbitmap(default="C:/Users/caio_battisti/Documents/GitHub/foto/logo.png")#carrega a imagem da logo

#cria a Frame
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE",relief="raise")#cria a frame a esquerda
LeftFrame.pack(side=LEFT)
RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

#adicionar o logo
#Logolabel = Label(LeftFrame, image=Logo, bg="MIDNIGHTBLUE")#cria im label para a imgem ao lado
#Logolabel.place(x=50, y=100)#posiciona o label no frame esquerdo

#adicionar campos de usuario e senha
usuarioLabel = Label(RightFrame, text="Usuario: ",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White")#cria um albel para o usuario
usuarioLabel.place(x=5, y=100)#posiciona o label no frame direito
usuarioEntry = ttk.Entry(RightFrame, width=30)#cria um campo de entrada para o usuario
usuarioEntry.place(x=120, y=115)#posiciona o campo de entrada

senhaLabel = Label(RightFrame, text="Senha: ", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
senhaLabel.place(x=5, y=150)
senhaEntry = ttk.Entry(RightFrame, width=30, show="*")  # Usa "*" para ocultar a senha
senhaEntry.place(x=120, y=165)

# Função de login
def Login():
    usuario = usuarioEntry.get()
    senha = senhaEntry.get()

#conectar ao banco de dado
    db = MYSLQ_DATABASE()
    db.cursor.execute("""
    SELECT * FROM usuario1 
    WHERE usuario = %s and senha = %s""",(usuario, senha))
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

    #função para registrar no banco de dados
    def RegistrarNoBanco():
        nome = NomeEntry.get()
        Email = EmailEntry.get()
        usuario = usuarioEntry.get()
        senha = senhaEntry.get()
        #vefica se todos os campos estão preenchidos
        if nome == "" or Email == "" or usuario == "" or senha == "":
            messagebox.showerror(title="Erro de registro",message="Preencha todos os campos!")
        else:
            db = MYSLQ_DATABASE()
            db.RegistrarNoBanco(nome,Email,usuario,senha)
            messagebox.showinfo("Sucesso","Usuario registrado com Sucesso!")
#Limpar campos após o registro
        NomeEntry.delete(0,END)
        EmailEntry.delete(0,END)
        usuarioEntry.delete(0,END)
        senhaEntry.delete(0,END)
    Register = ttk.Button(RightFrame, text="registrar",width=15, command=RegistrarNoBanco)
    Register.place(x=150,y=225)
#função para voltar a tela de login
    def VoltarLogin():
        #removendo widgets de cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=10000)
        EmailEntry.place(x=10000)
        Register.place(x=5000)
        Voltar.place(x=5000)
    
        #trazendo de volta o widgets
    LoginButton.place(x=150)
    
    RegisterButton.place(x=150)
        
    Voltar = ttk.Button(RightFrame, text="Voltar",width=15,command=VoltarLogin)
    Voltar.place(x=150,y=255)

RegisterButton = ttk.Button(RightFrame, text="Registrar",width=15,command=registrar)
RegisterButton.place(x=150,y=255)

#iniciar o loop principal
jan.mainloop()
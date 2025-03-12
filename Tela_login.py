from tkinter import *
from tkinter import messagebox  # Importa o módulo de caixas de mensagem do tkinter
from tkinter import ttk  # Importa o módulo de widgets temáticos do tkinter
from DataBase import get_connection  # Importa a função correta do módulo DataBase

# Cria a janela
jan = Tk()
jan.title("SL Systems - Painel de Acesso")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)

#jan.iconbitmap(default="C:/Users/caio_battisti/Documents/GitHub/foto/logo.png")#carrega a imagem da logo

# Cria a Frame
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")  # Cria a frame à esquerda
LeftFrame.pack(side=LEFT)
RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

# Adicionar campos de usuário e senha
usuarioLabel = Label(RightFrame, text="Usuário: ", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
usuarioLabel.place(x=5, y=100)  # Posiciona o label no frame direito
usuarioEntry = ttk.Entry(RightFrame, width=30)  # Cria um campo de entrada para o usuário
usuarioEntry.place(x=120, y=115)  # Posiciona o campo de entrada

senhaLabel = Label(RightFrame, text="Senha: ", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
senhaLabel.place(x=5, y=150)
senhaEntry = ttk.Entry(RightFrame, width=30, show="*")  # Usa "*" para ocultar a senha
senhaEntry.place(x=120, y=165)

# Função de login
def Login():
    usuario = usuarioEntry.get()
    senha = senhaEntry.get()

    try:
        # Conectar ao banco de dados
        conn = get_connection()  # Usa a função get_connection() para conexão
        cursor = conn.cursor()

        # Executar a consulta
        cursor.execute("""
        SELECT * FROM usuario1 
        WHERE usuario = %s AND senha = %s""", (usuario, senha))  # Ajuste para MySQL
        VerifiyLogin = cursor.fetchone()

        # Verificar se o usuário foi encontrado
        if VerifiyLogin:
            messagebox.showinfo(title="Info Login", message="Acesso Confirmado. Bem-vindo!")
        else:
            messagebox.showinfo(title="Info Login", message="Acesso Negado. Verifique as credenciais.")
    except Exception as e:
        messagebox.showerror(title="Erro", message=f"Erro ao realizar login: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

# Criando botões
LoginButton = ttk.Button(RightFrame, text="Login", width=15, command=Login)
LoginButton.place(x=150, y=225)

# Função para registrar novo usuário
def registrar():
    # Removendo botões de Login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)

    # Inserindo widgets de cadastro
    NomeLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    NomeLabel.place(x=5, y=5)
    NomeEntry = ttk.Entry(RightFrame, width=30)
    NomeEntry.place(x=120, y=20)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    EmailLabel.place(x=5, y=50)
    EmailEntry = ttk.Entry(RightFrame, width=30)
    EmailEntry.place(x=120, y=70)

    # Função para registrar no banco de dados
    def RegistrarNoBanco():
        nome = NomeEntry.get()
        email = EmailEntry.get()
        usuario = usuarioEntry.get()
        senha = senhaEntry.get()

        # Verifica se todos os campos estão preenchidos
        if nome == "" or email == "" or usuario == "" or senha == "":
            messagebox.showerror(title="Erro de Registro", message="Preencha todos os campos!")
        else:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("""
                INSERT INTO usuario (nome, email, usuario, senha) 
                VALUES (%s, %s, %s, %s)""", (nome, email, usuario, senha))
                conn.commit()
                messagebox.showinfo("Sucesso", "Usuário registrado com sucesso!")
            except Exception as e:
                messagebox.showerror(title="Erro de Registro", message=f"Erro: {e}")
            finally:
                if 'cursor' in locals():
                    cursor.close()
                if 'conn' in locals():
                    conn.close()

            # Limpar campos após o registro
            NomeEntry.delete(0, END)
            EmailEntry.delete(0, END)
            usuarioEntry.delete(0, END)
            senhaEntry.delete(0, END)

    Register = ttk.Button(RightFrame, text="Registrar", width=15, command=RegistrarNoBanco)
    Register.place(x=150, y=225)

    # Função para voltar à tela de login
    def VoltarLogin():
        # Remover widgets de cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Voltar.place(x=5000)

        # Trazer de volta os widgets de login
        LoginButton.place(x=150)
        RegisterButton.place(x=150)

    Voltar = ttk.Button(RightFrame, text="Voltar", width=15, command=VoltarLogin)
    Voltar.place(x=150, y=255)

RegisterButton = ttk.Button(RightFrame, text="Registrar", width=15, command=registrar)
RegisterButton.place(x=150, y=255)

# Iniciar o loop principal
jan.mainloop()

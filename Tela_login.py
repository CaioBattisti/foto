from tkinter import *
from tkinter import messagebox  # Importa o módulo de caixas de mensagem do tkinter
from tkinter import ttk  # Importa o módulo de widgets temáticos do tkinter
from DataBase import Database  # Certifique-se de que a classe Database está correta

# Cria a janela
jan = Tk()
jan.title("SL Sytens - Painel de Acesso")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)

# Cria a Frame
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)
RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

# Adicionar campos de usuário e senha
usuarioLabel = Label(RightFrame, text="Usuário: ", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
usuarioLabel.place(x=5, y=100)
usuarioEntry = ttk.Entry(RightFrame, width=30)
usuarioEntry.place(x=120, y=115)

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
        db = Database()
        conn = db.get_connection()
        cursor = conn.cursor()

        # Executar a consulta
        cursor.execute("""
        SELECT * FROM usuario1 
        WHERE usuario = %s AND senha = %s""", (usuario, senha))
        VerifiyLogin = cursor.fetchone()

        # Verificar se o usuário foi encontrado
        if VerifiyLogin:
            messagebox.showinfo(title="Info Login", message="Acesso Confirmado. Bem-vindo!")
        else:
            messagebox.showinfo(title="Info Login", message="Acesso Negado. Verifique suas credenciais.")
    except Exception as e:
        messagebox.showerror(title="Erro", message=f"Erro ao realizar login: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

# Criar botões
LoginButton = ttk.Button(RightFrame, text="Login", width=15, command=Login)
LoginButton.place(x=150, y=225)

# Iniciar o loop principal
jan.mainloop()

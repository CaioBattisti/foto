import mysql.connector

class Database:
    def __init__(self):
        #conecta ao banco de dados
        self.conn = mysql.connector.connect(
            host ="localhost",
            user ="root", 
            password ="",
            Database ="CaioBattisti_db" 
        )
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS 
        usuario1(                    
            idusuario INT AUTO_INCREMENT PRIMARY KEY               
            nome TEXT (255),               
            email TEXT (255),               
            usuario TEXT (255),  
            senha TEXT (255)                           
        );''')
        self.conn.commit()

    print("Conectando ao Banco de Dados")

#Método para registrar um novo usuário no Banco de Dados
    def RegistrarnoBanco(self,nome,email,usuario,senha):
        self.cursor.execute("INSERT INTO usuario1 (nome,email,usuario,senha) VALUES (%s,%s,%s,%s)",
                            (nome,email,usuario,senha))
        self.conn.commit()

#Método para alterar os dados de um usuario existente no Banco de Dados
    def alterar(self,idusuario,nome,email,usuario,senha):
        self.cursor.execute("UPDATE usuario1 SET nome=%s, email=%s, usuario=%s,senha=%s WHERE idusuario=%s",
                            (nome,email,usuario,senha,idusuario))
        self.conn.commit()

#Método para excluir usuario do Banco de Dados
    def excluir(self,idusuario):
        self.cursor.execute("DELETE FROM usuario1 WHERE idusuario=%s",(idusuario))
        self.conn.commit()

#Método para buscar os Dados de um usuario no Banco de Dados
    def buscar(self,idusuario):
        self.cursor.execute("SELECT * FROM usuario1 WHERE idusuario=%s",(idusuario))
        self.conn.commit()
        
#Método chamado quando a instancia da classe é destruida
    def __del__(self):
        self.conn.close()
import mysql.connector

# Configurações do banco de dados
MYSQL_HOST = "localhost"  # Remove a vírgula
MYSQL_USER = "root"  # Remove a vírgula
MYSQL_PASSWORD = ""  # Remove a vírgula
MYSQL_DATABASE = "caiobattisti_db"  # Corrigir o nome da constante

def get_connection():
    try:
        # Conecta ao banco de dados
        return mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE  # Corrigido para 'database' (letra minúscula)
        )
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        raise

def create_user(nome, telefone, email, usuario, senha):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO usuario (nome, telefone, email, usuario, senha) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nome, telefone, email, usuario, senha))
    conn.commit()
    cursor.close()
    conn.close()

def read_users():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM usuario"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def update_user(nome, telefone, email, usuario, senha, user_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE usuario SET nome=%s, telefone=%s, email=%s, usuario=%s, senha=%s WHERE idusuario=%s"
    cursor.execute(query, (nome, telefone, email, usuario, senha, user_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM usuario WHERE idusuario=%s"
    cursor.execute(query, (user_id,))
    conn.commit()
    cursor.close()
    conn.close()

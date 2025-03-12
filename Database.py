import mysql.connector

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_DATABASE = "caiobattisti_db"

def get_connection():
    try:
        return mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE  # Corrigido para 'database'
        )
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        raise

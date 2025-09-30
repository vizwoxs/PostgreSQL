import psycopg2 as pg
from dotenv import load_dotenv
import os
#pip install dotenv


params = {
    "dbname": os.getenv("DB_NAME"),
    "dbuser": os.getenv("DB_USER"),
    "dbpassword": os.getenv("DB_PASSWORD"),
    "dbhost": os.getenv("DB_HOST"),
    "dbport": os.getenv("DB_PORT"),
}

def conectar():
    try:
        conexao = pg.connect(**params)
        cursor = conexao.cursor()
        return conexao, cursor
    except Exception as erro:
        print(f"Erro de conexão {erro}")
        return None, None


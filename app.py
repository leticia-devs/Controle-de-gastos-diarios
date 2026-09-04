import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="teste",
    database="financias_db",
)

cursor = conexao.cursor()

print("--- Cadastrar Nova Despesa ---")
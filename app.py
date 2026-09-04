import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="teste",
    database="financias_db",
)

cursor = conexao.cursor()

print("--- Cadastrar Nova Despesa ---")
valor = float(input("Digite o valor gasto (ex: 45.90): "))
categoria = input("Digite a categoria (ex: Alimentação, Transporte): ")
descricao = input("Digite uma descrição (100 caracteres): ")
data = input("Digite a data (AAAA-MM-DD): ")

comando = """
    INSERT INTO despesas (valor, categoria, descricao, data) 
    VALUES (%s, %s, %s, %s)
"""

valores = (valor, categoria, descricao, data)
cursor.execute(comando, valores)
conexao.commit()

print("Despesa cadastrada com sucesso!")
conexao.close()

import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="teste",
    database="financias_db",
)

cursor = conexao.cursor()

print("--- Cadastrar Nova Despesa ---")

conexao.close()
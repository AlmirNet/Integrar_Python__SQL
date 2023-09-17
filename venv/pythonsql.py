import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-ENBV1N0;"
    "Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print("Executed Successfully")

cursor = conexao.cursor()


id = 3
cliente = "Almir Python"
produto= "Carro"
data = "16/09/2023"
preco = 9000
quantidade = 1

comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    ({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""

cursor.execute(comando)
cursor.commit()

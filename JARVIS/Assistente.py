import mysql.connector
def conectar_banco():
    try:
        conexao = mysql.connector.connect(
            host="localhost", #Endereço do servidor
            user="seu_usuario", #Usuário padrão geralmente é 'root'
            password="sua_senha", #Senha que você definiu na instalação
            database="assistente_db" #Nome do banco criado
        )
        
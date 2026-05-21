import pyttsx3
import speech_recognition as sr 
import sqlite3
#Inicialíza o mototr de voz
engine = pyttsx3.init()
def fala(texto):
    engine.say(texto)
    engine.runAndWait()
def consultar_banco(comando):
    # Conecta ao banco de dados (ou cria um se não existir)
    conexao = sqlite3.connect('assistente_dados.db')
    cursor = conexao.cursor()
    # Cria a tabela caso não exista
    cursor.execute("CREATE TABLE IF NOT EXISTS memorias (id INTEGER PRIMARY KEY AUTOINCREMENT, chave TEXT, reposta TEXT)")
    #Busca a resposta no banco de dados
    cursor.execute("SELECT resposta FROM memorias WHERE chave = ?",(comando,))
    resultado = cursor.fetchone()
    conexao.close()
    if resultado:
        return resultado[0]
    else:
            return "Desculpe não encontrei essa informaçao no meu banco de dados."
    #Exemplo de uso:
    #resposta = consultar_banco("qual o meu saldo")
    #falar(resposta)        

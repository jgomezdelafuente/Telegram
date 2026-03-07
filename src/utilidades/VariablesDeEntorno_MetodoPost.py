import requests
#python-dotenv es una librería de Python que sirve para cargar variables de entorno desde un archivo .env.
#pip install python-dotenv
from dotenv import load_dotenv
#acceder a funciones del sistema operativo
import os

#Cargamos las variables del fichero .env
load_dotenv()
TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")



def MandarMensaje(mensaje):

    if not TOKEN or not CHAT_ID:
        raise ValueError("TOKEN y CHATID deben de tener valor")
    #URL de Telegram para mandar un mensaje
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": mensaje
    }
    response = requests.post(url, json=data)
    print(response.json())
    

mensaje = "Probando puedo mandar mensajes a un canal de telegram"
MandarMensaje(mensaje)

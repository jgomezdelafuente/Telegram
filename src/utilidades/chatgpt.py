from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN_CHATGPT")


# 1. Configura tu cliente (asume que tienes la variable de entorno OPENAI_API_KEY)
client = OpenAI(api_key=TOKEN)

def consultar_agente_legal(rol, contexto, pregunta):
    response = client.chat.completions.create(
        model="gpt-4o", # O "gpt-3.5-turbo" si prefieres algo más económico
        messages=[
            {
                "role": "system", 
                "content": f"Eres un {rol} experto en derecho laboral. Tu tono es formal y técnico."
            },
            {
                "role": "user", 
                "content": f"Contexto del caso: {contexto}\n\nPregunta: {pregunta}"
            }
        ],
        temperature=0.7 # Controla la creatividad (0.2 más preciso, 0.9 más creativo)
    )
    
    return response.choices[0].message.content

# --- EJEMPLO DE USO ---
caso = "Un empleado fue despedido tras 5 años por llegar tarde 3 veces en un mes."
resultado = consultar_agente_legal("Fiscal", caso, "¿Es este despido procedente o nulo?")

print(resultado)
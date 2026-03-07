#Obtener valores de una página web
import requests
import json
from bs4 import BeautifulSoup

def getURL(url):
    response = requests.get(url)
    print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
        #  indica qué motor va a usar BeautifulSoup para analizar (parsear) el HTML
    title = soup.title.text
    print(f"el titulo de la pagina web es: {title}")

getURL("https://www.opositait.com")
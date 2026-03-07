#Paquete que hace un get a un servicio web
import requests
import json
from bs4 import BeautifulSoup

def getChuckNorris():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    #La respuesta generada la formatea en json
    
    if response.status_code == 200:
        data = response.json()    
        print(data["value"])
    else:
        print(f"Error al obtener los datos: {response.status_code}")


def getChuckNorrisJson():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    #La respuesta generada la formatea en json
    
    if response.status_code == 200:
        data = response.json()    
        print(json.dumps(
            data,
            indent=3
        ))
        print(f"el valor de id es: {data["id"]}")
    else:
        print(f"Error al obtener los datos: {response.status_code}")




    
import time
import random
import requests
import threading
from bs4 import BeautifulSoup 

def obtener_precio(symbol):
    time.sleep(8 *random.random())
    url="https://es.finance.yahoo.com/quote/{symbol}"

    header={
            "User-Agent":"Mi proyecto/SP500/1.0"
    }
    response = requests.get(url,headers=header)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text,"html.parser")
        valor=soup.find("span",{"data-testid":"qsp-price"})
        if valor:
            precio = (valor.text.strip())
        else:
            precio = "privado"
        print(f"la accion {symbol} cuesta {precio}")

if __name__ == "__main__":
    with open("clase_3/lista_sp500.txt","r") as f:
        lista_symbolos = eval(f.read())
    
    threads = []

    for symbol in lista_symbolos:
        threads.append(
            threading.Thread(obtener_precio,)
        )
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
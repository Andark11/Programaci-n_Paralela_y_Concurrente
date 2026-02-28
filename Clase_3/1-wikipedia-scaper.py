import requests
from bs4 import BeautifulSoup 
try:
    with open("clase_3.html","r") as f:
        response = f.read()
        print("---------")
    soup = BeautifulSoup(response,"html.parser")
    table = soup.find(id="constituents")
    symbols = []
    for row in table.find_all("tr")[1:]:
        symbols.append(row.find("td").text.strip())
    with open("lista_sp500.txt","w"):
        f.write(str(symbols))
        
except:
    url = "https://en-wikipedia-org.translate.goog/wiki/List_of_S%26P_500_companies?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc"
    header={
        "User-Agent":"Mi proyecto/SP500/1.0"
    }
    response = requests.get(url,headers=header)
    if response.status_code == 200:
        with open("clase_3.html","w") as f:
            f.write(response.text)
    else:
        print("Error")
        print(response.text)
        


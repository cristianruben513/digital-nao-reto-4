# Web Scrapping a la pagina de mercado libre

import requests
from bs4 import BeautifulSoup

url = "https://listado.mercadolibre.com.mx/ps5"

response = requests.get(url)

# Verificar si la petición fue exitosa
soup = BeautifulSoup(response.content, "html.parser")

# Obtener los elementos de la página 
items = soup.find_all("div", class_="ui-search-result__content-wrapper")

for item in items :
  name = item.find("h2", class_="ui-search-item__title").text
  price = item.find("span", class_="andes-money-amount__fraction").text
  print(f"Nombre -> : {name} \nPrecio -> : {price} \n")
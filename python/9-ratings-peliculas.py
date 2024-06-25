import requests

# Tu clave de API de TMDb
api_key = '65706f8d395f8e34c60350a3b99d2996'

# Query de búsqueda (por ejemplo, 'Avengers')
query = 'Avengers'

# URL de la API de TMDb para búsqueda de películas
url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}'

# Realizar la solicitud GET a la API de TMDb
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    # Mostrar resultados de la búsqueda
    for result in data['results']:
        title = result['title']
        release_date = result['release_date']
        rating = result['vote_average']
        print('-----------------------------------------------------------------')
        print(f'Título: {title}')
        print(f'Fecha de estreno: {release_date}')
        print(f'Rating: {rating}')
        print('----------------------------------------------------------------- \n')
else:
    print(f'Error al realizar la búsqueda: {response.status_code}')

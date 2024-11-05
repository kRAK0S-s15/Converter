import requests

BASE_POL_URL = 'https://api.nbp.pl/api/exchangerates/rates/'

def get_pol_currency_today(curency_code):

    url = f"{BASE_POL_URL}c/{curency_code}/today/"

    try:
        responce = requests.get(url)
        responce.raise_for_status()
        data = responce.json()
        return (f"{curency_code}".upper() + f" for today: {data['rates'][0]['ask']} PLN")
    
    except requests.exceptions.RequestException():
        return ('Request error')
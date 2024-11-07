import requests

# national belarusian bank
BASE_BEL_URL = "https://www.nbrb.by/api/exrates/rates/" 

def get_bel_currecy_last(currency_code):

    url = f'{BASE_BEL_URL}{currency_code}?=&parammode=2'

    try:
        responce = requests.get(url)
        responce.raise_for_status()
        data = responce.json()
        price = float(f"{data['Cur_OfficialRate']}")
        return (f"{currency_code} for the last avaible date: {price} BYN"), price
    
    except requests.exceptions.RequestException as e:
        print("Ошибка при обращении к API:", e)

    except KeyError:
        print("Неверный код валюты. Пожалуйста, проверьте и попробуйте снова.")


# national polish bank
BASE_POL_URL = 'https://api.nbp.pl/api/exchangerates/rates/'

def get_pol_currency_last(currency_code):

    url = f"{BASE_POL_URL}c/{currency_code}/last/1/"

    try:
        responce = requests.get(url)
        responce.raise_for_status()
        data = responce.json()
        price = float(next(iter({data['rates'][0]['ask']})))
        return f"{currency_code}".upper() + f" for the last avaible date: {price} PLN", price
    
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return f"No data available for currency code {currency_code}"
        else:
            return f"Request error: {e}"
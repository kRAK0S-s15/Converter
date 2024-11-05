import requests

BASE_BEL_URL = "https://www.nbrb.by/api/exrates/rates/" 

def get_bel_currecy_today(currency_code):

    url = f'{BASE_BEL_URL}{currency_code}?ondate=&parammode=2'

    try:
        responce = requests.get(url)
        responce.raise_for_status()
        data = responce.json()
        return (f"{currency_code} for today: {data['Cur_OfficialRate']} BYN")

    except requests.exceptions.RequestException as e:
        print("Ошибка при обращении к API:", e)
    except KeyError:
        print("Неверный код валюты. Пожалуйста, проверьте и попробуйте снова.")
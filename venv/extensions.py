import json
import requests
import telebot
import logging
from config import API, keys, TOKEN

class APIException(Exception):
    pass

class Convertor:
    @staticmethod
    def get_price(values):
        if len(values) != 3:
            raise APIException("Неверное количество параметров")
        quote, base, amount = values
        if quote == base:
            raise APIException(f"Вы ввели одинаковые валюты: {base}")
        try:
            quote_formatted = keys[quote]
        except KeyError:
            raise APIException(f"Такая валюта не поддерживается: {quote}")
        try:
            base_formatted = keys[base]
        except KeyError:
            raise APIException(f"Такая валюта не поддерживается: {base}")
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"Не корректно введено количество валюты: {amount}")
        query = f'{quote_formatted}_{base_formatted}'
        r = requests.get(f'https://api.exchangerate-api.com/v4/latest/{quote_formatted}',
                            headers={'Authorization': f'Bearer {API}'})
        logging.info('HTML response received:')
        logging.info(r.content)
        try:
            result = (json.loads(r.content)['rates'][base_formatted]) * amount
        except KeyError:
            result = None
            print("Key 'Rub' not found")
        logging.info('Currency conversion result:')
        logging.info(result)
        return round(result, 2)
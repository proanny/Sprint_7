from json import JSONDecodeError

import allure
import requests

from urls import BASE_URL, ORDERS_URL


class OrdersMethods:
    @staticmethod
    @allure.step('Заказать самокат')
    def create_order(payload):
        response = requests.post(f'{BASE_URL}/{ORDERS_URL}', json=payload)

        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text

    @staticmethod
    @allure.step('Получить список заказов')
    def get_orders(payload):
        response = requests.get(f'{BASE_URL}/{ORDERS_URL}', params=payload)

        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text

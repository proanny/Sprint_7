from json import JSONDecodeError

import allure
import requests

from urls import BASE_URL, COURIER_URL


class CourierMethods:
    @staticmethod
    @allure.step('Зарегистрировать курьера')
    def registration(payload):
        response = requests.post(f'{BASE_URL}/{COURIER_URL}', json=payload)

        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text

    @staticmethod
    @allure.step("Авторизовать курьера")
    def login(payload):
        response = requests.post(f'{BASE_URL}/{COURIER_URL}/login', json=payload)

        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text

    @staticmethod
    @allure.step('Удалить курьера')
    def delete_courier(self, courier_id):
        response = requests.delete(f'{BASE_URL}/{COURIER_URL}/{courier_id}')

        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text

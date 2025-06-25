import pytest

from helpers import Helpers
from methods.courier_methods import CourierMethods

@pytest.fixture()
def registration_credentials():
    yield {
        'login': Helpers.generate_random_string(10),
        'password': Helpers.generate_random_string(10),
        'first_name': Helpers.generate_random_string(10),
    }

@pytest.fixture()
def register_courier(registration_credentials):
    result = CourierMethods().registration(registration_credentials)
    yield result, registration_credentials
    if result[1].get('id'):
        CourierMethods().delete_courier()

@pytest.fixture()
def login_courier(register_courier):
    credentials = register_courier[1]
    result = CourierMethods().login(credentials)

    yield result, credentials
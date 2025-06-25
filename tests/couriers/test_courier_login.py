import allure

from helpers import Helpers
from methods.courier_methods import CourierMethods

@allure.feature('Авторизация курьера')
class TestCourierLogin:
    @allure.title('Успешная авторизация курьера')
    def test_courier_can_login(self, login_courier):
        result = login_courier[0]
        assert result[0] == 200
        assert result[1].get('id') is not None

    @allure.title('Успешная авторизация курьера со всеми обязательными полями')
    def test_login_requires_all_fields(self, registration_credentials):
        credentials = {
            'login': registration_credentials.get('login'),
            'password': ''
        }

        result = CourierMethods.login(credentials)
        assert result[0] == 400
        assert result[1] == {'code': 400, 'message': 'Недостаточно данных для входа'}

    @allure.title('Авторизация курьера с некорректным паролем')
    def test_login_wrong_credentials(self, registration_credentials):
        credentials = {
            'login': registration_credentials.get('login'),
            'password': Helpers.generate_random_string(10)
        }
        result = CourierMethods.login(credentials)

        assert result[0] == 404
        assert result[1] == {'code': 404, 'message': 'Учетная запись не найдена'}

    @allure.title('Авторизация несуществующего курьера')
    def test_login_nonexistent_user(self):
        credentials = {'login': Helpers.generate_random_string(10), 'password': Helpers.generate_random_string(10)}
        result = CourierMethods.login(credentials)

        assert result[0] == 404
        assert result[1] == {'code': 404, 'message': 'Учетная запись не найдена'}

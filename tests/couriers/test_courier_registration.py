import allure

from methods.courier_methods import CourierMethods

@allure.feature('Регистрация курьера')
class TestCourierRegistration:
    @allure.title('Успешная регистрация курьера')
    def test_create_courier_success(self, register_courier):
        response = register_courier[0]

        assert response[0] == 201
        assert response[1] == {'ok': True}

    @allure.title('Регистрация существующего курьера')
    def test_create_duplicate_courier(self, register_courier):
        duplicated_credentials = register_courier[1]
        response = CourierMethods.registration(duplicated_credentials)

        assert response[0] == 409
        assert response[1] == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}


    @allure.title('Регистрация курьера без обязательных полей')
    def test_create_courier_missing_required_field(self, registration_credentials):
        credentials = {'login': registration_credentials.get('login')}
        response = CourierMethods.registration(credentials)

        assert response[0] == 400
        assert response[1] == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}


    @allure.title('Регистрация курьера c существующим логином')
    def test_duplicated_courier_login(self, register_courier, registration_credentials):
        credentials = {'login': register_courier[1].get('login'),
                       'password': registration_credentials.get('password')}

        response = CourierMethods.registration(credentials)

        assert response[1] == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
        assert response[0] == 409

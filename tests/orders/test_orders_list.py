import allure
import pytest

from methods.orders_methods import OrdersMethods

@allure.feature('Получение списка заказов самоката')
class TestOrdersList:

    @allure.title('Успешное получение списка заказов самоката')
    def test_get_orders(self,login_courier):
        result = OrdersMethods.get_orders(login_courier[1].get('id'))

        assert result[0] == 200
        assert isinstance(result[1].get('orders'), list) and len(result[1])>0

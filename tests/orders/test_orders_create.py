import allure
import pytest

from data import ORDER_MULTICOLOR, ORDER_TRANSPARENT, ORDER_GRAY_COLOR, ORDER_BLACK_COLOR
from methods.orders_methods import OrdersMethods

@allure.feature('Создание заказа на самокат')
class TestOrdersCreate:
    @allure.title('Успешное создание заказа')
    @pytest.mark.parametrize(
        'order_data',
        [ORDER_GRAY_COLOR, ORDER_BLACK_COLOR]
    )
    def test_create_with_color(self, order_data):
        result = OrdersMethods.create_order(order_data)

        assert result[0] == 201
        assert 'track' in result[1]

    @allure.title('Успешное создание заказа со всеми цветами самоката')
    def test_create_with_all_colors(self):
        result = OrdersMethods.create_order(ORDER_MULTICOLOR)

        assert result[0] == 201
        assert 'track' in result[1]

    @allure.title('Успешное создание заказа со без цветов самоката')
    def test_create_without_colors(self):
        result = OrdersMethods.create_order(ORDER_TRANSPARENT)

        assert result[0] == 201
        assert 'track' in result[1]

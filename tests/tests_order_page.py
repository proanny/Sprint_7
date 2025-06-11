import allure
import pytest

from data import OrderData
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.title('Тесты создания заказа')
class TestsOrderPage:
    @pytest.mark.parametrize(
        'locator, order_data',
        [
            (MainPageLocators.ORDER_BUTTON_TOP, OrderData.DATA[0]),
            (MainPageLocators.ORDER_BUTTON_BOTTOM, OrderData.DATA[1])
        ]
    )
    def test_create_order(self, driver, locator, order_data):
        main_page = MainPage(driver)
        main_page.scroll_to_element(locator)
        main_page.click_to_element(locator)
        order_page = OrderPage(driver)
        order_page.set_customer_data(order_data)
        order_page.click_next_button()
        order_page.set_order_data(order_data)
        order_page.click_to_create_order()
        order_page.click_to_confirm_create_order()
        assert order_page.check_create_order()



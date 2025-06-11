import allure
from selenium.webdriver import Keys

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Заполнение первой части формы с информацией о заказчике')
    def set_customer_data(self, data):
        self.add_text_to_element(OrderPageLocators.CUSTOMER_NAME, data.get('name'))
        self.add_text_to_element(OrderPageLocators.CUSTOMER_SURNAME, data.get('surname'))
        self.add_text_to_element(OrderPageLocators.CUSTOMER_ADDRESS, data.get('address'))
        self.click_to_element(OrderPageLocators.CUSTOMER_METRO)
        self.click_to_element(self.format_locators(OrderPageLocators.CUSTOMER_METRO_OPTION, data.get('metro_option')))
        self.add_text_to_element(OrderPageLocators.CUSTOMER_PHONE_NUMBER, data.get('phone_number'))

    @allure.step('Заполнение второй части формы с информацией о заказе')
    def set_order_data(self, data):
        self.add_text_to_element(OrderPageLocators.ORDER_START_DATE, data.get('date'))
        self.find_element_with_wait(OrderPageLocators.ORDER_START_DATE,).send_keys(Keys.RETURN)
        self.click_to_element(OrderPageLocators.ORDER_DAYS)
        self.click_to_element(self.format_locators(OrderPageLocators.ORDER_DAYS_OPTION, data.get('days')))
        self.click_to_element(self.format_locators(OrderPageLocators.ORDER_SCOOTER_COLOR_OPTION, data.get('color')))
        self.add_text_to_element(OrderPageLocators.ORDER_COMMENT, data.get('comment'))

    @allure.step('Клик на кнопку Далее')
    def click_next_button(self):
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Клик на кнопку создания заказа')
    def click_to_create_order(self):
        self.click_to_element(OrderPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Клик на кнопку подтверждения создания заказа')
    def click_to_confirm_create_order(self):
        self.click_to_element(OrderPageLocators.CONFIRM_CREATE_ORDER_BUTTON)

    @allure.step('Проверка появления модального окна об успешном создании заказа')
    def check_create_order(self):
        return self.find_element_with_wait(OrderPageLocators.ORDER_SUCCESS_CREATE_MODAL)
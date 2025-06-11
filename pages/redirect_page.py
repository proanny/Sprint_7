import allure

from data import UrlForTests
from locators.main_page_locators import MainPageLocators
from locators.redirect_page_locators import RedirectPageLocators
from pages.base_page import BasePage


class RedirectPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_url(UrlForTests.URL_MAIN_PAGE)

    @allure.step('Клик на лого Самокат')
    def click_to_scooter_logo(self):
        self.click_to_element(RedirectPageLocators.SCOOTER_LOGO)

    @allure.step('Клик на лого Яндекс')
    def click_to_yandex_logo(self):
        self.click_to_element(RedirectPageLocators.YANDEX_LOGO)

    @allure.step('Проверка редиректа на главную страницу Яндекс.Самокат')
    def check_redirect_to_main_page(self):
        return self.find_element_with_wait(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step('Проверка редиректа на главную страницу Яндекс.Дзен')
    def check_redirect_to_dzen(self):
        self.go_to_last_browser_tab(driver)
        return self.find_element_with_wait(RedirectPageLocators.DZEN_LOCATOR)


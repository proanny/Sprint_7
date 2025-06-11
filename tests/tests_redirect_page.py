import allure

from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.redirect_page import RedirectPage



class TestsRedirectPage:

    @allure.title('Тест перехода на главную страницу Яндекс.Самокат')
    def test_redirect_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_element(MainPageLocators.ORDER_BUTTON_TOP)
        redirect_page = RedirectPage(driver)
        redirect_page.click_to_scooter_logo()
        assert redirect_page.check_redirect_to_main_page

    @allure.title('Тест перехода на главную страницу Яндекс.Дзен')
    def test_redirect_to_dzen_page(self, driver):
        redirect_page = RedirectPage(driver)
        redirect_page.click_to_yandex_logo()
        assert redirect_page.check_redirect_to_dzen



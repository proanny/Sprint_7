import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data import UrlForTests

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_url(UrlForTests.URL_MAIN_PAGE)

    @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        locator_question_formated = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.click_to_element(locator_question_formated)

    @allure.step('Получение текста ответа на вопрос')
    def get_answer_text(self, num):
        locator_answer_formated = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(locator_answer_formated)



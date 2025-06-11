import allure
import pytest

from data import Answers
from pages.main_page import MainPage


@allure.title('Тесты на соответствие вопросов и ответов')
class TestMainPage:
    @pytest.mark.parametrize(
        'num',
        [0,1,2,3,4,5,6,7])
    def test_questions_and_answers(self, driver, num):
        main_page = MainPage(driver)
        main_page.click_to_question(num)
        assert main_page.get_answer_text(num) == Answers.answers_texts[num]


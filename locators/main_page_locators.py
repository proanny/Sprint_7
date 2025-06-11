from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTION_LOCATOR =  By.XPATH, ".//*[@id='accordion__heading-{}']"
    ANSWER_LOCATOR =  By.XPATH, ".//*[@id='accordion__panel-{}']"
    QUESTION_LOCATOR_TO_SCROLL = By.XPATH, ".//*[@id='accordion__heading-7']"

    ORDER_BUTTON_TOP = By.XPATH, ".//div[starts-with(@class, 'Header_Nav')]//button[text()='Заказать']"
    ORDER_BUTTON_BOTTOM = By.XPATH, ".//div[starts-with(@class, 'Home_FinishButton')]//button[text()='Заказать']"

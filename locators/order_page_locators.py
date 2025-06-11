from selenium.webdriver.common.by import By


class OrderPageLocators:

    CUSTOMER_FORM = By.XPATH, ".//*[starts-with(@class, 'Order_Form')]"
    CUSTOMER_NAME = By.XPATH, ".//input[@placeholder = '* Имя']"
    CUSTOMER_SURNAME = By.XPATH, ".//input[@placeholder = '* Фамилия']"
    CUSTOMER_ADDRESS = By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']"
    CUSTOMER_METRO = By.XPATH, ".//input[@placeholder = '* Станция метро']"
    CUSTOMER_METRO_OPTION = By.XPATH, ".//li[contains(@class, 'select-search__row')]//*[text()='{}']"
    CUSTOMER_PHONE_NUMBER = By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']"

    NEXT_BUTTON = By.XPATH, ".//button[text()='Далее']"

    ORDER_START_DATE = By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']"
    ORDER_DAYS = By.XPATH, ".//*[starts-with(@class, 'Dropdown-placeholder')][text()='* Срок аренды']/parent::*[@class='Dropdown-control']"
    ORDER_DAYS_OPTION = By.XPATH, ".//*[contains(@class, 'Dropdown-option')][text() = '{}']"
    ORDER_SCOOTER_COLOR_OPTION = By.XPATH, ".//label[@for='{}']"
    ORDER_COMMENT = By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']"

    CREATE_ORDER_BUTTON = By.XPATH, ".//*[starts-with(@class, 'Order_Buttons')]//button[text()='Заказать']"

    CONFIRM_CREATE_ORDER_BUTTON = By.XPATH, ".//*[starts-with(@class, 'Order_Modal')]//button[text()='Да']"
    ORDER_SUCCESS_CREATE_MODAL = By.XPATH, ".//*[starts-with(@class, 'Order_Modal')]//*[text()='Заказ оформлен']"




from selenium.webdriver.common.by import By


class RedirectPageLocators:

    SCOOTER_LOGO = By.XPATH, ".//a[starts-with(@class, 'Header_LogoScooter')]"
    YANDEX_LOGO = By.XPATH, ".//a[starts-with(@class, 'Header_LogoYandex')]"

    DZEN_LOCATOR = By.XPATH, ".//a[@data-testid='logo']"
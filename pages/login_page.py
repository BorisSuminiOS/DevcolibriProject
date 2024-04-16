import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger


class LoginPage(Base):

    url = 'https://joomla.devcolibri.com/login'

    # Locations

    pole_login = 'input[id="username"]'
    pole_password = 'input[id="password"]'
    button_enter = '//*[@id="com-users-login__form"]/fieldset/div[5]/div/button'
    text_main_page = '//*[@id="content-wrapper"]/div[1]/div/div/div[1]/div/h1'


    # Getters
    def get_pole_login(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.pole_login)))

    def get_pole_password(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.pole_password)))

    def get_button_enter(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.button_enter)))


    def get_text_main_page(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.text_main_page))).text


    # Actions

    def input_get_pole_login(self, login):
        self.get_pole_login().send_keys(login)
        print('Input login')

    def input_get_pole_password(self, password):
        self.get_pole_password().send_keys(password)
        print('Input password')

    def click_button_enter(self):
        self.get_button_enter().click()
        print('Click button enter')

    # Methods
    def authorization(self):
        with allure.step("Authorization"):
            Logger.add_start_step(method='authorization')
            '''Авторизация пользователя'''
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_get_pole_login('test_user2024')
            self.input_get_pole_password('qwerty123456')
            self.click_button_enter()
            self.method_assert_word('Android для разработчиков', self.get_text_main_page())
            self.separator_tests()
            Logger.add_end_step(self.driver.current_url, method='authorization')
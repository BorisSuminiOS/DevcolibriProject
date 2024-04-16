import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger


class RegistrationPage(Base):

    url = 'https://joomla.devcolibri.com/login?view=registration'

    # Locations

    pole_user_name = 'input[id="jform_name"]'
    pole_login = 'input[id="jform_username"]'
    pole_password = 'input[id="jform_password1"]'
    pole_confirmation_password = 'input[id="jform_password2"]'
    pole_email = 'input[id="jform_email1"]'
    button_registration = '//*[@id="member-registration"]/div/div/button'
    text_successful_registration = '//*[@id="system-message-container"]/joomla-alert/div[2]/div'
    text = 'Ваша учетная запись создана. Теперь вы можете войти в систему, используя логин и пароль, введенные при регистрации.'

    # Getters
    def get_pole_user_name(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.pole_user_name)))

    def get_pole_login(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.pole_login)))

    def get_pole_password(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.pole_password)))

    def get_pole_confirmation_password(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.pole_confirmation_password)))

    def get_pole_email(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.pole_email)))

    def get_button_registration(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.button_registration)))


    def get_text_successful_registration(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.text_successful_registration))).text

    # Actions

    def input_pole_user_name(self, user_name):
        self.get_pole_user_name().send_keys(user_name)
        print('Input user name')

    def input_pole_login(self, login):
        self.get_pole_login().send_keys(login)
        print('Input login')

    def input_pole_password(self, password):
        self.get_pole_password().send_keys(password)
        print('Input password')

    def input_pole_confirmation_password(self, confirmation_password):
        self.get_pole_confirmation_password().send_keys(confirmation_password)
        print('Input confirmation password')

    def input_pole_email(self, email):
        self.get_pole_email().send_keys(email)
        print('Input email')

    def click_button_registration(self):
        self.get_button_registration().click()
        print('Click button registration')

    # Methods

    def registration(self):
        with allure.step("Registration"):
            '''Регистрация пользователя'''
            Logger.add_start_step(method='registration')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_pole_user_name('Александр')
            self.input_pole_login('test_user2024')
            self.input_pole_password('qwerty123456')
            self.input_pole_confirmation_password('qwerty123456')
            self.input_pole_email('test_user2024@mail.ru')
            self.click_button_registration()
            self.method_assert_word(self.text, self.get_text_successful_registration())
            self.to_screenshot('registration')
            self.separator_tests()
            Logger.add_end_step(url=self.driver.current_url, method='registration')
            self.driver.close()



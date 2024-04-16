import allure
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger


class EditProfilePage(Base):
    # data_user

    faker = Faker('en_US')

    name = faker.first_name()
    email = faker.email()
    phone_number = faker.phone_number()

    # Locations

    pole_new_name = 'input[name="jform[name][new]"]'
    pole_new_email = 'input[name="jform[email][new]"]'
    pole_new_phone = 'input[name="jform[phone][new]"]'
    button_update_name = 'a[onclick="RadicalMartExpressSettingsUpdate_name(this)"]'
    button_update_email = 'a[onclick="RadicalMartExpressSettingsUpdate_email(this)"]'
    button_update_phone = 'a[onclick="RadicalMartExpressSettingsUpdate_phone(this)"]'

    # Getters

    def get_pole_new_name(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.pole_new_name)))

    def get_pole_new_email(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.pole_new_email)))

    def get_pole_new_phone(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.pole_new_phone)))

    def get_button_update_name(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_update_name)))

    def get_button_update_email(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_update_email)))

    def get_button_update_phone(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_update_phone)))



    # Actions

    def input_pole_new_name(self, name):
        self.get_pole_new_name().send_keys(name)
        print('Input new name')

    def input_pole_new_email(self, email):
        self.get_pole_new_email().send_keys(email)
        print('Input email')

    def input_pole_new_phone(self, phone):
        self.get_pole_new_phone().send_keys(phone)
        print('Input phone')

    def click_button_update_name(self):
        self.get_button_update_name().click()
        print('Click button update name')

    def click_button_update_email(self):
        self.get_button_update_email().click()
        print('Click button update email')

    def click_button_update_phone(self):
        self.get_button_update_phone().click()
        print('Click button update phone')

    # Methods

    def edit_profile(self):
        with allure.step("Edit_profile"):
            Logger.add_start_step(method='edit_profile')
            '''Редактировать профиль'''
            self.get_current_url()
            self.input_pole_new_name(self.name)
            self.click_button_update_name()
            self.input_pole_new_email(self.email)
            self.click_button_update_email()
            self.input_pole_new_phone(self.phone_number)
            self.click_button_update_phone()
            self.to_screenshot('edit_profile')
            self.separator_tests()
            Logger.add_end_step(self.driver.current_url, method='edit_profile')
            self.driver.close()

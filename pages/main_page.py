import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):

    url = 'https://joomla.devcolibri.com/'

    # Locations

    button_courses = '//*[@id="nav-rail-content"]/ul/li[5]/div/a[1]/div/div/div'
    text_courses = '//*[@id="content-wrapper"]/div[1]/main/div/div[1]/div[1]/h1'
    button_my_courses = '//*[@id="nav-rail-content"]/ul/li[6]/div/a/div/div/div'
    button_user = '//*[@id="content-wrapper"]/header/nav/div/div/div/button/div'
    button_edit_profile = '//*[@id="content-wrapper"]/header/nav/div/div/div/div/ul/li[1]/a/div'
    text_settings = '//*[@id="RadicalMart"]/h1'

    # Getters

    def get_button_courses(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.button_courses)))

    def get_text_courses(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.text_courses))).text

    def get_button_my_courses(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.button_my_courses)))


    def get_button_user(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.button_user)))

    def get_button_edit_profile(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.button_edit_profile)))

    def get_text_settings(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.text_settings))).text

    # Actions
    def click_button_courses(self):
        self.get_button_courses().click()
        print('Click button courses')

    def click_button_my_courses(self):
        self.get_button_my_courses().click()
        print('Click button my courses')

    def click_button_user(self):
        self.get_button_user().click()
        print('Click button user')

    def click_button_edit_profile(self):
        self.get_button_edit_profile().click()
        print('Click button edit profile')

    # Methods

    def the_courses_section(self):
        with allure.step("The_courses_section"):
            Logger.add_start_step(method='the_courses_section')
            '''Перейти в раздел курсы'''
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_button_courses()
            self.method_assert_word('Курсы', self.get_text_courses())
            self.separator_tests()
            Logger.add_end_step(self.driver.current_url, method='the_courses_section')

    def my_courses_section(self):
        with allure.step("My_courses_section"):
            Logger.add_start_step(method='my_courses_section')
            '''Перейти в раздел мои курсы'''
            self.get_current_url()
            self.click_button_my_courses()
            self.separator_tests()
            Logger.add_end_step(self.driver.current_url, method='my_courses_section')

    def the_courses_section_2(self):
        with allure.step("The_courses_section_2"):
            Logger.add_start_step(method='the_courses_section_2')
            '''Перейти в раздел курсы'''
            self.get_current_url()
            self.click_button_courses()
            self.method_assert_word('Курсы', self.get_text_courses())
            self.separator_tests()
            Logger.add_end_step(self.driver.current_url, method='the_courses_section_2')

    def edit_profile_section(self):
        with allure.step("Edit_profile_section"):
            Logger.add_start_step(method='edit_profile_section')
            '''Перейти в раздел Редактировать профиль'''
            self.get_current_url()
            self.click_button_user()
            self.click_button_edit_profile()
            self.method_assert_word('Настройки', self.get_text_settings())
            self.separator_tests()
            Logger.add_end_step(self.driver.current_url, method='edit_profile_section')
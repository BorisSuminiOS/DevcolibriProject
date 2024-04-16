import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger


class CoursesPage(Base):

    # Locations

    button_course_java1_java2 = '//*[@id="content-wrapper"]/div[1]/main/div/div[2]/div[6]/article/div[1]/div[1]/div[1]/a'
    text_java1_java2 = '//*[@id="content-wrapper"]/div[1]/main/div/div[1]/div[1]/hgroup/h1'
    button_android1_java1 = 'a[title="Курс Android разработка: Базовый курс + Основы программирования"]'
    text_android1_java1 = '//*[@id="content-wrapper"]/div[1]/main/div/div[1]/div[1]/hgroup/h1'

    # Getters
    def get_button_course_java1_java2(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.button_course_java1_java2)))

    def get_text_java1_java2(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.text_java1_java2))).text

    def get_button_android1_java1(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_android1_java1)))

    def get_text_android1_java1(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.text_android1_java1))).text


    # Actions

    def click_button_course_java1_java2(self):
        self.get_button_course_java1_java2().click()
        print('Click button course java1-java2')

    def click_button_android1_java1(self):
        self.get_button_android1_java1().click()
        print('Click button course java1-java2')

    # Methods
    def choose_course_java1_java2(self):
        with allure.step("Choose_course_java1_java2"):
            Logger.add_start_step(method='choose_course_java1_java2')
            '''Выбрать курс Java1-Java2'''
            self.get_current_url()
            self.apply_scroll(0,700)
            self.click_button_course_java1_java2()
            self.method_assert_word('Java с нуля до Junior + Подготовка к собеседованию', self.get_text_java1_java2())
            self.separator_tests()
            Logger.add_end_step(self.driver.current_url, method='choose_course_java1_java2')

    def choose_course_android1_java1(self):
        with allure.step("Choose_course_android1_java1"):
            Logger.add_start_step(method='choose_course_android1_java1')
            '''Выбрать курс Android1-Java1'''
            self.get_current_url()
            self.apply_scroll(0,700)
            self.click_button_android1_java1()
            self.method_assert_word('Android разработка: Базовый курс + Основы программирования', self.get_text_java1_java2())
            self.separator_tests()
            Logger.add_end_step(self.driver.current_url, method='choose_course_android1_java1')


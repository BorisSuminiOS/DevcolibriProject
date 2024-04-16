import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger


class MyCoursesPage(Base):

    # Locations

    course_java1_java2 = '//span[contains(text(),"Java c нуля + Java продвинутый уровень")]'
    course_android1_java1 = '//span[contains(text(),"Android с нуля + Java с нуля")]'

    # Getters

    def get_course_java1_java2(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.course_java1_java2))).text

    def get_course_android1_java1(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.course_android1_java1))).text


    # Methods

    def course_availability_1(self):
        with allure.step("Course_availability_1"):
            Logger.add_start_step(method='course_availability_1')
            '''Проверить наличие купленного курса java1-java2'''
            self.get_current_url()
            self.method_assert_word('Java c нуля + Java продвинутый уровень', self.get_course_java1_java2())
            self.to_screenshot('new_course_1')
            self.separator_tests()
            Logger.add_end_step(self.driver.current_url, method='course_availability_1')
            self.driver.close()

    def course_availability_2(self):
        with allure.step("Course_availability_2"):
            Logger.add_start_step(method='course_availability_2')
            '''Проверить наличие купленного курса android1-java1'''
            self.get_current_url()
            self.method_assert_word('Android с нуля + Java с нуля', self.get_course_android1_java1())
            self.to_screenshot('new_course_2')
            self.separator_tests()
            Logger.add_end_step(self.driver.current_url, method='course_availability_2')
            self.driver.close()





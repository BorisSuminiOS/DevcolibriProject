import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.android1_java1_page import Android1Java1Page
from pages.courses_page import CoursesPage
from pages.java1_java2_page import Java1Java2Page
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.my_courses_page import MyCoursesPage
from pages.payment_page import PaymentPage


@allure.description('Покупка курса Java1-Java2, пользователь не авторизован')
def test_buy_course_1():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    mp = MainPage(driver)
    mp.the_courses_section()

    cp = CoursesPage(driver)
    cp.choose_course_java1_java2()

    jp = Java1Java2Page(driver)
    jp.making_order_java1_java2()

    pp = PaymentPage(driver)
    pp.payment_course_java1_java2()


@allure.description('Проверка купленного курса java1-java2')
def test_check_purchased_course_1():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    lp = LoginPage(driver)
    lp.authorization()

    mp = MainPage(driver)
    mp.my_courses_section()

    mcp = MyCoursesPage(driver)
    mcp.course_availability_1()


@allure.description('Покупка курса Android1-Java1, пользователь авторизован')
def test_buy_course_2():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    lp = LoginPage(driver)
    lp.authorization()

    mp = MainPage(driver)
    mp.the_courses_section_2()

    cp = CoursesPage(driver)
    cp.choose_course_android1_java1()

    ajp = Android1Java1Page(driver)
    ajp.making_order_android1_java1()

    pp = PaymentPage(driver)
    pp.payment_course_android1_java1()


@allure.description('Проверка купленного курса android1-java1')
def test_check_purchased_course_2():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    lp = LoginPage(driver)
    lp.authorization()

    mp = MainPage(driver)
    mp.my_courses_section()

    mcp = MyCoursesPage(driver)
    mcp.course_availability_2()


# python -m pytest --alluredir=test_results/tests/tests_devcolibri





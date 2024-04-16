from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.registration_page import RegistrationPage
import allure


@allure.description('Регистрация нового пользователя')
def test_registration():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    rp = RegistrationPage(driver)
    rp.registration()
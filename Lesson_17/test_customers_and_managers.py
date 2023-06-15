import allure
import pytest
from selenium.common import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

SOURCE_LINK_LOGIN = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'


@allure.story('Customers login test')
class TestCustomerLogin:

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(SOURCE_LINK_LOGIN)

    def teardown(self):
        self.driver.quit()

    def search_element(self, by, selector):
        wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException])
        return wait.until(EC.element_to_be_clickable((by, selector)))

    @allure.title('customer login test')
    @allure.description('Test each customer login')
    @pytest.mark.parametrize("customer_name",
                             [('Hermoine Granger'), ('Harry Potter'), ('Ron Weasly'), ("Albus Dumbledore"),
                              ("Neville Longbottom")])
    def test_customer_login(self, customer_name):
        select_customer_login_option = self.search_element(By.XPATH, "//button[@ng-click='customer()']")
        select_customer_login_option.click()

        user_select_dropdown = self.search_element(By.XPATH, '//*[@id="userSelect"]')
        user_select_dropdown.click()

        customer_option = self.search_element(By.XPATH, f'//*[@id="userSelect"]/option[text()="{customer_name}"]')
        customer_option.click()

        assert customer_option.text == customer_name

        customer_login = self.search_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button')
        customer_login.click()

        welcome_user_name = self.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/strong/span')
        assert welcome_user_name.text == customer_name


@allure.story('Manager login test')
class TestBankManagerLogin:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(SOURCE_LINK_LOGIN)

    def teardown_method(self):
        self.driver.quit()

    def search_element(self, by, selector):
        wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException])
        return wait.until(EC.element_to_be_clickable((by, selector)))

    @allure.title('Customer adding test')
    @allure.description('Test adding of a new customer')
    def test_add_customer(self):
        select_manager_login = self.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button')
        select_manager_login.click()

        add_customer = self.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[1]')
        add_customer.click()

        name_input = self.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/input')
        name_input.send_keys('Severus')

        surname_input = self.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/input')
        surname_input.send_keys('Snape')

        postal_code_input = self.search_element(By.XPATH,
                                                '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/input')
        postal_code_input.send_keys('AD523-HA')

        submit_profile = self.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button')
        submit_profile.submit()

        assert self.driver.switch_to.alert.text == "Customer added successfully with customer id :6"

    @allure.title('Open customer profile test')
    @allure.description('Test the opening of each customer profile')
    @pytest.mark.parametrize("customer_name",
                             [('Hermoine Granger'), ('Harry Potter'), ('Ron Weasly'), ("Albus Dumbledore"),
                              ("Neville Longbottom")])
    @pytest.mark.parametrize("currency", ['Dollar', 'Pound', 'Rupee'])
    def test_open_account(self, customer_name, currency):
        select_manager_login = self.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button')
        select_manager_login.click()

        open_account = self.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[2]')
        open_account.click()

        select_customer = self.search_element(By.XPATH, f'//*[@id="userSelect"]/option[text()="{customer_name}"]')
        select_customer.click()

        select_currency = self.search_element(By.XPATH, '//*[@id="currency"]')
        select_currency.click()

        select_currency_dollar = self.search_element(By.XPATH, f'//*[@id="currency"]/option[text()="{currency}"]')
        select_currency_dollar.click()

        submit_actions = self.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button')
        submit_actions.submit()

        alert = self.driver.switch_to.alert
        alert.accept()

    @allure.title('Customer deletion test')
    @allure.description('Test deleting of a customer')
    def test_delete_customer(self):
        select_manager_login = self.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button')
        select_manager_login.click()

        open_customers_list = self.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[3]')
        open_customers_list.click()

        existed_customer = self.search_element(By.XPATH,
                                               '/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr[5]/td[1]')
        customer_name = existed_customer.text
        assert customer_name == 'Neville'

        self.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr[4]/td[5]/button'
                            ).click()

    @allure.title('Search for a customer test')
    @allure.description('Test searching for a customer')
    def test_search_for_customer(self):
        select_manager_login = self.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button')
        select_manager_login.click()

        customers_tab_activate = self.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[3]')
        customers_tab_activate.click()

        search_input_activate = self.search_element(By.XPATH,
                                                    '/html/body/div/div/div[2]/div/div[2]/div/form/div/div/input')
        search_input_activate.click()
        search_input_activate.send_keys('Ron')

        searched_user = search_input_activate.get_attribute('value')

        assert searched_user == 'Ron'

    @allure.title('Return homepage test')
    @allure.description('Test returning to the homepage')
    def test_return_to_home_page(self):
        select_manager_login = self.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button')
        select_manager_login.click()

        customers_tab_activate = self.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[3]')
        customers_tab_activate.click()

        return_to_home_page = self.search_element(By.XPATH, '/html/body/div/div/div[1]/button[1]')
        return_to_home_page.click()

        current_url = self.driver.current_url
        expected_url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
        assert current_url == expected_url

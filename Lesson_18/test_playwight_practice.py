import pytest
from playwright.sync_api import Page

URL_1 = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
URL_2 = 'https://www.saucedemo.com/v1/'


@pytest.mark.parametrize("customer_name",
                         [('Hermoine Granger'), ('Harry Potter'), ('Ron Weasly'), ("Albus Dumbledore"),
                          ("Neville Longbottom")])
def test_page_title_and_username(page: Page, customer_name):
    page.goto(URL_1)
    assert page.title() == 'XYZ Bank'

    page.click("//button[@ng-click='customer()']")
    page.click('//*[@id="userSelect"]')
    assert page.inner_text(f'//*[@id="userSelect"]/option[text()="{customer_name}"]') == customer_name


def test_standard_user_login_and_adding_items_to_the_cart(page: Page):
    page.goto(URL_2)
    page.fill('[id = "user-name"]', 'standard_user')
    page.fill('[id = "password"]', 'secret_sauce')
    page.click('[id = "login-button"]')

    """ Check the page title """
    assert page.title() == 'Swag Labs'
    page.screenshot(path="screenshot.png")

    add_to_cart = '//*[@id="inventory_container"]/div/div[1]/div[3]/button'
    remove_from_cart = '//*[@id="inventory_container"]/div/div[1]/div[3]/button'

    """ Check button name changing into 'REMOVE' after adding item to the cart"""
    page.click(add_to_cart)
    remove_button = page.query_selector(add_to_cart)

    cart_sign = page.query_selector('//*[@id="shopping_cart_container"]/a/span')

    assert cart_sign.text_content() == '1'

    assert remove_button.text_content() == 'REMOVE'

    """ Check button name changing into 'ADD TO CART' after removing item from the cart"""
    page.click(remove_from_cart)
    return_to_add_to_cart = page.query_selector(remove_from_cart)

    assert return_to_add_to_cart.text_content() == 'ADD TO CART'

    cart_sign = page.query_selector('//*[@id="shopping_cart_container"]/a/span')

    assert cart_sign is None


def test_locked_out_user_logon(page: Page):
    page.goto(URL_2)
    page.fill('[id = "user-name"]', 'locked_out_user')
    page.fill('[id = "password"]', 'secret_sauce')
    page.click('[id = "login-button"]')

    error_message = '//h3'
    return_error_message = page.query_selector(error_message)

    assert return_error_message.text_content() == 'Epic sadface: Sorry, this user has been locked out.'



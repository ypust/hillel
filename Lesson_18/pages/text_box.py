import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='session')
def playwright():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        yield playwright, browser, context, page
        page.close()
        context.close()
        browser.close()


class TextBox:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://demoqa.com/text-box")

    def enter_full_name(self, full_name):
        self.page.locator("[id=userName]").fill(full_name)

    def enter_email(self, email):
        self.page.locator("[id=userEmail]").fill(email)

    def enter_current_address(self, currant_address):
        self.page.locator('[id=currentAddress]').fill(currant_address)

    def enter_permanent_address(self, permanent_address):
        self.page.locator("#permanentAddress").fill(permanent_address)

    def submit_form(self):
        self.page.locator("[id=submit]").click()

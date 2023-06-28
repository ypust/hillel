import pytest
from playwright.sync_api import sync_playwright
import allure


@allure.story('Test Text Box')
@pytest.fixture(scope='session')
def playwright():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture
def browser(playwright):
    browser = playwright.chromium.launch(headless=True)
    yield browser
    browser.close()


@pytest.fixture
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()


# class StudentRegistrationForm:
#     def __init__(self, page):
#         self.page = page
#
#     def navigate(self):
#         self.page.goto("https://demoqa.com/automation-practice-form")
#
#     def enter_user_name(self, name, lastname):
#         self.page.locator('input[id="firstName"]').fill(name)
#         self.page.locator('input[id="lastName"]').fill(lastname)
#
#     def enter_email(self, email):
#         self.page.locator('input[id="userEmail"]').fill(email)
#
#     def enter_gender(self, gender):
#         self.page.locator(f'input[type="radio"][value="{gender}"]').check()
#
#     def enter_mobile(self, tel_number):
#         self.page.fill('input[id="userNumber"]', tel_number)
#
#     def set_date_of_birth(self, day, month, year):
#         self.page.locator("[id=dateOfBirthInput]").click()
#         month_combobox = self.page.locator("div").filter(has_text=re.compile(
#             r"^JanuaryFebruaryMarchAprilMayJuneJulyAugustSeptemberOctoberNovemberDecember$")).get_by_role(
#             "combobox")
#         month_combobox.select_option(month)
#
#         year_combobox = self.page.locator("div").filter(has_text=str(year))
#         year_combobox_elements = year_combobox.query_all('select')
#         year_combobox_element = year_combobox_elements[1]
#         year_combobox_element.select_option(str(year))
#
#         day_gridcell = self.page.locator("div").filter(has_text=re.compile(rf"^\b{day}\b")).get_by_role("gridcell")
#         day_gridcell.click()
#
#     def set_subjects(self, subject):
#         self.page.locator("#subjectsInput").fill(subject)
#         self.page.get_by_text(subject, exact=True).click()
#
#     def set_hobbies(self, hobby):
#         self.page.get_by_text(hobby).click()
#
#     def set_current_address(self, address):
#         self.page.querySelector('[id="currentAddress"]').fill(address)


# def test_fill_registration_form(page):
#     student_registration_form = StudentRegistrationForm(page)
#     student_registration_form.navigate()
#     student_registration_form.enter_user_name("John", "Doe")
#     student_registration_form.enter_email("johndoe@example.com")
#     # student_registration_form.enter_gender("Male")
#     student_registration_form.enter_mobile("1234567890")
#     student_registration_form.set_date_of_birth("15", "June", "1990")
#     student_registration_form.set_subjects("Computer Science")
#     student_registration_form.set_hobbies("Sports")
#     student_registration_form.set_current_address("123 ABC Street, City")
#
#     # Assert that the form is filled correctly
#     assert student_registration_form.page.query_selector('input[id="firstName"]').get_attribute("value") == "John"
#     assert student_registration_form.page.query_selector('input[id="lastName"]').get_attribute("value") == "Doe"
#     assert student_registration_form.page.query_selector('input[id="userEmail"]').get_attribute(
#         "value") == "johndoe@example.com"
#     assert student_registration_form.page.query_selector('input[type="radio"][value="Male"]').is_checked()
#     assert student_registration_form.page.query_selector('input[id="userNumber"]').get_attribute(
#         "value") == "1234567890"


class TextBox:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://demoqa.com/")

    def go_to_elements_tab(self):
        self.page.goto('https://demoqa.com/elements')

    def open_text_box(self):
        self.page.get_by_role("list").get_by_text("Text Box").click()

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


@allure.title('Test user form filling all fields')
@allure.description('Test user can fill the form with all fields filled')
def test_user_form_filling_all_fields(page):
    user_form = TextBox(page)
    user_form.navigate()
    user_form.go_to_elements_tab()
    user_form.open_text_box()
    user_form.enter_full_name('User Test')
    user_form.enter_email('test.mail@example.com')
    user_form.enter_current_address('Lipowa, 25')
    user_form.enter_permanent_address('Street, 84')
    user_form.submit_form()

    entered_name = page.locator("[id=name]").text_content()[5:]
    entered_email = page.locator("[id=email]").text_content()[6:]

    assert entered_name == 'User Test'
    assert entered_email == 'test.mail@example.com'


class WebTables:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://demoqa.com/")

    def go_to_elements_tab(self):
        self.page.goto('https://demoqa.com/elements')

    def open_web_tables_tab(self):
        self.page.get_by_role("list").locator('[id=item-3]').click()

    def add_new_user(self, first_name, last_name, email, age, salary, department):
        self.page.locator('[id=addNewRecordButton]').click()
        self.page.locator('[id=firstName]').fill(first_name)
        self.page.locator('[id=lastName]').fill(last_name)
        self.page.locator('[id=userEmail]').fill(email)
        self.page.locator('[id=age]').fill(age)
        self.page.locator('[id=salary]').fill(salary)
        self.page.locator('[id=department]').fill(department)

    def submit_application(self):
        self.page.locator('[id=submit]').click()

    def search_for_user(self, user_name):
        self.page.locator('[id=searchBox]').fill(user_name)

    def edit_user(self, first_name, last_name, email, age, salary, department):
        self.page.locator('[id="edit-record-1"]').click()
        self.page.locator('[id=addNewRecordButton]').click()
        self.page.locator('[id=firstName]').fill(first_name)
        self.page.locator('[id=lastName]').fill(last_name)
        self.page.locator('[id=userEmail]').fill(email)
        self.page.locator('[id=age]').fill(age)
        self.page.locator('[id=salary]').fill(salary)
        self.page.locator('[id=department]').fill(department)

    def delete_user_from_search_result(self):
        self.page.get_by_title("Delete").get_by_role("img").click()

    def delete_user_from_the_table(self, first_name, last_name, age, email, salary, department):
        self.page.get_by_role("row",
                              name=f"{first_name} {last_name} {age} {email} {salary} {department} Edit Delete").get_by_title(
            "Delete").locator("path").click()


@allure.title('Test adding a new user')
@allure.description('Test user can add a new user')
def test_adding_new_user(page):
    user = WebTables(page)
    user.navigate()
    user.go_to_elements_tab()
    user.open_web_tables_tab()
    user.add_new_user('Maria', 'Jones', 'maria.jones@testmail.com', '30', '5000', 'Sales')
    user.submit_application()

    assert page.get_by_role("gridcell", name="Maria", exact=True)


@allure.title('Test search for a user')
@allure.description('Test user can search for a user')
def test_search_for_user(page):
    user = WebTables(page)
    user.navigate()
    user.go_to_elements_tab()
    user.open_web_tables_tab()
    user.search_for_user('Cierra')

    assert user.page.get_by_role("gridcell", name="Cierra", exact=True)


@allure.title('Test user deletion from the search results')
@allure.description('Test user can delete a user from search results')
def test_delete_user_from_search_result(page):
    user = WebTables(page)
    user.navigate()
    user.go_to_elements_tab()
    user.open_web_tables_tab()
    user.search_for_user('Cierra')
    user.delete_user_from_search_result()

    assert user.search_for_user('Cierra') is None


@allure.title('Test user deletion from the table')
@allure.description('Test user can delete a user from the table')
def test_delete_user_from_the_table(page):
    user = WebTables(page)
    user.navigate()
    user.go_to_elements_tab()
    user.open_web_tables_tab()
    user.delete_user_from_the_table('Cierra', 'Vega', 39, 'cierra@example.com', 10000, 'Insurance')
    user.search_for_user('Cierra')

    assert user.search_for_user('Cierra') is None

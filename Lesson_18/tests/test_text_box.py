import allure

from Lesson_18.pages.text_box import TextBox


@allure.story('Test Text Box')
@allure.title('Test user form filling all fields')
@allure.description('Test user can fill the form with all fields filled')
class TestTextBox:
    def test_user_form_filling_all_fields(self, page):
        user_form = TextBox(page)
        user_form.navigate()
        user_form.enter_full_name('User Test')
        user_form.enter_email('test.mail@example.com')
        user_form.enter_current_address('Lipowa, 25')
        user_form.enter_permanent_address('Street, 84')
        user_form.submit_form()

        entered_name = page.locator("[id=name]").text_content()[5:]
        entered_email = page.locator("[id=email]").text_content()[6:]
        entered_current_address = page.get_by_text("Current Address : ").text_content()[17:]
        entered_permanent_address = page.get_by_text("Permananet Address : ").text_content()[19:]

        assert entered_name == 'User Test'
        assert entered_email == 'test.mail@example.com'

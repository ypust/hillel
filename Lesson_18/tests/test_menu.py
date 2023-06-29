import re

import allure
import pytest

from Lesson_18.pages.select_menu import SelectMenu


@allure.story('Test Select Menu')
class TestSelectMenu:
    @allure.title('Test Selecting item from the dropdown menu')
    @pytest.mark.parametrize('option', ["Group 2, option 1", "Another root option", "Group 1, option 1"])
    def test_select_value(self, page, option):
        menu = SelectMenu(page)
        menu.navigate()
        menu.select_value(option)
        selected_option = page.locator('//*[@id="withOptGroup"]/div/div[1]/div[1]').text_content()

        assert selected_option == option

    @allure.title('Test Selecting item from the dropdown menu(Prefixes)')
    @pytest.mark.parametrize('prefix', ['Dr.', 'Mrs.', 'Mr.', 'Ms.'])
    def test_select_prefixes(self, page, prefix):
        menu = SelectMenu(page)
        menu.navigate()
        menu.select_prefixes(prefix)
        selected_prefix = page.locator('//*[@id="selectOne"]/div/div[1]/div[1]').text_content()

        assert selected_prefix == prefix

    @allure.title('Test Selecting item from the dropdown menu(colors) ')
    @pytest.mark.parametrize('color, color_number', [('Red', 1), ('Blue', 2), ('Green', 3), ('Yellow', 4)])
    def test_select_old_style_menu(self, page, color, color_number):
        menu = SelectMenu(page)
        menu.navigate()
        menu.select_old_style_menu(color)
        selected_color = page.locator(f'//*[@id="oldSelectMenu"]/option[{color_number}]').text_content()

        assert selected_color == color

    @pytest.mark.parametrize('color, color_number', [('Green', 0), ('Blue', 1), ('Black', 2), ('Red', 3)])
    @allure.title('Test Selecting item from the dropdown menu(multiple colors)')
    def test_drop_down(self, page, color, color_number):
        menu = SelectMenu(page)
        menu.navigate()
        menu.drop_down(color_number)
        menu.drop_down(color_number)
        selected_items = page.locator(
            '//*[@id="selectMenuContainer"]/div[7]/div/div/div/div[1]/div[1]/div/div[1]').text_content()
        assert selected_items == color

    @pytest.mark.parametrize('color_number', [0, 1, 2, 3])
    @allure.title('Test clear search field')
    def test_clear_drop_down(self, page, color_number):
        menu = SelectMenu(page)
        menu.navigate()
        menu.drop_down(color_number)
        menu.clear_drop_down()
        clear_field = page.locator("div").filter(has_text=re.compile(r"^Select\.\.\.$")).nth(1).text_content()
        assert clear_field == 'Select...'

    @allure.title('Test Selecting item from the dropdown menu(car)')
    @pytest.mark.parametrize('car_model, car_option', [('Volvo', 1), ('Saab', 2), ('Opel', 3), ('Audi', 4)])
    def test_select_car(self, page, car_model, car_option):
        menu = SelectMenu(page)
        menu.navigate()
        menu.select_car(car_model)
        selected_car = page.locator(f'//*[@id="cars"]/option[{car_option}]').text_content()

        assert selected_car == car_model

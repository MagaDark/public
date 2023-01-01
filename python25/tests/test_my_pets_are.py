from conftest import *


def test_all_pets_are_present(go_to_my_pets):
    """Проверяем что на странице со списком моих питомцев присутствуют питомцы"""

    # Сохраняем в переменную statistic элементы статистики
    statistic = pytest.driver.find_elements_by_css_selector(".\\.col-sm-4.left")

    # Сохраняем в переменную pets элементы карточек питомцев
    pets = pytest.driver.find_elements_by_css_selector('.table.table-hover tbody tr')

    # Получаем количество питомцев из данных статистики
    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    # Получаем количество карточек питомцев
    number_of_pets = len(pets)

    # Проверяем что количество питомцев из статистики совпадает с количеством карточек питомцев
    assert number == number_of_pets
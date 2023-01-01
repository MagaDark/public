from conftest import *


def test_photo_availability(go_to_my_pets):
    """Поверяем что на странице со списком моих питомцев хотя бы у половины питомцев есть фото"""

    # Сохраняем в переменную statistic элементы статистики
    statistic = pytest.driver.find_elements_by_css_selector(".\\.col-sm-4.left")

    # Сохраняем в переменную images элементы с атрибутом img
    images = pytest.driver.find_elements_by_css_selector('.table.table-hover img')

    # Получаем количество питомцев из данных статистики
    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    # Находим половину от количества питомцев
    half = number // 2

    # Находим количество питомцев с фотографией
    number_photos = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            number_photos += 1

    # Проверяем что количество питомцев с фотографией больше или равно половине количества питомцев
    assert number_photos >= half
    print(f'\nКоличество фото: {number_photos}')
    print(f'\nПоловина от числа питомцев: {half}')
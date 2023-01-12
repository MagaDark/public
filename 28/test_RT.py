from selenium import webdriver
from selenium.webdriver.common.by import By
from config import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
import time



@pytest.fixture(autouse=True)    # Фикстура
def testing():
    selenium = webdriver.Chrome()  # инициализация драйвера
    selenium.implicitly_wait(7)   # ожидание 7 секунд
    selenium.get('https://b2c.passport.rt.ru')    # открытие сайта
    yield selenium   #   возврат из функции
    selenium.quit()   # закрытие сайта


""" Test_01 Пользователь может перейти на страницу регистрации """
def test_opening_registration_page(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')   # открываем сайт
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-register')))   # ожидание 7 секунд
    selenium.find_element(By.ID, 'kc-register').click()    # нажимаем на кнопку "Зарегистрироваться"
    selenium.save_screenshot('test_opening_registration_page.png')   # снимок экрана с результатом теста
    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'Регистрация', print('Тест провален')
    assert selenium.find_element(By.TAG_NAME, 'p').text == 'Личные данные', print('Тест провален')
    assert selenium.find_element(By.XPATH, '//button[@type="submit"]'), print('Тест провален')


""" Test_02 Пользователь может открыть чат поддержки, перейдя на страницу регистрации """
def test_opening_chat_registration_page(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')   # открываем сайт
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-register')))   # ожидание 7 секунд
    selenium.find_element(By.ID, 'kc-register').click()   # нажимаем на кнопку "Зарегистрироваться"
    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'widget_bar')))
    selenium.find_element(By.ID, 'widget_bar').click()   # открываем чат поддержки
    time.sleep(3)   # задержка 3 секунды
    selenium.save_screenshot('test_opening_chat_registration_page.png')   # снимок экрана с результатом теста
    assert selenium.find_element(By.ID, 'widget_sendPrechat'), print('Тест провален')


""" Test_03 На странице регистрации есть продуктовый слоган """
def test_registration_grocery_slogan(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')   # открываем сайт
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-register')))   # ожидание 7 секунд
    selenium.find_element(By.ID, 'kc-register').click()   # нажимаем на кнопку "Зарегистрироваться"
    time.sleep(3)   # задержка 3 секунды
    selenium.save_screenshot('test_registration_grocery_slogan.png')   # снимок экрана с результатом теста
    assert selenium.find_element(By.TAG_NAME, 'p').text == 'Персональный помощник в цифровом мире Ростелекома', print('Тест провален')


""" Test_04 Регистрация на сайте с валидными данными """
def test_registration(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')   # открываем сайт
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-register')))   # ожидание 7 секунд
    selenium.find_element(By.ID, 'kc-register').click()   # нажимаем на кнопку "Зарегистрироваться"
    selenium.find_element(By.NAME, 'firstName').send_keys(valid_name)   # вводим данные в поле "Имя"
    selenium.find_element(By.NAME, 'lastName').send_keys(valid_surname)   # вводим данные в поле "Фамилия"
    selenium.find_element(By.ID, 'address').send_keys(valid_email)   # вводим данные в поле "E-mail или мобильный телефон". В данном случае вводим email
    selenium.find_element(By.ID, 'password').send_keys(valid_password)   # вводим данные в поле "Пароль"
    selenium.find_element(By.ID, 'password-confirm').send_keys(valid_password)   # вводим данные в поле "Подтверждение пароля"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()   # нажимаем на кнопку "Зарегистрироваться"
    time.sleep(3)   # задержка 3 секунды
    selenium.find_element(By.ID, 'rt-code-0').send_keys(valid_code)   # вводим код, который будет получен по электронной почте
    selenium.save_screenshot('test_registration.png')   # снимок экрана с результатом теста
    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'Подтверждение email', print('Тест провален')


""" Test_05 Регистрация пользователя с невалидным вводом всех полей (только цифры) """
def test_registration_2(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')   # открываем сайт
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-register')))   # ожидание 7 секунд
    selenium.find_element(By.ID, 'kc-register').click()   # нажимаем на кнопку "Зарегистрироваться"
    selenium.find_element(By.NAME, 'firstName').send_keys(invalid_name)    # вводим некорректные данных в поле "Имя"
    selenium.find_element(By.NAME, 'lastName').send_keys(invalid_surname)   # вводим некорректные данных в поле "Фамилия"
    selenium.find_element(By.ID, 'address').send_keys(invalid_email)    # вводим некорректные данные в поле "E-mail или мобильный телефон"
    selenium.find_element(By.ID, 'password').send_keys(invalid_password)   # вводим некорректные данных в поле "Пароль"
    selenium.find_element(By.ID, 'password-confirm').send_keys(invalid_password)   # вводим данные в поле "Подтверждение пароля"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()   # нажимаем на кнопку "Зарегистрироваться"
    time.sleep(3)   # задержка 3 секунды
    selenium.save_screenshot('test_registration_2.png')   # снимок экрана с результатом теста


""" Test_06 Регистрация пользователя с невалидным вводом некоторых полей """
def test_registration_3(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')   # открываем сайт
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-register')))   # ожидание 7 секунд
    selenium.find_element(By.ID, 'kc-register').click()   # нажимаем на кнопку "Зарегистрироваться"
    selenium.find_element(By.NAME, 'firstName').send_keys(valid_name)   # вводим корректные данные в поле "Имя"
    selenium.find_element(By.NAME, 'lastName').send_keys(valid_surname)   # вводим корректные данные в поле "Фамилия"
    selenium.find_element(By.ID, 'address').send_keys(invalid_email)   # вводим некорректные данные в поле "E-mail или мобильный телефон". В данном случае вводим email
    selenium.find_element(By.ID, 'password').send_keys(valid_password)   # вводим некорректные данные в поле "Пароль"
    selenium.find_element(By.ID, 'password-confirm').send_keys(invalid_password)   # вводим данные в поле "Подтверждение пароля"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()   # нажимаем на кнопку "Зарегистрироваться"
    time.sleep(3)   # задержка 3 секунды
    selenium.save_screenshot('test_registration_3.png')   # снимок экрана с результатом теста


""" Test_07 Регистрация пользователя с вводом неверного кода доступа """
def test_registration_4(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')   # открытие сайта
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-register')))   # ожидание 7 секунд
    selenium.find_element(By.ID, 'kc-register').click()   # нажимаем на кнопку "Зарегистрироваться"
    selenium.find_element(By.NAME, 'firstName').send_keys(valid_name)   # ввод данных в поле "Имя"
    selenium.find_element(By.NAME, 'lastName').send_keys(valid_surname)   # ввод данных в поле "Фамилия"
    selenium.find_element(By.ID, 'address').send_keys(valid_email)   # ввод данных в поле "E-mail или мобильный телефон". В данном случае вводим email
    selenium.find_element(By.ID, 'password').send_keys(valid_password)   # ввод данных в поле "Пароль"
    selenium.find_element(By.ID, 'password-confirm').send_keys(valid_password)   # ввод данных в поле "Подтверждение пароля"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()   # нажимаем на кнопку "Зарегистрироваться"
    time.sleep(3)   # задержка 3 секунды
    selenium.find_element(By.ID, 'rt-code-0').send_keys(invalid_code)   # ввод некорректного кода
    time.sleep(3)   # задержка 3 секунды
    selenium.save_screenshot('test_registration_4.png')   # снимок экрана с результатом теста


""" Test_08 Регистрация пользователя с невалидным вводом всех полей (только спецсимволы) """
def test_registration_5(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')   # открытие сайта
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-register')))   # ожидание 7 секунд
    selenium.find_element(By.ID, 'kc-register').click()   # нажимаем на кнопку "Зарегистрироваться"
    selenium.find_element(By.NAME, 'firstName').send_keys(invalid_name_2)   # вводим некорректные данные в поле "Имя"
    selenium.find_element(By.NAME, 'lastName').send_keys(invalid_surname_2)   # вводим некорректные данные в поле "Фамилия"
    selenium.find_element(By.ID, 'address').send_keys(invalid_email_2)   # вводим некорректные данные в поле "E-mail или мобильный телефон"
    selenium.find_element(By.ID, 'password').send_keys(invalid_password_2)   # вводим некорректные данные в поле "Пароль"
    selenium.find_element(By.ID, 'password-confirm').send_keys(invalid_password_2)   # вводим данные в поле "Подтверждение пароля"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()   # нажимаем на кнопку "Зарегистрироваться"
    time.sleep(3)   # задержка 3 секунды
    selenium.save_screenshot('test_registration_5.png')   # снимок экрана с результатом теста


""" Test_09 Регистрация пользователя с невалидным вводом всех полей (русская и английская раскладка) """
def test_registration_6(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')   # открытие сайта
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-register')))   # ожидание 7 секунд
    selenium.find_element(By.ID, 'kc-register').click()   # нажимаем на кнопку "Зарегистрироваться"
    selenium.find_element(By.NAME, 'firstName').send_keys(invalid_name_3)   # ввод некорректных данных в поле "Имя"
    selenium.find_element(By.NAME, 'lastName').send_keys(invalid_surname_3)   # ввод некорректных данных в поле "Фамилия"
    selenium.find_element(By.ID, 'address').send_keys(invalid_email_3)   # ввод некорректных данных в поле "E-mail или мобильный телефон"
    selenium.find_element(By.ID, 'password').send_keys(invalid_password_3)   # ввод некорректных данных в поле "Пароль"
    selenium.find_element(By.ID, 'password-confirm').send_keys(invalid_password_3)   # ввод некорректных данных в поле "Подтверждение пароля"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()   # нажимаем на кнопку "Зарегистрироваться"
    time.sleep(3)   # задержка 3 секунды
    selenium.save_screenshot('test_registration_6.png')   # снимок экрана с результатом теста


""" Test_10 Пользователь ввёл в поле "Подтверждение пароля" пароль, отличный от пароля "Новый пароль" то под полем "Подтверждение" отображается "Пароли не совпадают" """
def test_registration_7(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')   # открытие сайта
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-register')))   # ожидание 7 секунд
    selenium.find_element(By.ID, 'kc-register').click()   # нажимаем на кнопку "Зарегистрироваться"
    selenium.find_element(By.NAME, 'firstName').send_keys(valid_name)   # ввод корректных данных в поле "Имя"
    selenium.find_element(By.NAME, 'lastName').send_keys(valid_surname)   # ввод корректных данных в поле "Фамилия"
    selenium.find_element(By.ID, 'address').send_keys(valid_email)   # ввод корректных данных в поле "E-mail или мобильный телефон"
    selenium.find_element(By.ID, 'password').send_keys(valid_password)   # ввод корректных данных в поле "Пароль"
    selenium.find_element(By.ID, 'password-confirm').send_keys(invalid_password_4)   # ввод данных в поле "Подтверждение пароля"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()   # нажимаем на кнопку "Зарегистрироваться"
    time.sleep(3)   # задержка 3 секунды
    selenium.save_screenshot('test_registration_7.png')   # снимок экрана с результатом теста


""" Test_11 Пользователь может перейти на страницу авторизации """
def test_opening_authorization_page(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')   # открытие сайта
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-login')))   # ожидание 7 секунд
    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'Авторизация', print('Тест провален')
    assert selenium.find_element(By.ID, 'kc-login'), print('Тест провален')
    selenium.save_screenshot('test_opening_authorization_page.png')   # снимок экрана с результатом теста


""" Test_12 Пользователь может открыть чат поддержки на странице авторизации """
def test_opening_chat_authorization_page(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')   # открытие сайта
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-login')))   # ожидание 7 секунд
    selenium.find_element(By.ID, 'widget_bar').click()   # нажать на виджет "Поддержка"
    time.sleep(3)   # задержка 3 секунды
    assert selenium.find_element(By.ID, 'widget_sendPrechat'), print('Тест провален')
    selenium.save_screenshot('test_opening_chat_authorization_page.png')   # снимок экрана с результатом теста


""" Test_13 На странице авторизации есть продуктовый слоган """
def test_authorization_grocery_slogan(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')   # открытие сайта
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-login')))   # ожидание 7 секунд
    assert selenium.find_element(By.TAG_NAME, 'p').text == 'Персональный помощник в цифровом мире Ростелекома', \
        print('Тест провален')
    selenium.save_screenshot('test_authorization_grocery_slogan.png')   # снимок экрана с результатом теста


""" Test_14 Таб выбора авторизации по номеру, "Номер" """
def test_opening_authorization_page_2(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')   # открытие сайта
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-login')))   # ожидание 7 секунд
    selenium.find_element(By.ID, 't-btn-tab-phone').click()   # таб "Телефон"
    selenium.save_screenshot('test_opening_authorization_page_2.png')   # снимок экрана с результатом теста
    time.sleep(3)   # задержка 3 секунды
    assert selenium.find_element(By.ID, 't-btn-tab-phone').text == 'Номер', print('Тест провален')


""" Test_15 Таб выбора авторизации по логину и паролю, "Почта" """
def test_opening_authorization_page_3(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')   # открытие сайта
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-login')))   # ожидание 7 секунд
    selenium.find_element(By.ID, 't-btn-tab-login').click()   # таб "Логин"
    selenium.save_screenshot('test_opening_authorization_page_3.png')   # снимок экрана с результатом теста
    time.sleep(3)   # задержка 3 секунды
    assert selenium.find_element(By.ID, 't-btn-tab-login').text == 'Почта', print('Тест провален')


""" Test_16 Таб выбора авторизации по почте и паролю, "Логин" """
def test_opening_authorization_page_4(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')   # открытие сайта
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-login')))   # ожидание 7 секунд
    selenium.find_element(By.ID, 't-btn-tab-mail').click()   # таб "Почта"
    selenium.save_screenshot('test_opening_authorization_page_4.png')   # снимок экрана с результатом теста
    time.sleep(3)   # задержка 3 секунды
    assert selenium.find_element(By.ID, 't-btn-tab-mail').text == 'Логин', print('Тест провален')


""" Test_17 Таб выбора авторизации по лицевому счету и паролю, "Лицевой счёт" """
def test_opening_authorization_page_5(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')   # открытие сайта
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-login')))   # ожидание 7 секунд
    selenium.find_element(By.ID, 't-btn-tab-ls').click()   # таб "Лицевой счёт"
    selenium.save_screenshot('test_opening_authorization_page_5.png')   # снимок экрана с результатом теста
    time.sleep(3)   # задержка 3 секунды
    assert selenium.find_element(By.ID, 't-btn-tab-ls').text == 'Лицевой счёт', print('Тест провален')


""" Test_18 Авторизация с помощью валидных введённых данных (мобильный телефон и пароль) (действующий аккаунт)"""
def test_authorization(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')   # открытие сайта
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-login')))    # ожидание 7 секунд
    selenium.find_element(By.ID, 't-btn-tab-phone').click()   # нажать на "Телефон"
    selenium.find_element(By.ID, 'username').send_keys(valid_phone)   # ввод корректного номера телефона
    selenium.find_element(By.ID, 'password').send_keys(valid_password)   # ввод корректного пароля
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()   # нажимаем на кнопку "Войти"
    time.sleep(3)   # задержка 3 секунды
    selenium.save_screenshot('test_authorization.png')   # снимок экрана с результатом теста
    assert selenium.find_element(By.TAG_NAME, 'h3').text == 'Учетные данные', print('Тест провален')


""" Test_19 Авторизация с помощью валидных введённых данных (электронная почта и пароль) (действующий аккаунт)"""
def test_authorization_2(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')   # открытие сайта
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-login')))   # ожидание 7 секунд
    selenium.find_element(By.ID, 't-btn-tab-mail').click()   # нажать на "Почта"
    selenium.find_element(By.ID, 'username').send_keys(valid_email)   # ввод корректной электронной почты
    selenium.find_element(By.ID, 'password').send_keys(valid_password)   # ввод корректного пароля
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()   # нажимаем на кнопку "Войти"
    time.sleep(3)   # задержка 3 секунды
    selenium.save_screenshot('test_authorization_2.png')   # снимок экрана с результатом теста
    assert selenium.find_element(By.TAG_NAME, 'h3').text == 'Учетные данные', print('Тест провален')


""" Test_20 Авторизация валидные данные (логин и пароль) (действующий аккаунт) """
def test_authorization_3(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')   # открытие сайта
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-login')))   # ожидание 7 секунд
    selenium.find_element(By.ID, 't-btn-tab-login').click()   # нажать на "Логин"
    selenium.find_element(By.ID, 'username').send_keys(valid_name)   # ввод валидного логина
    selenium.find_element(By.ID, 'password').send_keys(valid_password)   # ввод валидного пароля
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()   # нажимаем на кнопку "Войти"
    time.sleep(3)   # задержка 3 секунды
    selenium.save_screenshot('test_authorization_3.png')   # снимок экрана с результатом теста
    assert selenium.find_element(By.TAG_NAME, 'h3').text == 'Учетные данные', print('Тест провален')


""" Test_21 Авторизация: валидный номер телефона, но невалидный пароль """
def test_authorization_4(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')   # открытие сайта
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-login')))   # ожидание 7 секунд
    selenium.find_element(By.ID, 't-btn-tab-phone').click()   # нажать на "Телефон"
    selenium.find_element(By.ID, 'username').send_keys(valid_phone)   # ввод корректного номера телефона
    selenium.find_element(By.ID, 'password').send_keys(invalid_password)   # ввод некорректного пароля
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()   # нажимаем на кнопку "Войти"
    time.sleep(3)   # задержка 3 секунды
    selenium.save_screenshot('test_authorization_4.png')   # снимок экрана с результатом теста
    assert selenium.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль', print('Тест провален')


""" Test_22 Авторизация: верная электронная почта, но неверный пароль """
def test_authorization_5(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')   # открытие сайта
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-login')))   # ожидание 7 секунд
    selenium.find_element(By.ID, 't-btn-tab-mail').click()   # нажать на "Почта"
    selenium.find_element(By.ID, 'username').send_keys(valid_email)    # ввод корректной электронной почты
    selenium.find_element(By.ID, 'password').send_keys(invalid_password)   # ввод некорректного пароля
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()    # нажимаем на кнопку "Войти"
    time.sleep(3)   # задержка 3 секунды
    selenium.save_screenshot('test_authorization_5.png')   # снимок экрана с результатом теста
    assert selenium.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль', print('Тест провален')


""" Test_23 Пользователь может перейти на страницу "Восстановление пароля" """
def test_password_recovery(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')   # открытие сайта
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-login')))   # ожидание 7 секунд
    selenium.find_element(By.ID, 'forgot_password').click()   # нажимаем на кнопку "Забыл пароль"
    selenium.save_screenshot('test_password_recovery.png')   # снимок экрана с результатом теста
    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'Восстановление пароля', print('Тест провален')
    assert selenium.find_element(By.TAG_NAME, 'p').text == 'Введите данные и нажмите «Продолжить»', print('Тест провален')
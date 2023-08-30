import time

import pytest
from testpage import OperationHelper

username = "Cm"
password = "4d42fd7ad7"


def test_step_1(browser):
    test_page1 = OperationHelper(browser)
    test_page1.go_to_site()
    test_page1.enter_login("Cm")
    test_page1.enter_pswd("4d42fd7ad7")
    test_page1.click_button()
    time.sleep(3)
    # Залогинились
    test_page1.click_contact()
    time.sleep(3)
    # Заполняем поля
    test_page1.enter_cont_name("Alexey")
    test_page1.enter_cont_email("yandex@yandex.ru")
    test_page1.enter_cont_text("Hello world!")
    time.sleep(1)
    # нажимаем кнопку
    test_page1.click_button()
    time.sleep(1)
    # проверим текст всплывающего окна
    assert test_page1.get_alert_text() == "Form successfully submitted"

import yaml
import pytest
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])

def test_step1():
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("kulizhenya")
    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("d0641c1a50")
    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()
    x_selector3 = """//*[id="Title"]/div[1]/label/input"""
    input3.send_keys("заголовок")
    x_selector4 = """//*[id="Description]/div[1]/label/input"""
    input4.send_keys("описание")
    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()
    assert "Заголовок" in https://test-stand.gb.ru/posts/72627
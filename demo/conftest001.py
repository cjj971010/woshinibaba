from time import sleep

import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def driver():
    # 打开浏览器
    driver = webdriver.Chrome('../chrome_drive_v78//chromedriver.exe')

    sleep(1)
    # 调整浏览器窗口大小
    driver.maximize_window()
    driver.implicitly_wait(10)#设置等待时长10秒

    #浏览器全局设置，一般在浏览器启动之后设置一次，终生有效
    yield driver
    driver.quit()



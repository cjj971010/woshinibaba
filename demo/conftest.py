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
    sleep(1)
    yield driver
    driver.quit()
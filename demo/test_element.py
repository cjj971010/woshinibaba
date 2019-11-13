from asyncio import sleep
from time import sleep

import autoit
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def test_input(driver):
    driver.get("http://ui.yansl.com/#/input")
    sleep(2)

    input = driver.find_element_by_xpath("//input[@name='t1']")
    #清空
    input.clear()
    #输入
    input.send_keys("我是谁？我在哪？我叫什么")
    sleep(2)



def test_radio(driver):
    driver.get("http://ui.yansl.com/#/radio")
    sleep(2)

    radio = driver.find_element_by_xpath("//input[@name='sex'][2]")
    #点击
    radio.click()
    sleep(2)


def test_select(driver):
    driver.get("http://ui.yansl.com/#/select")
    sleep(2)

    select = driver.find_element_by_xpath("//*[@id='form']/form/div[3]/div/div/div[2]/input")
    #点击
    select.click()
    sleep(2)

    option = driver.find_element_by_xpath("(//span[text()='双皮奶'])[last()]")
    actions = ActionChains(driver)
    actions.move_to_element(option).perform()
    sleep(2)
    option.click()
    sleep(2)



def test_slider(driver):
    driver.get("http://ui.yansl.com/#/select")
    sleep(2)

    select = driver.find_element_by_xpath("//*[@id='form']/form/div[3]/div/div/div[2]/input")
    #点击
    select.click()
    sleep(2)

    option = driver.find_element_by_xpath("(//span[text()='双皮奶'])[last()]")
    actions = ActionChains(driver)
    actions.move_to_element(option).perform()
    sleep(2)
    option.click()
    sleep(2)


def test_time(driver):
    driver.get("http://ui.yansl.com/#/datetime")
    sleep(2)

    t1 = driver.find_element_by_xpath("//*[@id='form']/form/div[1]/div[1]/div/div/input")
    #清空
    t1.clear()
    #输入
    t1.send_keys("14:14:00")
    sleep(2)


def test_file(driver):
    driver.get("http://ui.yansl.com/#/upload")
    sleep(2)

    file = driver.find_element_by_xpath("//*[@id='form']/form/div[1]/div/input")
    #清空
    file.clear()
    file.send_keys("C:\\Users\\guoya\\Desktop\\手机.jpg")
    sleep(2)


def test_file2(driver):
    driver.get("http://ui.yansl.com/#/upload")
    sleep(2)

    file = driver.find_element_by_xpath("//*[@id='form']/form/div[2]/div/div/div[1]/button/span")

    file.click()
    sleep(2)
    autoit.win_wait("打开", 10)
    sleep(1)
    # autoit.control_send("打开", "Edit1", os.path.abspath(file_path))
    autoit.control_set_text("打开", "Edit1", "C:\\Users\guoya\Desktop\手机.jpg")
    sleep(2)
    autoit.control_click("打开", "Button1")

def test_windows(driver):
    driver.get("http://192.168.1.128:8082/xuepl/demo.html")
    sleep(2)
    dang_dang = driver.find_element_by_link_text("当当")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(dang_dang).key_up(Keys.CONTROL).perform()
    sleep(2)
    jd = driver.find_element_by_link_text("京东")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(jd).key_up(Keys.CONTROL).perform()
    sleep(2)
    dn = driver.find_element_by_partial_link_text("度娘")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(dn).key_up(Keys.CONTROL).perform()
    sleep(2)

    # 获取所有窗口的句柄
    handles = driver.window_handles
    for h in handles:
        # 根据窗口句柄，切换窗口
        driver.switch_to.window(h)
        sleep(2)
        if driver.title.__contains__("京东"):
            break
from asyncio import sleep
from time import sleep

import autoit
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # 定义了变量EC表示expected_conditions


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

# 嵌套切换
def test_iframe(driver):
    driver.get("http://192.168.1.128:8082/xuepl1/frame/main.html")
    sleep(2)
# 进入到当前的iframe模块(左侧模块)
    frame = driver.find_element_by_xpath('/html/frameset/frameset/frame[1]')
# 涉及到切换模块用frame
    driver.switch_to.frame(frame)
    sleep(2)
    # 点击京东的文字按钮
    driver.find_element_by_partial_link_text('京东').click()
    sleep(2)
    #退出当前iframe
    driver.switch_to.parent_frame()
    #回到初始页面
    # driver.switch_to.default_content()
    # 进入到当前的iframe模块（京东模块）
    iframe = driver.find_element_by_xpath("/html/frameset/frameset/frame[2]")
    # 涉及到切换模块用frame
    driver.switch_to.frame(iframe)
    sleep(2)
    # 选定输入框
    inpu = driver.find_element_by_xpath('//*[@id="key"]')
    inpu.clear()
    # 输入文本（电脑）
    inpu.send_keys("电脑")
    sleep(2 )





def test_wait(driver):
    driver.get("http://ui.yansl.com/#/loading")
    bt = driver.find_element_by_xpath("//span[contains(text(),'指令方式')]")
    bt.click()
    WebDriverWait(driver, 5, 0.5).until(
        EC.visibility_of_element_located((By.XPATH, '//tbody/tr[1]/td[2]/div'))
    )
    bg = driver.find_element_by_xpath("//tbody/tr[1]/td[2]/div")
    print(bg.text)
    sleep(2)


# 消息提示
def test_text(driver):
    driver.get("http://ui.yansl.com/#/message")
    # 定位到“自动关闭提示”中的“消息”模块.多元素+s,elements
    buttons = driver.find_elements_by_xpath("//label[contains(text(),'自动关闭提示')]/..//span[text()='消息']")
    buttons[0].click()  #取下标0（0消息）
    # 再定位到提示信息
    message = driver.find_element_by_xpath("//div[@role='alert']/p")
    text = message.text # text+方法  获取展示文本
    print(text)
    assert"这是一条消息" in text
    sleep(2)
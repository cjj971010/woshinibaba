# 消息提示
from time import sleep


def test_text(driver):
    driver.get("http://ui.yansl.com/#/message")
    # 定位到“自动关闭提示”中的“消息”模块.多元素+s,elements
    buttons = driver.find_elements_by_xpath("//label[contains(text(),'自动关闭提示')]/..//span[text()='消息']")
    buttons[0].click()  # 取下标0（0消息）
    # 再定位到提示信息
    message = driver.find_element_by_xpath("//div[@role='alert']/p")
    text = message.text  # text+方法  获取展示文本
    print(text)
    assert "这是一条消息" in text
    sleep(2)


def test_page_source(driver):
    driver.get("http://ui.yansl.com/")
    sleep(2)
    driver.find_element_by_xpath('//*[@id="app"]/section/section/aside/ul/li[3]/div').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="app"]/section/section/aside/ul/li[3]/ul/li/ul/li[3]').click()
    sleep(2)
    #获取页面源代码
    source = driver.page_source
    print(source)
    assert "手工关闭提示"in source
    sleep(2)
# coding=utf-8

from appium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import os

class Tests(unittest.TestCase):
    # 启动app
    def setUp(self):
        app = os.path.abspath('/Users/ryan/workspace/appium/nfzmAppPath/nfzm.app')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '14.1',
                'deviceName': 'iPhone 11 Pro Max',
                # 'udid': '212442AB-2EB3-466F-A81A-60FCC6956DBE',
                'automationName': 'XCUITest',
                'noReset': 'True'
        })
        self.driver.implicitly_wait(20)

    # 定义多个test cases，比如查看页面元素
    def testCase1_findElements(self):
        driver = self.driver

        # 协议声明弹窗
        try:
            button = driver.find_element_by_id("nfzmNZCommonAlertView0")
            button.click()
        except NoSuchElementException:
            print('找不到协议页，可能之前已经同意过了')
        # else:
        #     print('成功点击了协议页')


        time.sleep(2)
        
        # 推送
        try:
            self.driver.switch_to.alert.accept()
        except NoAlertPresentException:
            print('没有推送alertView')
        # else:
        #     print('推送alert点击成功')


        # 查找引导页
        try:
            guideElement = driver.find_element_by_ios_predicate('type=="XCUIElementTypeScrollView"')
            if guideElement is not None:
                size = guideElement.size
                x = size['width']
                y = size['height']
                x1 = x * 0.9
                y1 = y * 0.5
                x2 = x * 0.1
                t = 1000
                n = 4  # n表示滑动次数
                time.sleep(1)
                for i in range(n):
                    driver.swipe(x1, y1, x2, y1, t)
        except NoSuchElementException:
            print('找不到引导页')
        # else:
        #     print('成功点击了引导页')

        try:
            guideEnterButton = driver.find_element_by_ios_predicate('type=="XCUIElementTypeButton"')
            guideEnterButton.click()
            time.sleep(5)
        except NoSuchElementException:
            print('找不到引导页上的确认按钮')
        # else:
        #     print('成功进入了主页')

        # 进入主页

        try:
            tabbar = driver.find_element_by_ios_predicate('type=="XCUIElementTypeTabBar"')
        except NoSuchElementException:
            print('找不到写真的tab')
        else:
            print('!!找到了Tab!!!')

        # 查找所有可以点击的按钮
        try:
            buttons = tabbar.find_elements_by_ios_predicate('type=="XCUIElementTypeButton"')
        except NoSuchElementException:
            print('找不到buttons')
        else:
            print('找到了')
            for button in buttons:
                button.click()
                time.sleep(2)


        # 我的
        try:
            tabMy=  tabbar.find_element_by_name('我的')
        except NoSuchElementException:
            print('找不到我的')
        else:
            print('能找到"我的"')
            print(tabMy.get_attribute('type'))
            tabMy.click()

        # 影像
        try:
            tabVideo=  tabbar.find_element_by_name('影像')
        except NoSuchElementException:
            print('找不到我的')
        else:
            tabVideo.click()

        # 严选
        try:
            tabYanXuan =  tabbar.find_element_by_name('我的')
        except NoSuchElementException:
            print('找不到我的')
        else:
            tabYanXuan.click()
        # VIP
        try:
            tabVip =  tabbar.find_element_by_name('我的')
        except NoSuchElementException:
            print('找不到我的')
        else:
            tabVip.click()

    time.sleep(3)

    # 比如点击按钮，页面会有元素改变
    def testCase2_ButtonChange(self):
        driver = self.driver

        # Click the button to change the content of the label and the text
        button = driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Button"]')
        button.click()
        time.sleep(2)
        textWorld = driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="world"]').text
        textaaa = driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="TestProduct"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTextField')

        # 添加断言，若label和text没有被改变或正确地被改变，则打印错误信息try:
        assert textWorld == 'changed label', print('The label has not been changed by button')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Tests('testCase1_findElements'))
    # suite.addTest(Tests('testCase2_ButtonChange'))
    unittest.TextTestRunner(verbosity=1).run(suite)
    # 一种简单打印测试报告的方式，执行数，成功数，失败数
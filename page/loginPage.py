"""
============================
Author:柠檬班-木森
Time:2021/2/20 20:13
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
=======
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from common.base_page import BasePage


class LoginPage(BasePage):
    # 账号输入框
    user_input_loc = (By.XPATH, '//input[@name="account"]')
    # 密码输入框
    pwd_input_loc = (By.XPATH, '//input[@name="pass"]')
    # 点击登录
    btn_loc = (By.XPATH, '(//a[@class="btn-btn"])[1]')
    # 错误提示元素
    error_info = (By.XPATH, '//p[@class="error-tips"]')

    def login(self, user, pwd):
        """登录操作"""
        # 输入账号
        # self.driver.find_element(*self.user_input_loc).send_keys(user)
        # 输入密码
        # self.driver.find_element(*self.pwd_input_loc).send_keys(pwd)
        # 点击登录
        # self.driver.find_element(*self.btn_loc).click()

        self.input_send_keys(self.user_input_loc, user, '登录页面_账号输入')
        self.input_send_keys(self.pwd_input_loc, pwd, '登录页面_密码输入')
        self.click_element(self.btn_loc, '登录页面_登录按钮')

    def get_error_info(self):
        """获取错误提示"""
        # return self.driver.find_element(*self.error_info).text
        return self.get_element_text(self.error_info, '登录页面_登录的错误提示')



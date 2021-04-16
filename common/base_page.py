"""
============================
Author:柠檬班-木森
Time:2021/2/23 20:19
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
=======
"""
import os

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from common.handler_log import my_log

"""
BasePage: 封装的是一个所有页面的父类，在父类张红封装一些页面常用的操作方法
    1、查找元素
    2、点击元素
    3、输入内容
    4、清空输入框
    5、获取元素文本
    6、获取元素的属性
    7、等待元素可见
    8、等待元素可点击
    9、等待元素存在
    10、iframe切换
    11、错误截图
    
    
    12、窗口切换
    13、打开新窗口
    
    14、执行js代码
    
    
"""
import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.handle_path import ERROR_IMAGE_DIR


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_element(self, loc, desc=None):
        """
        查找元素
        :param loc: 元素的定位器
        :param desc: 元素的描述
        :return:
        """
        try:
            ele = self.driver.find_element(*loc)
        except Exception as e:
            my_log.error("查找元素--【{}】--失败".format(desc))
            my_log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            my_log.info("查找元素--【{}】--成功".format(desc))
        return ele

    def get_elements(self, loc, desc=None):
        """
        查找多个元素
        :param loc: 元素的定位器
        :param desc: 元素的描述
        :return:
        """
        try:
            eles = self.driver.find_elements(*loc)
        except Exception as e:
            my_log.error("查找元素--【{}】--失败".format(desc))
            my_log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            my_log.info("查找元素--【{}】--成功".format(desc))
        return eles

    def click_element(self, loc, desc=None):
        """
        点击元素
        :param loc: 元素的定位器
        :param desc: 元素的描述
        :return:
        """
        try:
            self.driver.find_element(*loc).click()
        except Exception as e:
            my_log.error("点击元素--【{}】--失败".format(desc))
            my_log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            my_log.info("点击元素--【{}】--成功".format(desc))

    def input_send_keys(self, loc, value, desc=None):
        """
        输入框，输入
        :param loc: input框元素的定位器
        :param value: 输入的值
        :param desc: 元素的描述
        :return:
        """
        try:
            self.driver.find_element(*loc).send_keys(value)
        except Exception as e:
            my_log.error("往输入框--【{}】--输入值失败".format(desc))
            my_log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            my_log.info("往输入框--【{}】--输入值成功".format(desc))

    def clear_input(self, loc, desc):
        """
        清空输入框
        :param loc:  input框元素的定位器
        :param desc: 元素的描述
        :return:
        """
        try:
            self.driver.find_element(*loc).clear()
        except Exception as e:
            my_log.error("情况输入框--【{}】--失败".format(desc))
            my_log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            my_log.info("情况输入框--【{}】--成功".format(desc))

    def get_element_text(self, loc, desc):
        """
        获取元素的文本
        :param loc: 元素的定位器
        :param desc: 元素的描述
        :return:
        """
        try:
            text = self.driver.find_element(*loc).text
        except Exception as e:
            my_log.error("查找元素--【{}】--失败".format(desc))
            my_log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            my_log.info("查找元素--【{}】--成功".format(desc))
        return text

    def get_element_attribute(self, loc, attr, desc):
        """
        获取元素的属性
        :param loc:  元素的定位器
        :param attr:  属性名
        :param desc:   元素的描述
        :return:
        """
        try:
            res = self.driver.find_element(*loc).get_attribute(attr)
        except Exception as e:
            my_log.error("获取元素--【{}】--的属性失败".format(desc))
            my_log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            my_log.info("获取元素--【{}】--的属性成功".format(desc))
        return res

    def wait_element_visibility(self, loc, desc=None, timeout=10):
        """
        等待元素可见
        :param loc: 元素的定位器
        :param desc: 元素的描述
        :return:
        """
        try:
            ele = WebDriverWait(self.driver, timeout, 0.5).until(
                EC.visibility_of_element_located(loc)
            )
        except Exception as e:
            my_log.error("等待元素可见--【{}】--失败".format(desc))
            my_log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            my_log.info("等待元素可见--【{}】--成功".format(desc))
        return ele

    def wait_element_presence(self, loc, desc=None, timeout=10):
        """
        等待元素存在
        :param loc: 元素的定位器
        :param desc: 元素的描述
        :return:
        """
        try:
            ele = WebDriverWait(self.driver, timeout, 0.5).until(
                EC.presence_of_element_located(loc)
            )
        except Exception as e:
            my_log.error("等待元素存在--【{}】--失败".format(desc))
            my_log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            my_log.info("等待元素存在--【{}】--成功".format(desc))
        return ele

    def wait_element_clickable(self, loc, desc=None, timeout=10):
        """
        等待元素可点击
        :param loc: 元素的定位器
        :param desc: 元素的描述
        :return:
        """
        try:
            ele = WebDriverWait(self.driver, timeout, 0.5).until(
                EC.element_to_be_clickable(loc)
            )
        except Exception as e:
            my_log.error("等待元素可点击--【{}】--失败".format(desc))
            my_log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            my_log.info("等待元素可点击--【{}】--成功".format(desc))
        return ele

    def switch_to_iframe_loc(self, loc, desc):
        """
        通过frame标签的定位表达式，进行ifrome切换
        :param loc: 元素的定位器
        :param desc: 元素的描述
        :return:
        """
        try:
            WebDriverWait(self.driver, 20, 0.5).until(
                EC.frame_to_be_available_and_switch_to_it(loc)
            )
        except Exception as e:
            my_log.error("等待iframe可见并进行切换--【{}】--失败".format(desc))
            my_log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            my_log.info("等待iframe可见并进行切换--【{}】--成功".format(desc))

    def switch_to_iframe_name(self, name, desc):
        """
        通过frame标签的name属性，进行ifrome切换
        :param name iframe标签的name属性
        :param desc: 元素的描述
        :return:
        """
        try:
            self.driver.switch_to.frame(name)
        except Exception as e:
            my_log.error("切换iframe--【{}】--失败".format(desc))
            my_log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            my_log.info("切换iframe--【{}】--成功".format(desc))

    def error_save_screenshot(self, desc):
        """
        错误截图
        :return:
        """
        i_date = time.strftime("%Y-%m-%d_%H_%M_%S_")
        filename = i_date + desc + '.png'
        file_path = os.path.join(ERROR_IMAGE_DIR, filename)
        try:
            self.driver.save_screenshot(file_path)
        except Exception as e:
            my_log.error("对-【{}】--操作进行截图--失败".format(desc))
            my_log.exception(e)
            raise e
        else:
            with open(file_path, 'rb') as f:
                content = f.read()
            allure.attach(content, '失败截图', allure.attachment_type.PNG)
            my_log.info("对-【{}】--操作进行截图--成功".format(desc))
            my_log.info("图片保存为{}".format(file_path))
        return file_path

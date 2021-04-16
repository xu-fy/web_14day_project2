"""
============================
Author:柠檬班-木森
Time:2021/2/20 20:07
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
=======
"""
import allure
import pytest

from page.indexPage import IndexPage
from page.loginPage import LoginPage
from datas import global_data as GD
from datas.test_data import LoginData

"""
登录功能：

页面：  
    一、登录页面
        1、 登录操作
            涉及到的元素：
                - 账号输入框
                - 密码输入框
                - 点击登录
        2、获取错误提示
            涉及到的元素：
               - 错误信息提示
                
    二、首页
        1、判断用户是登录成功（获取用户信息的元素，看是否存在）
            涉及到的元素：
               - 用户信息
                           
用例执行的步骤：

    1、打开浏览器
    2、进行登录操作
    3、断言

"""

from datas import global_data as GD
from common.handler_log import my_log


# datas = [{'data': 12, "title": "账号为空"},
#          {'data': 13, "title": "密码为空"},
#          {'data': 14, "title": "账号错误"},
#          ]
#
# datas2 = [{'data': 12, "title": "注册账号为空"},
#           {'data': 13, "title": "注册密码为空"},
#           {'data': 14, "title": "注册账号错误"},
#           ]
#
#
# @allure.suite('用户模块')
# @allure.story('登录功能')
# class TestLogin:
#     """测试登录功能"""
#
#     @allure.title('登录成功')
#     def test_login_pass(self):
#         pass
#
#     @pytest.mark.parametrize('case', datas)
#     def test_login_error(self, case):
#         allure.dynamic.title(case['title'])
#
#
# @allure.story('登录功能')
# class TestRigers:
#     """测试登录功能"""
#
#     @allure.title('注册成功')
#     def test_login_pass(self):
#         pass
#
#     @pytest.mark.parametrize('case', datas2)
#     def test_login_error(self, case):
#         allure.dynamic.title(case['title'])

class TestLogin:
    """测试登录功能"""

    @allure.title('登录成功')
    def test_login_success(self, open_browser):
        """登录成功的用例"""
        # 前置操作：打开浏览器
        driver = open_browser
        driver.get(GD.login_url)
        login_page = LoginPage(driver)
        # 进行登录
        login_page.login(GD.student_user, GD.student_pwd)
        # 断言
        index_page = IndexPage(driver)
        res = index_page.is_login_success()
        try:
            assert res == True
        except AssertionError as e:
            index_page.save_course_code("登录用例_断言失败")
            my_log.error("【登录成功的用例】————>执行失败")
            my_log.exception(e)
            raise e
        else:
            my_log.info("【登录成功的用例】————>执行通过")

    @pytest.mark.parametrize('case', LoginData.login_error_test_data)
    def test_login_error(self, case, open_browser):
        """登录的反向用例"""
        driver = open_browser
        driver.get(GD.login_url)
        login_page = LoginPage(driver)
        # 进行登录
        login_page.login(case['user'], case['pwd'])
        # 断言
        res = login_page.get_error_info()

        try:
            assert res == case['expected']
        except AssertionError as e:
            login_page.error_save_screenshot("登录用例执行失败")
            my_log.error("————>执行失败")
            my_log.exception(e)
            raise e
        else:
            my_log.info("————>执行通过")

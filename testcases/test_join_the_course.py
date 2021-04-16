"""
============================
Author:柠檬班-木森
Time:2021/2/20 20:50
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
=======
"""

import pytest

from common.handler_log import my_log
from datas.test_data import JoinTheCourse
from page.indexPage import IndexPage
from page.loginPage import LoginPage

"""
测试：学生加入课程功能

测试操作的步骤：
    1、老师登录，创建一个课程，提取加课码保存
    2、学生登录，加入课程（输入老师创建课程保存的加课码）
    3、断言    
    
页面：
    登录页面：
        登录操作（老师、学生）
    
    首页：
        1、创建课程（老师）
           涉及到的元素：

        2、提取加课码（老师）
            涉及到的元素：
        
        3、加入课程（学生）
            涉及到的元素：
        
        4、判断是否加课成功（首页是否有最新加入的课程显示）
            涉及到的元素：
        
        5、获取加课失败错误提示     
            
"""
from selenium import webdriver
from datas import global_data as GD


class TestJoinTheCourse:

    def test_add_course_success(self, student_login):
        """加课成功的用例"""
        #  =========老师登录，创建一个课程，提取加课码保存=======
        # driver = webdriver.Chrome()
        # driver.get('https://www.ketangpai.com/User/login.html')
        # # 老师登录
        # login_page = LoginPage(driver)
        # login_page.login(GD.teach_user, GD.teach_pwd)
        # # 老师添加课程
        # index_page = IndexPage(driver)
        # course_name = self.random_course_name()
        # index_page.create_course(course_name)
        # # 老师提取课程的加课码和课程id
        # course_code, course_id = index_page.save_course_code(course_name)
        # print("加课码：", course_code, '课程id', course_id)
        course_code = "BG8W6H"
        course_id = 'MDAwMDAwMDAwMLWGvZWH36do'
        # ==========学生加课================
        driver2 = student_login
        index_page = IndexPage(driver2)
        # 加课
        index_page.join_the_course(course_code)
        # ==========断言========
        res = index_page.is_join_the_course_success(course_id)
        driver2.quit()
        assert res == True

    @pytest.mark.parametrize('case', JoinTheCourse.except_test_data)
    def test_add_course_except_case(self, student_login, case):
        """反向用例:加课失败的用例"""
        # ==========学生加课================
        driver2 = student_login
        index_page = IndexPage(driver2)
        # 加课
        index_page.join_the_course(case['course_code'])
        # ==========断言========
        res = index_page.get_join_the_course_error_info()
        driver2.quit()

        try:
            assert res == case['expected']
        except AssertionError as e:
            index_page.error_save_screenshot("加课用例断言失败")
            my_log.error("————>执行失败")
            my_log.exception(e)
            raise e
        else:
            my_log.info("————>执行通过")

    @staticmethod
    def random_course_name():
        import random
        return '测试课程{}'.format(random.randint(0, 100000))

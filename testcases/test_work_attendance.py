"""
============================
Author:柠檬班-木森
Time:2021/2/23 14:26
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
=======
"""
import pytest

from common.handler_log import my_log

"""
测试操作步骤：
1、老师登录，开启课程考勤，提取考勤码
2、学生登录，输入考勤码考勤
3、老师校验考勤人数是否加1



思路二：

用例的前置：
    老师登录
    学生登录



思路三：







页面
    一、登录页面：
       1、登录操作（老师、学生）
    二、首页
       2、点击进入课程（老师、学生）
       
    三、课程页面
       1、开启考勤（老师）
       
       2、获取考勤码（老师）
       
       2、输入考勤码考勤（学生）
       
       3、获取已考勤人数（老师）  
    
"""
import time
from datas import global_data as GD
from page.indexPage import IndexPage
from page.coursePage import CoursePage


class TestAttend2:
    """测试考勤"""

    def test_teach_start_attend(self, teach_login):
        # --------------老师开启考勤-----------
        my_log.info("=========步骤一：老师开启考勤=======")
        driver = teach_login
        IndexPage(driver).enter_course(GD.course_id)
        # =====课程页面====
        course_page = CoursePage(driver)
        # 新建考勤
        course_page.create_attendance()
        # 获取考勤码
        attend_code = course_page.get_attendance_code()
        # setattr(TestAttend2,'code',attend_code)
        TestAttend2.code = attend_code
        my_log.info("考勤开启成功，考勤码为:{}".format(attend_code))
        s_attend_number = course_page.get_attendance_number()
        # setattr(TestAttend2, 's_number', attend_code)
        TestAttend2.s_number = s_attend_number
        my_log.info("考勤之前，考勤人数为：:{}".format(s_attend_number))

    def test_student_start_attend(self, student_login):
        # ---------------学生进行考勤---------------------------
        my_log.info("=========步骤二：学生进行考勤=======")
        driver2 = student_login
        # 点击进入课程页面
        index_page = IndexPage(driver2)
        index_page.enter_course(GD.course_id)
        # =====课程页面====
        course_page2 = CoursePage(driver2)
        course_page2.work_attendance(TestAttend2.code)

    def test_assert_attend_number(self, teach_login):
        # -----------------数据校验----------------
        my_log.info("=========步骤三：校验考勤人数=======")
        time.sleep(3)
        # 老师获取考勤人数
        driver2 = teach_login
        # 进入课程
        IndexPage(driver2).enter_course(GD.course_id)
        # 点击考勤
        course_page = CoursePage(driver2)
        course_page.enter_attend()
        # 获取考勤页面
        e_attend_number = course_page.get_attendance_number()
        my_log.info("考勤之后，考勤人数为：:{}".format(e_attend_number))
        # 老师关闭考勤
        course_page.close_attendance()
        try:
            assert int(e_attend_number) - int(TestAttend2.s_number) == 1
        except AssertionError as e:
            course_page.error_save_screenshot('考勤用例断言失败')
            my_log.error("【登录成功的用例】————>执行失败")
            my_log.exception(e)
            raise e
        else:
            my_log.info("【登录成功的用例】————>执行通过")

#
# class TestAttend2:
#     """测试考勤"""
#
#     def test_attend_success(self, teach_login, student_login):
#         """测试考勤成功"""
#         # --------------老师开启考勤-----------
#         my_log.info("=========测试考勤功能=======")
#         driver = teach_login
#         IndexPage(driver).enter_course(GD.course_id)
#         # =====课程页面====
#         course_page = CoursePage(driver)
#         # 新建考勤
#         course_page.create_attendance()
#         # 获取考勤码
#         attend_code = course_page.get_attendance_code()
#         my_log.info("考勤开启成功，考勤码为:{}".format(attend_code))
#         s_attend_number = course_page.get_attendance_number()
#         my_log.info("考勤之前，考勤人数为：:{}".format(s_attend_number))
#         # ---------------学生进行考勤---------------------------
#         driver2 = student_login
#         # 点击进入课程页面
#         index_page = IndexPage(driver2)
#         index_page.enter_course(GD.course_id)
#         # =====课程页面====
#         course_page2 = CoursePage(driver2)
#         course_page2.work_attendance(attend_code)
#         # -----------------数据校验----------------
#         time.sleep(3)
#         # 老师获取考勤人数
#         e_attend_number = course_page.get_attendance_number()
#         my_log.info("考勤之后，考勤人数为：:{}".format(e_attend_number))
#         # 老师关闭考勤
#         course_page.close_attendance()
#         try:
#             assert int(e_attend_number) - int(s_attend_number) == 1
#         except AssertionError as e:
#
#             my_log.error("【登录成功的用例】————>执行失败")
#             my_log.exception(e)
#             raise e
#         else:
#             my_log.info("【登录成功的用例】————>执行通过")
#


# class TestAttend:
#     """测试考勤"""
#
#     def test_attend_success(self):
#         """测试考勤成功"""
#         # --------------老师开启考勤-----------
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(15)
#         driver.maximize_window()
#         driver.get(GD.login_url)
#         # 老师登录
#         login_page = LoginPage(driver)
#         login_page.login(GD.teach_user, GD.teach_pwd)
#         # 点击进入课程页面
#         # index_page = IndexPage(driver)
#         # index_page.enter_course(GD.course_id)
#         IndexPage(driver).enter_course(GD.course_id)
#         # =====课程页面====
#         course_page = CoursePage(driver)
#         # 新建考勤
#         course_page.create_attendance()
#         # 获取考勤码
#         attend_code = course_page.get_attendance_code()
#         print("考勤开启成功，考勤码为：", attend_code)
#         s_attend_number = course_page.get_attendance_number()
#         print("考勤之前，考勤人数为：", s_attend_number)
#         # ---------------学生进行考勤---------------------------
#         driver2 = webdriver.Chrome()
#         driver2.maximize_window()
#         driver2.implicitly_wait(15)
#         driver2.get(GD.login_url)
#         # 学生登录
#         login_page = LoginPage(driver2)
#         login_page.login(GD.student_user, GD.student_pwd)
#
#         # 点击进入课程页面
#         index_page = IndexPage(driver2)
#         index_page.enter_course(GD.course_id)
#         # =====课程页面====
#         course_page2 = CoursePage(driver2)
#         course_page2.work_attendance(attend_code)
#
#         # -----------------数据校验----------------
#         time.sleep(3)
#         # 老师获取考勤人数
#         e_attend_number = course_page.get_attendance_number()
#         print("考勤之后，考勤人数为：", e_attend_number)
#         # 老师关闭考勤
#         course_page.close_attendance()
#         assert int(e_attend_number) - int(s_attend_number) == 1
#         driver.quit()
#         driver2.quit()

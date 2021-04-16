"""
============================
Author:柠檬班-木森
Time:2021/2/20 20:13
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
=======
"""
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from locator.index_locator import IndexLocator  as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IndexPage(BasePage):
    """登录页面"""

    def is_login_success(self):
        """判断是否登录成功"""
        try:
            self.get_element(loc.user_loc, "首页_获取用户头像")
        except:
            return False
        else:
            return True

    def create_course(self, course_name):
        """老师身份：创建课程"""
        self.click_element(loc.teach_create_course_loc, "首页_老师点击创建课程")
        self.click_element(loc.teach_create_loc, "首页_老师点击创建")
        self.input_send_keys(loc.course_name_input_loc, course_name, '首页_输出创建的课程名')
        self.click_element(loc.create_loc, '首页_创建课程按钮')

    def save_course_code(self, course_name):
        """
        老师身份：提取加课码和课程的id进行返回
        :param course_name: 新建的课程名
        :return:
        """
        course_loc = '//a[@title="{}"]/../..//div[@class="down-menu"]/span'.format(course_name)
        course_loc_a = '//a[@title="{}"]'.format(course_name)
        course_code = self.get_element_attribute((By.XPATH, course_loc), 'data-code', '首页_获取课程加课码')
        course_id = self.get_element_attribute((By.XPATH, course_loc_a), 'data-id', '首页_获取课程id')
        return course_code, course_id

    def join_the_course(self, course_code):
        """
        学生身份：加入课程
        :param course_code: 加课码
        :return:
        """
        self.click_element(loc.join_the_course_loc, '首页_学生加入课程')
        self.input_send_keys(loc.input_course_code_loc, course_code, '首页_学生输入加课码')
        self.click_element(loc.add_btn_loc, '首页_学生加入课程的加入按钮')

    def is_join_the_course_success(self, course_id):
        """
        学生身份：判断加课是否成功
        :param course_id: 课程id
        :return:
        """
        course_loc = '//dl[@data-id="{}"]'.format(course_id)
        try:
            self.get_element((By.XPATH, course_loc), '首页_查找课程')
        except:
            return False
        else:
            return True

    def get_join_the_course_error_info(self):
        """获取加课失败的提示"""
        ele = self.wait_element_visibility(loc.pop_windows_error_info_loc, '首页_加课失败的错误提示')
        return ele.text

    def enter_course(self, course_id):
        """进入课程"""
        course_loc = '//a[@data-id="{}"]'.format(course_id)
        try:
            self.click_element((By.XPATH, course_loc), '首页_点击课程')
        except:
            return False
        else:
            return True

# class IndexPage(BasePage):
#     """登录页面"""
#
#     def is_login_success(self):
#         """判断是否登录成功"""
#         try:
#             self.driver.find_element(*loc.user_loc)
#         except:
#             return False
#         else:
#             return True
#
#     def create_course(self, course_name):
#         """老师身份：创建课程"""
# self.driver.find_element(*loc.teach_create_course_loc).click()
# self.driver.find_element(*loc.teach_create_loc).click()
# self.driver.find_element(*loc.course_name_input_loc).send_keys(course_name)
# self.driver.find_element(*loc.create_loc).click()
#
#     def save_course_code(self, course_name):
#         """
#         老师身份：提取加课码和课程的id进行返回
#         :param course_name: 新建的课程名
#         :return:
#         """
#         course_loc = '//a[@title="{}"]/../..//div[@class="down-menu"]/span'.format(course_name)
#         course_loc_a = '//a[@title="{}"]'.format(course_name)
#         course_code = self.driver.find_element_by_xpath(course_loc).get_attribute('data-code')
#         course_id = self.driver.find_element_by_xpath(course_loc_a).get_attribute('data-id')
#         return course_code, course_id
#
#     def join_the_course(self, course_code):
#         """
#         学生身份：加入课程
#         :param course_code: 加课码
#         :return:
#         """
#         self.driver.find_element(*loc.join_the_course_loc).click()
#         self.driver.find_element(*loc.input_course_code_loc).send_keys(course_code)
#         self.driver.find_element(*loc.add_btn_loc).click()
#
#     def is_join_the_course_success(self, course_id):
#         """
#         学生身份：判断加课是否成功
#         :param course_id: 课程id
#         :return:
#         """
#         course_loc = '//dl[@data-id="{}"]'.format(course_id)
#         try:
#             self.driver.find_element_by_xpath(course_loc)
#         except:
#             return False
#         else:
#             return True
#
#     def get_join_the_course_error_info(self):
#         """获取加课失败的提示"""
#         ele = WebDriverWait(self.driver, 10, 0.5).until(
#             EC.visibility_of_element_located(
#                 loc.pop_windows_error_info_loc
#             )
#         )
#         return ele.text

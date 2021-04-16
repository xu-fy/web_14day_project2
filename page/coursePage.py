"""
============================
Author:柠檬班-木森
Time:2021/2/23 14:39
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
=======
"""
from common.base_page import BasePage

"""
课程页面

"""
from locator.class_locator import ClsLocator as loc


class CoursePage(BasePage):
    """课程页面"""

    def enter_attend(self):
        """老师身份：点击进入考勤"""
        self.click_element(loc.attend_btn_loc, '课程页面_考勤按钮')
        # 切换iframe
        self.switch_to_iframe_loc(loc.attend_iframe_loc, '课程页面_考勤iframe')

    def create_attendance(self):
        """老师身份：创建考勤"""
        # 点击考勤
        self.enter_attend()
        # 如果之前有考勤未结束则关闭考勤
        try:
            # 点击新建考勤
            self.click_element(loc.new_attend_loc, '课程页面_新建考勤标签')
        except:
            # 关闭考勤
            self.close_attendance()
            # 刷新页面
            self.driver.refresh()
            # 进入考勤页面
            self.enter_attend()
            # 点击新建考勤
            self.click_element(loc.new_attend_loc, '课程页面_创建考勤标签')

        # 点击数字考勤
        self.wait_element_visibility(loc.digit_attend_loc, '课程页面_数字考勤')
        self.click_element(loc.digit_attend_loc, '课程页面_数字考勤')
        # 点击开始考勤
        self.click_element(loc.start_attend_loc, '课程页面_开始考勤')

    def get_attendance_code(self):
        """老师身份：获取考勤码"""
        self.wait_element_visibility(loc.digit_attend_number, desc='课程页面_考勤码数字')

        eles = self.get_elements(loc.digit_attend_number, '课程页面_考勤码数字')
        res = ''
        for ele in eles:
            res += ele.text
        return res

    def get_attendance_number(self):
        """老师身份：获取已考勤人数"""
        self.wait_element_visibility(loc.current_number_loc, '课程页面_已考勤人数')
        number = self.get_element_text(loc.current_number_loc, '课程页面_已考勤人数')
        return number

    def close_attendance(self):
        """老师身份关闭考勤"""
        self.click_element(loc.end_attend_loc, '课程页面_结束考勤')
        self.click_element(loc.pop_end_attend_loc, '课程页面_弹框结束考勤')

    def work_attendance(self, attendance_code):
        """
        学生身份：输入考勤码进行考勤
        :param attendance_code: 签到码
        :return:
        """
        # 等待立即签到可见
        self.wait_element_visibility(loc.go_to_sign_loc, desc='课程页面_立即签到')
        # 点击立即签到
        self.click_element(loc.go_to_sign_loc, desc='课程页面_立即签到')
        # 等待考勤码输入框可见
        self.wait_element_visibility(loc.input_sign_number_loc, desc='课程页面_考勤码输入框')
        # 考勤码输入
        self.input_send_keys(loc.input_sign_number_loc, attendance_code, '课程页面_考勤码输入框')

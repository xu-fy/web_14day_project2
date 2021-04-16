"""
============================
Author:柠檬班-木森
Time:2021/2/23 14:48
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
=======
"""
from selenium.webdriver.common.by import By


class ClsLocator:
    # --------------老师身份----------------
    # 考勤入口
    attend_btn_loc = (By.XPATH, '//span[text()="考勤"]/parent::a')
    # 考勤弹框iframe
    attend_iframe_loc = (By.XPATH, '//iframe[contains(@id,"layui-layer-content")]')
    # 考勤弹框iframe - 新建考勤按钮
    new_attend_loc = (By.XPATH, '//a[text()="新建考勤"]')
    # 考勤弹框iframe - 数字考勤区
    digit_attend_loc = (By.XPATH, '//div[@class="iconarea digit"]')
    # 开始考勤
    start_attend_loc = (By.XPATH, '//div[@id="new-perform"]//a[text()="开始考勤"]')

    # 考勤数字 - 一共匹配4个元素
    digit_attend_number = (By.XPATH, '//div[@class="number-box"]//span')
    # 获取目前考勤的人数
    current_number_loc = (By.XPATH, '//div[@id="number-attend"]//i[@class="ing"]')
    # 结束考勤
    end_attend_loc = (By.XPATH, '//div[@id="number-attend"]//a[text()="结束"]')
    # 弹框中的结束考勤
    pop_end_attend_loc = (By.XPATH, '//*[@id="end-attend"]//a[text()="结束"]')
    # ---------------学生身份----------------

    # ----------  学生角色  -------------
    # 前往考勤的弹出框提示框
    go_to_sign_loc = (By.XPATH, '//*[@id="have-attend"]//a[text()="立即签到"]')
    # 考勤码输入框
    input_sign_number_loc = (By.XPATH, '//input[@id="phoneVer_modalAuthInput"]')

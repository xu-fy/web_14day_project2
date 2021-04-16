"""
============================
Author:柠檬班-木森
Time:2021/2/20 21:07
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
=======
"""
from selenium.webdriver.common.by import By


class IndexLocator:
    # 用户头像信息
    user_loc = (By.ID, 'user')
    # 老师:创建/加入课程
    teach_create_course_loc = (By.XPATH, '//span[text()="+ 创建/加入课程"]')
    # 老师:创建课程
    teach_create_loc = (By.ID, 'addClass')
    # 老师：输入创建的课程名
    course_name_input_loc = (By.XPATH, '//input[@placeholder="请输入课程名称"]')
    # 老师：创建课程按钮
    create_loc = (By.XPATH, '//div[@id="new-class"]//a[@class="sure"]')

    # 学生：加入课程
    join_the_course_loc = (By.XPATH, "//div[text()='+ 加入课程']")
    # 学生：输入加课码
    input_course_code_loc = (By.XPATH, '//input[@placeholder="请输入课程加课验证码"]')
    # 学生：加课点击确定
    add_btn_loc = (By.XPATH, "//a[text()='加入']")
    # 学生：加课识别的弹框提示
    pop_windows_error_info_loc = (By.XPATH, '//div[@id="error-tip"]/span')

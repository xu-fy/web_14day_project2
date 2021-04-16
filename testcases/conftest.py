"""
============================
Author:柠檬班-木森
Time:2021/2/20 20:33
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
=======
"""
from selenium.webdriver import ChromeOptions
import pytest
from common.handler_log import my_log
from selenium import webdriver
from datas import global_data as GD
from page.loginPage import LoginPage


def create_driver(is_headers=True):
    """
    启动driver:默认启动浏览器窗口，is_headers设为False则已无头模式运行
    :param is_headers:  True  or  False
    :return:
    """
    if is_headers:
        driver = webdriver.Chrome()
    else:
        # 设置无头哦浏览器模式
        options = ChromeOptions()
        # 无头模式
        options.add_argument('--headless')
        # 设置窗口大小（无头模式下maximize_window()无法将窗口最大化，需要通过下面的启动参数去设置窗口大小）
        options.add_argument("--window-size=1920,1050")
        # 禁用GPU（可选）
        options.add_argument('--disable-gpu')
        # 非沙箱环境（可选）
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture
def open_browser():
    """打开浏览器"""
    driver = create_driver(is_headers=False)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def teach_login():
    """老师登录"""
    driver = create_driver(is_headers=False)
    driver.implicitly_wait(15)
    driver.maximize_window()
    driver.get(GD.login_url)
    # 老师登录
    my_log.info("====老师身份进行登录====")
    login_page = LoginPage(driver)
    login_page.login(GD.teach_user, GD.teach_pwd)
    yield driver

    driver.quit()


@pytest.fixture
def student_login():
    """学生登录"""
    driver = create_driver(is_headers=False)
    driver.implicitly_wait(15)
    driver.maximize_window()
    driver.get(GD.login_url)
    # 学生登录
    my_log.info("====学生身份进行登录====")
    login_page = LoginPage(driver)
    login_page.login(GD.student_user, GD.student_pwd)
    yield driver

    driver.quit()

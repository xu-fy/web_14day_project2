"""
============================
Author:柠檬班-木森
Time:2021/2/20 20:38
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
=======
"""


class LoginData:
    login_error_test_data = [
        {'user':"","pwd":"nmb_python",'expected':"账号不能为空66"},
        {'user': '408848063@qq.com', "pwd": "", 'expected': "密码不能为空"},
    ]


class JoinTheCourse:
    except_test_data = [
        # 加课码少于6位
        {"course_code": "73Z82", 'expected': "加课验证码必须是6位字符"},
        # 加课码错误
        {"course_code": "000000", 'expected': "该加课码不存在或者已经失效"},
    ]

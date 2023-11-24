import random
import string

from flask import Blueprint, render_template
from exts import  mail
from flask_mail import Message
from flask import request
# /auth
bp = Blueprint("auth",__name__,url_prefix="/auth")
@bp.route("/login")
def login():
    pass

@bp.route("/register")
def register():
    return render_template("register.html")

@bp.route("/captcha/email")
def get_email_captcha():
    # /captcha/email/<email>
    # /captcha/email?email=xxx@qq.com
    email = request.args.get("email")
    # 4/6: 随机数组、宁母、数组和字母的组合
    source = string.digits*4
    captcha = random.sample(source,4)
    # print(captcha)
    captcha="".join(captcha)
    message = Message(subject="知了传课验证码", recipients=[email], body=f"您的验证码是{captcha}")
    mail.send(message)
    # memcached/redis
    # 用数据库表的方式存储
    return "success"

@bp.route("/mail/test")
def mail_test():
    message = Message(subject="邮箱测试",recipients=["ygl2849115967@163.com"],body="这是一条测试邮件")
    mail.send(message)
    return "邮件发送成功"
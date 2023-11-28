from functools import wraps

from flask import g, redirect, url_for


def login_required(func):
    #保func的信息
    @wraps (func)
    def inner(*args,**kwargs):
        if g.user:
            #第一个用来接收任意数量的位置参数，第二个用来接收任意数量的关键字参数
            func(*args,**kwargs)
        else:
            return redirect(url_for("auth.login"))
    return inner
        # @login_required
        # def public_question(quesiton_id):
        #   pass
        # login_required(public_question)(question_id)f
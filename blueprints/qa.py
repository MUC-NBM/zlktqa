from flask import Blueprint, redirect, url_for,request,render_template
bp = Blueprint("qa",__name__, url_prefix="/")#设置为首页
# http://127.0.0.1:5000@bp.route("/")def index():
@bp.route("/")
def index():
    return "这是首页"

@bp.route("/qa/public",methods=['GET','POST'])
def public_qa():
    if request.method =='GET':
        return render_template("public_question.html")
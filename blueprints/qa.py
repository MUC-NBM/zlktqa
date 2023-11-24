from flask import Blueprint
bp = Blueprint("qa",__name__, url_prefix="/")#设置为首页
# http://127.0.0.1:5000@bp.route("/")def index():
@bp.route("/")
def index():
    pass
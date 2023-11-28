from flask import Blueprint, redirect, url_for, request, render_template, g
from .forms import QuestionForm
from models import QuestionModel
from exts  import db
from decorators import  login_required
bp = Blueprint("qa",__name__, url_prefix="/")#设置为首页
# http://127.0.0.1:5000@bp.route("/")def index():
@bp.route("/")
def index():
    questions = QuestionModel.query.order_by(QuestionModel.create_time.desc()).all()
    return render_template("index.html",questions = questions)


@bp.route("/qa/public",methods=['GET','POST'])
@login_required
def public_question():
    if request.method == 'GET':
        return render_template("public_question.html")
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            # TODO:跳转到这篇回答的问答
            return redirect("/")
        else:
            print(form.errors)
            return  redirect(url_for("qa.public"))

@bp.route("/qa/detail/<qa_id>")
def qa_detail(qa_id):
    question = QuestionModel.query.get(qa_id)
    return render_template("detail.html",question=question)

from flask import Blueprint, render_template, request, g, redirect, url_for
from .forms import QuestionForm
from models import QuestionModel
from exts import db
from decorators import login_required

bp = Blueprint("qa", __name__, url_prefix="/")


@bp.route('/')
def index():
    questions = QuestionModel.query.order_by(QuestionModel.create_time.desc()).all()
    return render_template("index.html", questions=questions)


@bp.route('/qa/post', methods=['GET', 'POST'])
@login_required
def post_question():
    if request.method == 'GET':
        return render_template("post_question.html")
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            return redirect("/")
        else:
            print(form.errors)
            return redirect(url_for("qa.post_question"))

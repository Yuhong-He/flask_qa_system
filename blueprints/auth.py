import random
import string

from flask import Blueprint, render_template, jsonify
from exts import mail, db
from flask_mail import Message
from flask import request
from models import EmailCaptchaModel

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route('/login')
def login():
    pass


@bp.route('/register')
def register():
    return render_template("register.html")


@bp.route('/captcha/email', methods=['POST'])
def get_email_captcha():
    email = request.args.get("email")
    source = string.digits * 4
    captcha = random.sample(source, 4)
    captcha = "".join(captcha)
    message = Message(subject="Q&A System Verification Code",
                      recipients=[email],
                      body=f"Your verification code is: {captcha}")
    email_captcha = EmailCaptchaModel(email=email, captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    mail.send(message)
    return jsonify({
        "code": 200,
        "message": "",
        "data": None
    })


@bp.route('/mail/test')
def mail_test():
    message = Message(subject="Send email test", recipients=["heyuhong1273@gmail.com"], body="This is a test mail.")
    mail.send(message)
    return "Mail sent!"

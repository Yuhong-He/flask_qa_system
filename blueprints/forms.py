import wtforms
from wtforms.validators import Email, Length, EqualTo
from models import UserModel, EmailCaptchaModel


class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="Email format incorrect")])
    captcha = wtforms.StringField(validators=[Length(min=4, max=20, message="Captcha incorrect")])
    username = wtforms.StringField(validators=[Length(min=3, max=20, message="Username format incorrect")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="Password format incorrect")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])

    # custom validator
    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="The email has been registered")

    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha = EmailCaptchaModel.query.filter_by(email=email, captcha=captcha).first()
        if not captcha:
            raise wtforms.ValidationError(message="Email or captcha error")


class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="Email format incorrect")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="Password format incorrect")])


class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[Length(min=3, max=100, message="Title format error")])
    content = wtforms.StringField(validators=[Length(min=3, message="Content at least 3 characters")])

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError

def validate_pass_conf(form, field):
    if field.data != form.password.data:
        raise ValidationError('Password and Password Confirmation must match')
        
class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirmation = PasswordField('Password Confirmation', validators=[DataRequired(), validate_pass_conf])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
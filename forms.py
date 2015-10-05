from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Email, Length

class SignupForm(Form):
    firstname = StringField('First name', validators=[DataRequired('Please enter your first name')])
    lastname = StringField('Last name', validators=[DataRequired('Please enter your last name')])
    email = StringField('Email', validators=[DataRequired('Please enter a valid email address'), Email('Please enter a valid email address')])
    password = PasswordField('Password', validators=[DataRequired('Please enter a password'), Length(min=6, message='Please enter a password of at least six characters')])
    submit = SubmitField('Sign up', validators=[DataRequired('Please Input')])

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired('Input your user name'), Email('Input the email address you registered with')])
    password = PasswordField('Password', validators=[DataRequired('Input a valid password')])
    submit = SubmitField('Sign in', )

class AddressForm(Form):
    address = StringField('Address', validators = [DataRequired("Please enter an address.")])
    submit = SubmitField("Search")

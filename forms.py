from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField,SubmitField,BooleanField  #all these r classes
from wtforms.validators import Length,DataRequired,Email,EqualTo


# Forms r created as classes
class Registration_Form(FlaskForm):
    username=StringField('Username', #it is the form label
                         validators=[DataRequired(),Length(min=2,max=20)])
    email=EmailField('Email',
                     validators=[DataRequired(),Email()])
    password=PasswordField('Password',
                           validators=[DataRequired()])
    confirm_pass=PasswordField('Confirm Password',
                               validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign UP!!')




class Login_Form(FlaskForm):
    email=EmailField('Email',
                     validators=[DataRequired(),Email()])
    password=PasswordField('Password',
                           validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Log In')


# We need to setup a secret key to the applcation to prevent the cookie changes, csrf attacks etc
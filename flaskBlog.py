from flask import Flask,render_template,url_for,flash,redirect
from forms import Registration_Form,Login_Form
app = Flask(__name__)

app.config['SECRET_KEY']='skhfkefwa34972rfkhdsvnm4r'

posts=[
    {
        'author' :"AlienX",
        'title' : "Ben 10",
        'content' : "Omnitrix",
        'date_posted' : "5th May 2003"
    },
    {
        'author' :"Spidy",
        'title' : "Marvel 10",
        'content' : "Spider",
        'date_posted' : "21th april 2005"
    }
]

@app.route("/")
@app.route("/home")   #Handles both routes to show same content
def home():
    return render_template('home.html',posts=posts)  #go to html page to add it

@app.route("/about")
def about():
    return render_template('about.html',title="Tennyson")

@app.route("/register",methods=["GET","POST"])
def register():
    form=Registration_Form()
    if form.validate_on_submit(): #this if is to redirect the user to home page with his username displayed
        flash(f'Account created for {form.username.data}!!','success') #Second arg is the class that will be used in the html page
        return redirect(url_for('home')) #home is the fn given here
    return render_template('register.html',title="Register",form=form)

@app.route("/login",methods=["GET","POST"])
def login():
    form=Login_Form()
    # same as regsiter...u can add stuff here too..
        
    return render_template('login.html',title="Login",form=form)


# @app.route('/<name>') #whatever u write in the angular brckets, it goes to the fn below as params
# def display(name):
#     return f'Hello {name}'

# For running without terminal..

if __name__ == '__main__':
    app.run(debug=True)
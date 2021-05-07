#import package that needed in project
from flask import Flask, url_for, redirect, render_template, request, session
from wtforms import Form, fields, validators, form
from wtforms.fields import StringField, PasswordField

from Scripts import Users

#create app and set static folder
app = Flask(__name__,static_folder="static")
#save the root for application
path=app.root_path


#registration forms
class RegistrationForm(form.Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    firstName = fields.StringField(validators=[validators.DataRequired()])
    lastName = fields.StringField(validators=[validators.DataRequired()])

    def usernameValidation(self,username):
        user = Users
        if user.validateUsername(app.root_path, self.username)==False:
            return False
        else:
            return True

#login form
class LoginForm(Form):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

#first route for index page
@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Welcome ' + username + '! <br>' +\
               "<b><br> " \
               "<br><a href = '/profile/"+username+"'>View Profile</a></b>" \
               "<br><a href = '/logout'>Logout Now!!</a></b>" \

    return "You are not logged in <br>" \
           "Login Here: <a href = '/login'>Click here</a><br>" \
           "Register here: <a href='/signup'>Click Here</a>"


@app.route('/signup', methods=('GET', 'POST'))
def getSignup():
    form = RegistrationForm()
    if request.method == 'POST':
        username = request.form['username']
        if form.usernameValidation(username)==False:
            password = request.form['password']
            email = request.form['email']
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            user = Users
            user.insertData(username, password, email, firstname, lastname)
            return redirect("/")
        else:
            error="Username found already"
            return render_template("error.html",error=error,redirect=url_for("getSignup"))

    return render_template("login.html",form=form)


@app.route('/login', methods=('GET', 'POST'))
def getLogin():
    form =LoginForm()
    if request.method == 'POST':
        user = Users
        if (user.validateUsername(path,request.form['username']) and user.validatePassword(path,request.form['password'])) == True:
                return redirect("/")
        else:
            error = "Username and Password not found! Try login again"
            return render_template("error.html", error=error)

    return render_template("login.html",form=form)


@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))


@app.route("/profile/<name>")
def getprofile(name):
    print (name)
    if str(session['username']) == str(name):
        user = Users
        return render_template("profile.html", profile=user.getUserProfile(path,name))
    else:
        return "You are not logged in <br><a href = '/login'></b>" + \
       "click here to log in</b></a>"


if __name__ == '__main__':
    app.run(debug=True)
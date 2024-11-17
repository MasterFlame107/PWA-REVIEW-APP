from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET', 'POST'])
def login():
    return render_template("login.html", b=True)

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up',methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 4:
            flash('Email is too short, Must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('First Name is too short, Must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 7:
            flash('password is too short, Must be greater than 6 characters.', category='error')
        else:
            flash('Account created!', category='success')
            #add user to database
            pass
    return render_template("sign_up.html")
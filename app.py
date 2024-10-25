from flask import Flask, render_template, redirect, session, flash
from models import connect_db, db, User
from forms import UserForm


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///flask_feedback"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "feedbacktothemask"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.app_context().push()
connect_db(app)
db.create_all()


@app.route('/')
def home_page():
    '''Shows home page'''

    form = UserForm()

    return render_template('index.html', form=form)


@app.route('/register', methods = ['POST', 'GET'])
def register_user():
    form = UserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        
        new_user =User.register(username, password, email,first_name,last_name)
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        flash('Welcome! Sucessfully created your Account')
        return redirect('/secret')
    
    else:
        return render_template('register.html', form=form)
    
@app.route('/secret')
def show_secrets():
    '''Shows user's secret'''

    return render_template('secret.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5503, debug=True)
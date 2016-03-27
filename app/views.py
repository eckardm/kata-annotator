from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Max'}
	annotations = [  # fake array of annotations
		{ 
		    'author': {'nickname': 'Max'}, 
		    'body': 'https://www.youtube.com/watch?v=pVYZkKXVOQ8' 
		},
		{ 
		    'author': {'nickname': 'Max'}, 
		    'body': 'https://www.youtube.com/watch?v=47LbO7k_cRE' 
		}
	]
	return render_template(
		'index.html',
		title='Home',
		user=user,
		annotations=annotations)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

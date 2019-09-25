#all page routes for application
from flask import render_template 
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def landing():
	return render_template('landing.html')

@app.route('/base')
def base():
	return render_template('base.html')
	
@app.route('/goals')
def goals():
	return render_template('goals.html')

@app.route('/projects')
def projects():
	return render_template('projects.html')
	
@app.route('/events')
def events():
	return render_template('events.html')

@app.route('/about')
def about():
	return render_template('about.html')
	
@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html',form=form)
'''
@app.route('/myProfile/<username>')
@login_required
def profile(username):
	return render_template('profile.html')
	'''
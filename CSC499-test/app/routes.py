#all page routes for application
from app import app

@app.route('/')
@app.route('/index')
def landing():
	return "Hello World!"

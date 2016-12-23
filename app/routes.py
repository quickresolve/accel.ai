from flask import *
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')



@app.route('/workshops')
def workshops():
    return render_template('workshops.html', title='Workshops')

@app.route('/blog')
def blog():
    return render_template('blog.html', title='Blog')

@app.route('/culture')
def culture():
      return render_template('culture.html', title='Culture')

@app.route('/curriculum')
def curriculum():
    return "curriculum"




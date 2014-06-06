from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
  return 'Index page'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
  return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
  return 'User %s' % username

@app.route('/projects/')
def projects():
  return 'Projects page'

if __name__ == '__main__':
  app.debug = True
  app.run()

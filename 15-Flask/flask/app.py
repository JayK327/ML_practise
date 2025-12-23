from flask import Flask
'''
This is a simple Flask application that demonstrates how to create a web server.
WSGI (Web Server Gateway Interface) is a specification that allows web servers to communicate with web applications in Python.
'''

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Home page"

@app.route('/index')
def welcome1():
    return "Welcome to the Index page"

if __name__=='__main__':
    app.run(debug=True)


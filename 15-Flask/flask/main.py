from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    return "<head><title>Home Page</title></head><body><h1>Welcome to the Home page</h1></body>"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=='__main__':
    app.run(debug=True)


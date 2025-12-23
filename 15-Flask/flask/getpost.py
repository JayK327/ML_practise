from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def welcome():
    return "<head><title>Home Page</title></head><body><h1>Welcome to the Home page</h1></body>"

@app.route('/index',methods=['GET'])   #by default GET method is used
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        return f"Name: {name} <br> Email: {email}"
    return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        return f"Name: {name} <br> Email: {email}"
    return render_template('form.html')

if __name__=='__main__':
    app.run(debug=True)


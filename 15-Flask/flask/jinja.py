#Build url dynamically
#variable rule
#jinja2 template engine
'''
{{}}: exoression to print output in html
{%...%} conditions,loops
{#...#}: This is for comment
'''
from flask import Flask, render_template,request, redirect ,url_for
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

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        return f"Name: {name} <br> Email: {email}"
    return render_template('form.html')

#variable rule
@app.route('/success/<int:score>')  #by default any parmaeter given is treated string
def success(score):    
    res=""
    if score>=50:
        res="You have passed"
    else:
        res="You have failed"
    return render_template('result.html',results=res)

@app.route('/successres/<int:score>') 
def successres(score):    
    res=""
    if score>=50:
        res="You have passed"
    else:
        res="You have failed"

    exp={'score':score,'res':res}
    return render_template('result1.html',results=exp)

#if condition
@app.route('/successif/<int:score>')  
def successif(score):    
    return render_template('result.html',results=score)

@app.route('/fail/<int:score>')  
def fail(score):    
    return render_template('result.html',results=score)

#Build url dynamically
@app.route('/submit1',methods=['POST','GET'])
def submit1():
    if request.method=='POST':
        science=float(request.form['Science'])
        maths=float(request.form['Maths'])
        english=float(request.form['English'])
        total=science+maths+english
        avg=total/3
    else:
        return render_template('getresult.html')
    return redirect(url_for('successif',score=avg))

if __name__=='__main__':
    app.run(debug=True)


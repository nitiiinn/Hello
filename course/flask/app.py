from flask import Flask,render_template
# it acts as the web server gateway interface 

app=Flask(__name__)  
# WSGI application

@app.route('/')
def welcome():
    return "Welcome to this page"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')
    

if __name__=="__main__": 
    app.run(debug=True)

from flask import Flask,render_template,request,redirect,url_for
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
    

@app.route("/submit",methods=["GET,POST"])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f"Hello {name}"
    return render_template('form.html')

# # Variable Rule
@app.route("/success/<int:score>")
def success(score):
    res=''
    if score>=33:
        res='PASSED'
    else:
        res="FAILED"

    return render_template('result.html',results=res)

# using loop statements inside html file instead of python file while passing the value into the html file
@app.route("/successif/<int:score>")
def successif(score):
    return render_template('result.html',results=score)


@app.route("/getresult", methods=['GET', 'POST'])
def successurl():
    total_score = 0
    if request.method == "POST":
        science = int(request.form['science'])   
        maths = int(request.form['maths'])       
        english = int(request.form['english'])   
        total_score = int((science + maths + english) / 3)
        return redirect(url_for('successif', score=total_score))
    
    return render_template("getresult.html")
  


if __name__=="__main__": 
    app.run(debug=True)
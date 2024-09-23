from flask import Flask,render_template,request,redirect,url_for #Render template works with Jinja2 functionality.

app=Flask(__name__) # App initialization. Instance of flask class which is WSI application.


@app.route("/")
def welcome():
    return "Hello world!!!Bye!Goodbye"

@app.route("/index",methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hi {name}'
    return render_template('form.html')

@app.route('/finalresult/<name>/<marks>',methods=['GET','POST'])
def finalresult(name,marks):
    return f'{name} got {marks}'

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        marks=request.form['marks']
        # return f'Hi {name}'
    return redirect(url_for('finalresult',name=name,marks=marks))

@app.route('/mark/<marks>')  #We can pass data type specific data EX:<int:marks>
def mark(marks):
    return f'The marks you got is {marks}'

@app.route('/success/<marks>') #Have used jinja template in the success.html file
def success(marks):
    return render_template('success.html',marks=marks)

@app.route('/result',methods=['GET','POST'])
def result():
    dic={"marks":49,"Result":"Pass"}
    return render_template('res.html',dic=dic)

if __name__=="__main__": #This is the point where course start
    app.run(debug=True)





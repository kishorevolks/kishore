from flask import *
app=Flask(__name__)
app.secret_key='hg'

@app.route('/Pcust',methods=['POST'])
def mypostmthd():
    name=request.form['fname']
    email=request.form['em']
    phno=request.form['ph']
    print(name,email,phno)
    return "succes "



@app.route('/s')
def reg():
    return render_template('fro.html')

@app.route('/suc',methods=['POST','GET'])
def get_data():
    if request.method=="POST":
        data=request.form
        return data
    else:
        return render_template('fro.html')
    
@app.route('/sc')
def set_cook():
    res=make_response("<h1>Cookie is set </h1>")
    res.set_cookie('fname','ammu')
    return res
    
@app.route('/gc')
def get_cook():
    name=request.cookies.get('fname')
    return name 

@app.route('/ss')
def set_sess():
    res=make_response('session is set')

    session['phone']=123455
    return res

@app.route('/gss')
def get_sess():
    if 'phone' in session:
        return str(session['phone'])
    




@app.route('/l')
def reg():
    return render_template('work.html')

@app.route('/f',methods=['POST','GET'])
def get_data():
    if request.method=="POST":
        data=request.form
        return data
    else:
        return render_template('work.html')


if __name__=="__main__":
    app.run(debug=True)
from flask import *

app=Flask(__name__)

@app.route('/admin')
def admin1():
    return 'welcome admin'

@app.route('/student')
def student1():
    return 'welcome student'

@app.route('/teacher')
def teacher1():
    return 'welcome teacher'


@app.route('/user/<uname>')
def user(uname):
    if uname=="admin":
        return redirect(url_for('admin1'))
    elif uname=="student":
        return redirect(url_for('student1'))
    elif uname=="teacher":
        return redirect(url_for('teacher1'))
    else:
        return "invalid user"



@app.route('/j/<job>')
def mypage(job):
    name="anu"
    return render_template("d1.html",uname=name,j=job)


@app.route('/<int:mul>')
def multi(mul):
 return render_template('multi1.html',num=mul)

if __name__=="__main__":
    app.run(debug=True)
    
    

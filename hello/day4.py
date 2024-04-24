from flask import *
from flask_mail import *

app=Flask(__name__)
app.secret_key="abb"

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=="GET":
        return render_template('day4.html')
    else:
        er="ffffffff"
        f=request.files['dp']
        f.save(f.filename)
        # return 'success'
        a=1
        if a==1:
            flash('successfully saved')
        else:
            flash('error')
        return render_template('day4.html',error=er)        





app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']="kishorea562@gmail.com"
app.config['MAIL_PASSWORD']='ykga ezec lkxt frus'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail=Mail(app)

@app.route('/sm')
def smail():
    msg=Message('subject',sender='kishorea562@gmail.com',recipients=['akishore811@gmail.com'])
    msg.body='hii friend'
    mail.send(msg)
    return 'success'


if __name__=="__main__":
    app.run(debug=True)
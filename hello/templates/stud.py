from flask import *
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def stud_reg():
    if request.method=='POST':
        n=request.form['fname']
        p=request.form['ph']
        e=request.form['em']
        
    

if __name__=="__main__":
    app.run(debug=True)
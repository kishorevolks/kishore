from flask import *
app=Flask(__name__)
@app.route('/Gstud',methods=['GET'])
def mygetmthd():
    name=request.args.get('fname')
    email=request.args.get('em')
    phno=request.args.get('ph')
    print(name,email,phno)
    return "succes"

if __name__=="__main__":
    app.run(debug=True)

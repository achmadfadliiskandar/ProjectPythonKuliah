from flask import *
app = Flask(__name__)

@app.route('/login',methods=['POST'])
def login():
    uname = request.form['uname']
    passwordd = request.form['passwordd']
    if uname == "fadli" and passwordd == "qwerty":
        return "Welcome %s" %uname
    
if __name__ == "__main__":
    app.run(debug=True)
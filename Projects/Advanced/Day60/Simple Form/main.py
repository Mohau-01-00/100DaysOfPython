from flask import Flask,render_template,request
from datetime import datetime




app = Flask(__name__)

@app.route('/')
def home():

    return render_template("form.html")

@app.route("/login",methods=["POST"])
def recieve_data():
    name=request.form['firstname']
    password=request.form['password']


    return render_template("post.html",name=name,password=password)

         



if __name__ == "__main__":
    app.run(debug=True)
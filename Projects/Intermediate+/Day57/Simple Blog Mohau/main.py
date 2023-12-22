from flask import Flask, render_template
import requests



app = Flask(__name__)

@app.route('/')
def home():

    url="https://api.npoint.io/c790b4d5cab58020d391"
    data=requests.get(url).json()
    return render_template("index.html",posts=data)
   


@app.route("/post")

def show_post():

    url="https://api.npoint.io/c790b4d5cab58020d391"
    data=requests.get(url).json()

   
    return render_template("post.html",posts=data)
   
 

if __name__ == "__main__":
    app.run(debug=True)

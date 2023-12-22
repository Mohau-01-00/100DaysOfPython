from flask import Flask,render_template,request
from datetime import datetime
import requests



url=" https://api.npoint.io/48369a40c3d8417532f3"
data=requests.get(url).json()

app = Flask(__name__)

@app.route('/')
def home():
 

    return render_template("index.html",posts=data)




@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

#need to study the below

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)
         

if __name__ == "__main__":
    app.run(debug=True)
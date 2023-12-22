from flask import Flask, render_template,request
import requests
import smtplib



    
# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/48369a40c3d8417532f3").json()


app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact",methods=["POST","GET"])

 
def contact():
    if request.method=="POST":
        
        data=request.form
    
        message="Successfully sent your message"
        try:
            my_email="mohaumasukela@gmail.com"
            password="nfinuwzdiiylckuu"

            with smtplib.SMTP('smtp.gmail.com',587) as connection:

                connection.starttls()
                connection.login(my_email,password)

            connection.sendmail(from_addr="Blog Page",to_addrs="mohau.masukela@vodacom.co.za",
                                msg=f"Subject:Daily Motivation\n\n{data}")
        except OSError:

            return render_template("contact.html",msg=message)
    else:
        message="Contact Me"
        return render_template("contact.html",msg=message)


        

        

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)





if __name__ == "__main__":
    app.run(debug=True, port=5001)

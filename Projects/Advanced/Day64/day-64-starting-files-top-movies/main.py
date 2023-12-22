from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField,FloatField
from wtforms.validators import DataRequired,ValidationError,URL
import requests

from dotenv import load_dotenv
load_dotenv()
import os

MOVIE_DB_API_KEY = "APP_KEY"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie.db"
db = SQLAlchemy()
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True ,nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200) ,nullable=False)
    rating = db.Column(db.Float,nullable=False)
    ranking = db.Column(db.Integer,nullable=False)
    review = db.Column(db.String(300),nullable=False)
    img_url= db.Column(db.String,nullable=False)


with app.app_context():

    db.create_all()


class MovieForm(FlaskForm):
    

    title=StringField('Movie Title',validators=[DataRequired()])
    description=StringField('Description',validators=[DataRequired()])
    rating=FloatField('Rating out of 10 e.g 7.5 ',validators=[DataRequired()])
    review=StringField('Your Review',validators=[DataRequired()])
    ranking=IntegerField('Ranking',validators=[DataRequired()])
    year=IntegerField('Year',validators=[DataRequired()])
    image=StringField('Add Image',validators=[DataRequired(),URL()])

    
    submit = SubmitField('Done')


class EditForm(FlaskForm):

    rating=FloatField('Rating out of 10 e.g 7.5 ',validators=[DataRequired()])
    review=StringField('Your Review',validators=[DataRequired()])

    submit = SubmitField('Done')

# New Find Movie Form
class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")




app.config['SECRET_KEY'] = 'MohauTopMovies'
Bootstrap5(app)



@app.route("/")
def home():
    movie = Movie.query.all()
    return render_template("index.html",movies=movie)



#you can call the movie_id anything,it will make sense once you link it on
#the jinja/html form it will be as below....
#"{{url_for('edit',movie_id=movie.id)}}"
@app.route("/<int:movie_id>",methods=("POST","GET"))
def edit(movie_id):
    form=EditForm()
    
    movie=Movie.query.get_or_404(movie_id)
    if form.validate_on_submit():
        rating_update=request.form['rating']
        review_update=request.form["review"]


        movie.rating=rating_update
        movie.review=review_update
        db.session.add(movie)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('edit.html',form=form,movie=movie)





@app.route("/add", methods=["GET", "POST"])
def add():
    form = FindMovieForm()
    
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        print(response.text)
        data = response.json()["results"]
        return render_template("select.html", options=data)
      
    return render_template("add.html", form=form)


@app.route("/<int:movie_id>/delete",methods=("POST","GET"))

def delete(movie_id):
     movie=Movie.query.get_or_404(movie_id)
     db.session.delete(movie)
     db.session.commit()

     return redirect(url_for('home'))

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        
        # Redirect to /edit route
        return redirect(url_for("rate_movie", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)

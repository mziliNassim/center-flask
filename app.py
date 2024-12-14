from flask import Flask, render_template, url_for
from data.categories import categories
from data.courses import coursesList
from data.testimonials import testimonials
from data.team import team

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
  return render_template('home.html',
    title='home',
    categories=categories,
    courses=coursesList,
    testimonials=testimonials
  )

@app.route("/about")
def about():
  return render_template('about.html' ,
    title='about',
    team=team
  )

@app.route("/courses")
def courses():
  return render_template("courses.html",
    title='courses',
    courses=coursesList,
    categories=categories
  )

@app.route("/courses/<categorie>")
def coursesByCategorie(categorie):
  filtered_courses = [cours for cours in coursesList if cours["categorie"] == categorie]
  return render_template(
    "courses.html",
    title='courses',
    courses=filtered_courses,
    categories=categories,
    active=categorie
  )

@app.route("/courses/<categorie>/<coursId>")
def cours(categorie, coursId):
  for cours in coursesList :
    if int(coursId) == cours['id'] :
      return render_template("cours.html", cours=cours)
  return render_template(
    "courses.html",
    title='courses',
    courses=coursesList,
    categories=categories
  )

@app.route("/contact")
def contact():
  return render_template(
    "contact.html",
    title='contact'
  )

@app.route("/login")
def login():
  return render_template(
    "login.html",
    title='login'
  )

@app.route("/register")
def register():
  return render_template(
    "register.html",
    title='register'
  )

@app.route("/<path:subpath>")
def not_found(subpath):
  return f'Page Not Found: {subpath}'

if __name__ == "__main__":
  app.run(debug=True)
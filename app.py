from flask import Flask, render_template,session, url_for,flash, request, redirect

from config.validData import validLoginData, validRegisterData

from data.categories import categories
from data.courses import coursesList
from data.testimonials import testimonials
from data.team import team

import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
@app.route("/home")
def home():
  return render_template('home.html',
    title='home',
    categories=categories,
    courses=coursesList,
    testimonials=testimonials,
    alert={"message" : ""}
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

@app.route("/<path:subpath>")
def not_found(subpath):
  return f'Page Not Found: {subpath}'

@app.route("/login", methods=['GET', 'POST'])
def login():
  loginAlert = {"message" : "", "type" : "warning"}
  if request.method == "POST" :
    username = request.form['username']
    password = request.form['password']

    loginAlert = validLoginData(username, password)
    if (loginAlert["valid"]) :
      flash(loginAlert["message"], loginAlert["type"])
      session["user"] = username
      return redirect(url_for("home"))
  return render_template(
    "login.html",
    title='login',
    loginAlert=loginAlert
  )

@app.route("/register", methods=['GET', 'POST'])
def register():
  registerAlert = {"message" : "", "type" : "warning"}
  if request.method == "POST" :
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirmPpassword = request.form['confirm_password']
    registerAlert = validRegisterData(username, email, password, confirmPpassword)

  return render_template(
    "register.html",
    title='register',
    registerAlert=registerAlert
  )

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
  app.run(debug=True)
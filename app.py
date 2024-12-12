from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home() :
  return render_template('home.html')

@app.route("/about")
def about() :
  return "about Page"

@app.route("/<path:subpath>")
def not_found(subpath):
    return 'NotFound Page'

if __name__ == "__main__" :
  app.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home() :
  return "home Page"

@app.route("/about")
def about() :
  return "about Page"

@app.route("/<path:subpath>")
def not_found(subpath):
    return 'NotFound Page'

if __name__ == "__main__" :
  app.run(debug=True)
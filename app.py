from flask import Flask, render_template, url_for

app = Flask(__name__)

categories = [
  {
    "id": 1,
    "categorie": "Web Static",
    "desc": "Development of static websites using fundamental web technologies like HTML, CSS, and JavaScript.",
    "link": "#",
    "icon": "bi bi-code-slash",
  },
  {
    "id": 2,
    "categorie": "Front-End",
    "desc": "Building user interfaces and ensuring responsive design with frameworks like React, Angular, or Vue.js.",
    "link": "#",
    "icon": "bi bi-braces-asterisk",
  },
  {
    "id": 3,
    "categorie": "Back-End",
    "desc": "Server-side development using programming languages such as Python, Node.js, or PHP to manage application logic and databases.",
    "link": "#",
    "icon": "bi bi-braces",
  },
  {
    "id": 4,
    "categorie": "Databases",
    "desc": "Managing data storage and retrieval using SQL and NoSQL databases like MySQL, PostgreSQL, or MongoDB.",
    "link": "#",
    "icon": "bi bi-database",
  },
  {
    "id": 5,
    "categorie": "UX/UI Design",
    "desc": "Creating intuitive and aesthetically pleasing designs that enhance user experience and interface usability.",
    "link": "#",
    "icon": "bi bi-file-earmark-fill",
  },
  {
    "id": 6,
    "categorie": "DevOps & Microservices",
    "desc": "Streamlining development workflows and managing microservice architectures using tools like Docker, Kubernetes, and CI/CD pipelines.",
    "link": "#",
    "icon": "bi bi-git",
  },
]

coursesList = [
  {
    "id": 1,
    "cours": "React JS",
    "desc": "Learn to build dynamic and responsive user interfaces with React, a popular JavaScript library for front-end development.",
    "img": "1.png",
    "url": "/courses/reactjs",
  },
  {
    "id": 2,
    "cours": "Flask",
    "desc": "Explore the power of Flask, a lightweight Python framework for building web applications and APIs.",
    "img": "2.png",
    "url": "/courses/flask",
  },
  {
    "id": 3,
    "cours": "Express JS",
    "desc": "Master back-end development with Express, a fast and minimalist framework for Node.js applications.",
    "img": "3.png",
    "url": "/courses/expressjs",
  },
  {
    "id": 4,
    "cours": "CSS / SASS",
    "desc": "Enhance your styling skills by learning CSS and SASS to create professional, responsive, and maintainable designs.",
    "img": "4.png",
    "url": "/courses/css-sass",
  },
  {
    "id": 5,
    "cours": "Django",
    "desc": "Delve into Django, a high-level Python framework, to develop robust and scalable web applications.",
    "img": "5.png",
    "url": "/courses/django",
  },
  {
    "id": 6,
    "cours": "Vue JS",
    "desc": "Discover Vue.js, a progressive JavaScript framework, to create seamless and interactive user interfaces.",
    "img": "6.png",
    "url": "/courses/vuejs",
  },
]

testimonials = [
  {
    "id": 1,
    "testimonial": "Enrolling in this program was the best decision of my life. The instructors are knowledgeable, and the practical projects gave me hands-on experience that prepared me for real-world challenges.",
    "author_name": "Karim TEST",
    "author_img": "pers1.jpg",
    "author_categorie": "Front-End",
  },
  {
    "id": 2,
    "testimonial": "The courses are well-structured and engaging. I gained valuable skills in UX/UI design that allowed me to secure my dream job in the tech industry.",
    "author_name": "Iman TEST",
    "author_img": "pers2.jpg",
    "author_categorie": "UX/UI Design",
  },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', categories=categories, courses=coursesList, testimonials=testimonials, title='home')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/courses")
def courses():
    return render_template("courses.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/<path:subpath>")
def not_found(subpath):
    return f'Page Not Found: {subpath}'

if __name__ == "__main__":
    app.run(debug=True)
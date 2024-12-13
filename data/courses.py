
coursesList = [
  {
    "id": 1,
    "cours": "React JS",
    "desc": "Learn to build dynamic and responsive user interfaces with React, a popular JavaScript library for front-end development.",
    "img": "1.png",
    "url": "/courses/reactjs",
    "categorie": "Front-End",
    "logo": "react.png",
    "totalTime" : "1 Months, 2 Weeks",
    "lessons": [
      {
        "id": 1,
        "lesson": "Introduction to React",
        "subLessons": [
          "What is React?",
          "Benefits of React",
          "React vs. other frameworks (Angular, Vue)",
          "Setting up a React development environment",
          "Your first 'Hello World' in React"
        ]
      },
      {
        "id": 2,
        "lesson": "Understanding JSX",
        "subLessons": [
          "What is JSX?",
          "JSX syntax and embedding expressions",
          "Differences between JSX and HTML",
          "Advantages of using JSX"
        ]
      },
      {
        "id": 3,
        "lesson": "React Components",
        "subLessons": [
          "Functional Components",
          "Class Components",
          "Props and how to pass data between components",
          "Component composition and reuse"
        ]
      },
      {
        "id": 4,
        "lesson": "State and Lifecycle",
        "subLessons": [
          "Understanding state and its importance",
          "Setting and updating state with useState",
          "Lifecycle methods in class components",
          "Using useEffect for side effects in functional components"
        ]
      },
      {
        "id": 5,
        "lesson": "Event Handling in React",
        "subLessons": [
          "Adding event listeners to components",
          "Handling user input (e.g., forms, buttons)",
          "Binding methods in class components",
          "Synthetic events and event pooling"
        ]
      },
      {
        "id": 6,
        "lesson": "React Router",
        "subLessons": [
          "Setting up React Router",
          "Route components and dynamic routing",
          "Navigation between pages using <Link> and <NavLink>",
          "URL parameters and query strings",
          "Protected routes and route guards"
        ]
      },
      {
        "id": 7,
        "lesson": "Managing Forms",
        "subLessons": [
          "Controlled components vs. uncontrolled components",
          "Handling form inputs, validation, and submission",
          "Using third-party libraries like Formik or React Hook Form"
        ]
      },
      {
        "id": 8,
        "lesson": "Styling in React",
        "subLessons": [
          "Inline styles and CSS classes",
          "CSS Modules for scoped styles",
          "Using libraries like TailwindCSS, Bootstrap, or Material-UI",
          "Styled-components for CSS-in-JS"
        ]
      },
      {
        "id": 9,
        "lesson": "Working with APIs",
        "subLessons": [
          "Fetching data with fetch and axios",
          "Handling loading states and errors",
          "Displaying API data in components",
          "POST, PUT, DELETE requests for CRUD operations"
        ]
      },
      {
        "id": 10,
        "lesson": "State Management",
        "subLessons": [
          "Understanding props drilling",
          "Introduction to Context API",
          "Redux basics: actions, reducers, store",
          "Using Redux Toolkit for efficient state management"
        ]
      },
      {
        "id": 11,
        "lesson": "React Hooks",
        "subLessons": [
          "Introduction to Hooks: Why Hooks?",
          "Core Hooks: useState, useEffect, useRef, useContext",
          "Advanced Hooks: useReducer, useCallback, useMemo, useLayoutEffect",
          "Creating custom hooks"
        ]
      },
      {
        "id": 12,
        "lesson": "Optimizing Performance",
        "subLessons": [
          "Code-splitting with React.lazy and Suspense",
          "Memoization with React.memo and useMemo",
          "Optimizing re-renders with useCallback",
          "Using React Profiler to identify performance bottlenecks"
        ]
      },
      {
        "id": 13,
        "lesson": "Testing in React",
        "subLessons": [
          "Introduction to testing frameworks (Jest, React Testing Library)",
          "Writing unit tests for components",
          "Snapshot testing",
          "Mocking API requests",
          "End-to-end testing with tools like Cypress"
        ]
      },
      {
        "id": 14,
        "lesson": "Advanced React Patterns",
        "subLessons": [
          "Higher-order components (HOCs)",
          "Render props pattern",
          "Compound components pattern",
          "Controlled vs. uncontrolled components"
        ]
      },
      {
        "id": 15,
        "lesson": "Deploying React Applications",
        "subLessons": [
          "Building production-ready React apps",
          "Deployment options: Vercel, Netlify, GitHub Pages, AWS, Heroku",
          "Best practices for React app deployment"
        ]
      },
      {
        "id": 16,
        "lesson": "Exploring Ecosystem and Libraries",
        "subLessons": [
          "Integrating third-party libraries (e.g., Chart.js, D3.js)",
          "Working with form libraries (Formik, React Hook Form)",
          "Using animation libraries like Framer Motion or React Spring"
        ]
      },
      {
        "id": 17,
        "lesson": "Building a Project",
        "subLessons": [
          "End-to-end project: Building a functional application",
          "Structuring and organizing code",
          "Version control with Git and GitHub",
          "Preparing for code reviews"
        ]
      }
    ]
  },
  {
  "id": 2,
  "cours": "Flask",
  "desc": "Explore the power of Flask, a lightweight Python framework for building web applications and APIs.",
  "img": "2.png",
  "url": "/courses/flask",
  "categorie": "Back-End",
  "logo": "flask.png",
  "totalTime": "2 Month",
  "lessons": [
      {
        "id": 1,
        "lesson": "Introduction to Flask",
        "subLessons": [
          "What is Flask?",
          "Installing Flask and setting up your environment",
          "The difference between Flask and other Python frameworks (e.g., Django)",
          "Building your first Flask application"
        ]
      },
      {
        "id": 2,
        "lesson": "Understanding Flask Routing",
        "subLessons": [
          "What is routing in Flask?",
          "Creating and handling routes with @app.route",
          "Dynamic routes with parameters",
          "URL converters and route constraints"
        ]
      },
      {
        "id": 3,
        "lesson": "Working with Templates",
        "subLessons": [
          "Introduction to Jinja2 templating engine",
          "Using placeholders and variables in templates",
          "Control structures in Jinja2 (loops, conditionals)",
          "Extending templates with inheritance"
        ]
      },
      {
        "id": 4,
        "lesson": "Handling Forms and Requests",
        "subLessons": [
          "Understanding HTTP methods (GET, POST, PUT, DELETE)",
          "Handling form submissions",
          "Using Flask-WTF for form validation",
          "Working with request data (query strings, form data)"
        ]
      },
      {
        "id": 5,
        "lesson": "Flask and Databases",
        "subLessons": [
          "Connecting Flask to a database (SQLite, MySQL, or PostgreSQL)",
          "Using Flask-SQLAlchemy for ORM",
          "Performing CRUD operations",
          "Database migrations with Flask-Migrate"
        ]
      },
      {
        "id": 6,
        "lesson": "Building RESTful APIs",
        "subLessons": [
          "Introduction to REST architecture",
          "Creating RESTful endpoints in Flask",
          "Returning JSON responses",
          "Using Flask-RESTful or Flask-Smorest for API development"
        ]
      },
      {
        "id": 7,
        "lesson": "User Authentication and Authorization",
        "subLessons": [
          "Understanding authentication vs. authorization",
          "Setting up Flask-Login for user authentication",
          "Handling sessions and cookies",
          "Implementing role-based access control"
        ]
      },
      {
        "id": 8,
        "lesson": "Error Handling and Debugging",
        "subLessons": [
          "Working with Flask's built-in error handling",
          "Customizing error pages (404, 500, etc.)",
          "Debugging Flask applications",
          "Using Flask-DebugToolbar for development"
        ]
      },
      {
        "id": 9,
        "lesson": "Flask and Front-End Integration",
        "subLessons": [
          "Serving static files (CSS, JS, images)",
          "Integrating front-end frameworks (Bootstrap, TailwindCSS)",
          "Working with JavaScript and AJAX in Flask",
          "Building interactive UIs with Flask and front-end libraries"
        ]
      },
      {
        "id": 10,
        "lesson": "Deployment and Production",
        "subLessons": [
          "Preparing a Flask app for deployment",
          "Deploying Flask applications to Heroku, AWS, or Vercel",
          "Using Gunicorn or uWSGI with Flask",
          "Best practices for Flask app security"
        ]
      },
      {
        "id": 11,
        "lesson": "Advanced Flask Features",
        "subLessons": [
          "Using Flask-Blueprints for modular applications",
          "Working with Flask-Caching to improve performance",
          "Understanding Flask-SocketIO for real-time communication",
          "Building asynchronous applications with Flask"
        ]
      },
      {
        "id": 12,
        "lesson": "Project: Building a Complete Flask Application",
        "subLessons": [
          "Defining the project structure",
          "Creating user authentication and authorization",
          "Integrating a database for storing and retrieving data",
          "Building RESTful APIs and front-end integration",
          "Deploying the project to a live server"
        ]
      }
    ]
  },
  {
    "id": 3,
    "cours": "Express JS",
    "desc": "Master back-end development with Express, a fast and minimalist framework for Node.js applications.",
    "img": "3.png",
    "url": "/courses/expressjs",
    "categorie": "Back-End",
    "logo": "express.png",
    "totalTime": "2 Month, 1 Weeks",
    "lessons": [
      {
        "id": 1,
        "lesson": "Introduction to Express",
        "subLessons": [
          "What is Express JS?",
          "Setting up a basic Express application",
          "Understanding the Express application structure",
          "Installing and configuring dependencies with npm"
        ]
      },
      {
        "id": 2,
        "lesson": "Routing in Express",
        "subLessons": [
          "Understanding HTTP methods (GET, POST, PUT, DELETE)",
          "Creating basic routes with Express",
          "Handling dynamic route parameters",
          "Using Express Router for modular routing"
        ]
      },
      {
        "id": 3,
        "lesson": "Middleware in Express",
        "subLessons": [
          "What is middleware?",
          "Using built-in middleware (express.json, express.static)",
          "Creating custom middleware functions",
          "Error handling middleware"
        ]
      },
      {
        "id": 4,
        "lesson": "Handling Forms and Requests",
        "subLessons": [
          "Handling form data with POST requests",
          "Accessing query parameters and request bodies",
          "Working with `req.body` and `req.query`",
          "Using third-party middleware (e.g., body-parser)"
        ]
      },
      {
        "id": 5,
        "lesson": "Templating with Express",
        "subLessons": [
          "Introduction to template engines (e.g., Pug, EJS)",
          "Setting up Pug or EJS with Express",
          "Passing dynamic data to views",
          "Rendering templates and using layout files"
        ]
      },
      {
        "id": 6,
        "lesson": "Connecting to a Database",
        "subLessons": [
          "Setting up a database (MongoDB, MySQL, PostgreSQL)",
          "Connecting Express to MongoDB with Mongoose",
          "Creating and managing database models",
          "Performing CRUD operations with Express and MongoDB"
        ]
      },
      {
        "id": 7,
        "lesson": "Building RESTful APIs with Express",
        "subLessons": [
          "Understanding RESTful API principles",
          "Creating RESTful routes in Express",
          "Handling JSON responses",
          "Authentication in APIs using JWT"
        ]
      },
      {
        "id": 8,
        "lesson": "User Authentication in Express",
        "subLessons": [
          "Setting up user authentication with Passport.js",
          "Understanding sessions and cookies",
          "Handling user login and registration",
          "JWT-based authentication for stateless APIs"
        ]
      },
      {
        "id": 9,
        "lesson": "Error Handling in Express",
        "subLessons": [
          "Catching and handling errors in Express",
          "Using try-catch for async code",
          "Creating custom error pages",
          "Handling 404 and 500 errors"
        ]
      },
      {
        "id": 10,
        "lesson": "File Uploads in Express",
        "subLessons": [
          "Handling file uploads with Multer",
          "Saving files to the server",
          "Validating uploaded files (size, type)",
          "Serving uploaded files"
        ]
      },
      {
        "id": 11,
        "lesson": "Security in Express",
        "subLessons": [
          "Preventing security vulnerabilities (XSS, CSRF, SQL injection)",
          "Using Helmet.js to secure Express apps",
          "Configuring CORS for cross-origin requests",
          "Rate limiting and brute-force protection"
        ]
      },
      {
        "id": 12,
        "lesson": "Testing Express Applications",
        "subLessons": [
          "Introduction to testing frameworks (Mocha, Chai)",
          "Writing unit tests for Express routes",
          "Testing middleware and error handling",
          "End-to-end testing with Supertest"
        ]
      },
      {
        "id": 13,
        "lesson": "Deploying Express Applications",
        "subLessons": [
          "Preparing Express app for production",
          "Deploying to Heroku, AWS, or DigitalOcean",
          "Using PM2 for process management",
          "Optimizing Express for performance"
        ]
      },
      {
        "id": 14,
        "lesson": "Building a Complete Project",
        "subLessons": [
          "Structuring a full Express application",
          "Implementing user authentication and database models",
          "Creating RESTful endpoints and API documentation",
          "Deploying the complete project to a live server"
        ]
      }
    ]
  },
  {
    "id": 4,
    "cours": "SASS",
    "desc": "Enhance your styling skills by learning SASS to create professional, responsive, and maintainable designs.",
    "img": "4.png",
    "url": "/courses/sass",
    "categorie": "Web Static",
    "logo": "sass.png",
    "totalTime": "3 Weeks",
    "lessons": [
      {
        "id": 1,
        "lesson": "Introduction to SASS",
        "subLessons": [
          "What is SASS and why use it?",
          "Installing and setting up SASS in your project",
          "Differences between CSS and SASS",
          "Compiling SASS to CSS"
        ]
      },
      {
        "id": 2,
        "lesson": "Variables in SASS",
        "subLessons": [
          "Declaring variables in SASS",
          "Using variables for colors, fonts, and dimensions",
          "Overriding variables for themes and styles",
          "Best practices for naming conventions"
        ]
      },
      {
        "id": 3,
        "lesson": "Nesting in SASS",
        "subLessons": [
          "What is nesting and why it's useful?",
          "How to nest CSS selectors in SASS",
          "Limitations and best practices for nesting",
          "Nesting pseudo-classes and pseudo-elements"
        ]
      },
      {
        "id": 4,
        "lesson": "SASS Mixins",
        "subLessons": [
          "What are mixins and how to use them?",
          "Passing parameters to mixins",
          "Creating reusable mixins for common patterns",
          "Using mixins with media queries"
        ]
      },
      {
        "id": 5,
        "lesson": "SASS Inheritance",
        "subLessons": [
          "Understanding inheritance in SASS",
          "Using `@extend` for inheritance",
          "The advantages and limitations of `@extend`",
          "Creating clean and reusable styles with inheritance"
        ]
      },
      {
        "id": 6,
        "lesson": "Partials and Imports",
        "subLessons": [
          "What are SASS partials?",
          "How to organize your SASS files with partials",
          "Using `@import` to include partials",
          "Avoiding issues with multiple imports"
        ]
      },
      {
        "id": 7,
        "lesson": "SASS Functions and Operations",
        "subLessons": [
          "Creating and using functions in SASS",
          "Performing operations (addition, subtraction, multiplication) on values",
          "Color manipulation functions in SASS",
          "Math functions for dynamic styling"
        ]
      },
      {
        "id": 8,
        "lesson": "Loops and Conditionals in SASS",
        "subLessons": [
          "Using loops in SASS for repetitive patterns",
          "Creating conditional statements in SASS",
          "Using `@if`, `@else`, `@for`, and `@each`",
          "Dynamic styling with loops and conditionals"
        ]
      },
      {
        "id": 9,
        "lesson": "Responsive Design with SASS",
        "subLessons": [
          "Setting up breakpoints in SASS",
          "Using mixins for media queries",
          "Building responsive layouts with flexible styles",
          "Mobile-first design with SASS"
        ]
      },
      {
        "id": 10,
        "lesson": "SASS with Frameworks",
        "subLessons": [
          "Integrating SASS with Bootstrap or Foundation",
          "Customizing SASS variables in frameworks",
          "Using SASS with CSS frameworks for faster development",
          "Combining SASS with pre-built grid systems"
        ]
      },
      {
        "id": 11,
        "lesson": "SASS Optimization and Best Practices",
        "subLessons": [
          "Optimizing SASS for performance",
          "Minifying compiled CSS files",
          "SASS architecture patterns (SMACSS, BEM, etc.)",
          "Best practices for maintainable and scalable SASS code"
        ]
      },
      {
        "id": 12,
        "lesson": "Project: Building a SASS-based Website",
        "subLessons": [
          "Defining project structure and planning styles",
          "Using SASS variables, mixins, and inheritance in the project",
          "Creating a fully responsive website with SASS",
          "Deploying and optimizing the final project"
        ]
      }
    ]
  },
  {
    "id": 5,
    "cours": "Django",
    "desc": "Delve into Django, a high-level Python framework, to develop robust and scalable web applications.",
    "img": "5.png",
    "url": "/courses/django",
    "categorie": "Back-End",
    "logo": "django.png",
    "totalTime": "1 Months, 2 Weeks",
    "lessons": [
      {
        "id": 1,
        "lesson": "Introduction to Django",
        "subLessons": [
          "What is Django and why use it?",
          "Setting up a Django project",
          "Understanding Django project structure",
          "Creating your first Django app"
        ]
      },
      {
        "id": 2,
        "lesson": "Django Models and Databases",
        "subLessons": [
          "Understanding Django ORM (Object-Relational Mapping)",
          "Creating and managing models",
          "Database migrations in Django",
          "Performing CRUD operations with Django models"
        ]
      },
      {
        "id": 3,
        "lesson": "Django Views and Templates",
        "subLessons": [
          "What are views in Django?",
          "Creating views for different HTTP methods",
          "Using Django templates for rendering HTML",
          "Template inheritance and passing data to templates"
        ]
      },
      {
        "id": 4,
        "lesson": "URLs and Routing in Django",
        "subLessons": [
          "Defining URL patterns in Django",
          "Using dynamic URLs with path converters",
          "Reverse URL lookup in Django",
          "Organizing URL patterns with include()"
        ]
      },
      {
        "id": 5,
        "lesson": "Forms in Django",
        "subLessons": [
          "Handling forms with Django forms module",
          "Validating form data",
          "Using ModelForm for creating forms from models",
          "Working with form submissions and error handling"
        ]
      },
      {
        "id": 6,
        "lesson": "Authentication and Authorization",
        "subLessons": [
          "Setting up user authentication in Django",
          "Creating user registration, login, and logout functionality",
          "User roles and permissions",
          "Implementing custom authentication mechanisms"
        ]
      },
      {
        "id": 7,
        "lesson": "Working with Static and Media Files",
        "subLessons": [
          "Serving static files (CSS, JavaScript, images) in Django",
          "Handling media files (uploads and downloads)",
          "Configuring static and media file settings",
          "Using third-party libraries for managing file uploads"
        ]
      },
      {
        "id": 8,
        "lesson": "Django Admin Interface",
        "subLessons": [
          "Introduction to Django's built-in admin interface",
          "Customizing the Django admin panel",
          "Registering models with the admin site",
          "Using Django admin for data management"
        ]
      },
      {
        "id": 9,
        "lesson": "Django REST Framework (DRF)",
        "subLessons": [
          "Introduction to Django REST Framework",
          "Building RESTful APIs with DRF",
          "Serializers for converting model data to JSON",
          "Handling authentication and permissions in DRF"
        ]
      },
      {
        "id": 10,
        "lesson": "Testing in Django",
        "subLessons": [
          "Introduction to testing in Django",
          "Writing unit tests for views, models, and forms",
          "Using Django's test client for simulating requests",
          "Testing Django APIs with DRF's test utilities"
        ]
      },
      {
        "id": 11,
        "lesson": "Django Security Best Practices",
        "subLessons": [
          "Securing your Django application (XSS, CSRF, SQL injection)",
          "Django's built-in security features",
          "Managing user sessions and cookies securely",
          "Handling sensitive data and secrets in production"
        ]
      },
      {
        "id": 12,
        "lesson": "Django Deployment",
        "subLessons": [
          "Preparing your Django project for production",
          "Deploying Django to a web server (Heroku, AWS, DigitalOcean)",
          "Using WSGI servers like Gunicorn for production",
          "Configuring your Django project for security and performance"
        ]
      },
      {
        "id": 13,
        "lesson": "Scaling Django Applications",
        "subLessons": [
          "Understanding the architecture of scalable Django applications",
          "Caching strategies in Django",
          "Using Celery for background tasks",
          "Optimizing database queries for large applications"
        ]
      },
      {
        "id": 14,
        "lesson": "Building a Complete Django Project",
        "subLessons": [
          "Defining the project structure and requirements",
          "Implementing user authentication and database models",
          "Creating views, forms, and APIs",
          "Deploying the project and maintaining the application"
        ]
      }
    ]
  },
  {
    "id": 6,
    "cours": "Vue JS",
    "desc": "Discover Vue.js, a progressive JavaScript framework, to create seamless and interactive user interfaces.",
    "img": "6.png",
    "url": "/courses/vuejs",
    "categorie": "Front-End",
    "logo": "vue.png",
    "totalTime": "1 Month, 1 Weeks",
    "lessons": [
      {
        "id": 1,
        "lesson": "Introduction to Vue.js",
        "subLessons": [
          "What is Vue.js and why use it?",
          "Setting up a Vue.js project with Vue CLI",
          "Vue.js architecture and basic concepts",
          "Creating your first Vue component"
        ]
      },
      {
        "id": 2,
        "lesson": "Vue.js Directives",
        "subLessons": [
          "Understanding Vue.js directives (v-bind, v-if, v-for)",
          "Using `v-model` for two-way data binding",
          "Conditional rendering with `v-if`, `v-else`, and `v-show`",
          "Rendering lists with `v-for`"
        ]
      },
      {
        "id": 3,
        "lesson": "Vue.js Data and Methods",
        "subLessons": [
          "Understanding Vue's reactive data model",
          "Defining and using data properties",
          "Methods and computed properties",
          "Handling events with `v-on`"
        ]
      },
      {
        "id": 4,
        "lesson": "Vue.js Components",
        "subLessons": [
          "Creating and using components in Vue.js",
          "Component communication (props, events)",
          "Component lifecycle hooks",
          "Dynamic component rendering with `component` tag"
        ]
      },
      {
        "id": 5,
        "lesson": "Vue.js Forms and Validation",
        "subLessons": [
          "Handling form inputs and bindings",
          "Two-way data binding with `v-model`",
          "Validating form fields in Vue.js",
          "Using custom form validation methods"
        ]
      },
      {
        "id": 6,
        "lesson": "Vue Router",
        "subLessons": [
          "What is Vue Router and why use it?",
          "Setting up Vue Router in a Vue project",
          "Defining routes and navigation",
          "Using nested routes and dynamic routing"
        ]
      },
      {
        "id": 7,
        "lesson": "State Management with Vuex",
        "subLessons": [
          "What is Vuex and why use it?",
          "Setting up Vuex in a Vue.js project",
          "State, mutations, actions, and getters in Vuex",
          "Handling global state with Vuex"
        ]
      },
      {
        "id": 8,
        "lesson": "Vue.js Lifecycle Methods",
        "subLessons": [
          "Understanding Vue component lifecycle",
          "Common lifecycle hooks (created, mounted, updated, destroyed)",
          "When to use each lifecycle hook",
          "Managing side effects during component lifecycle"
        ]
      },
      {
        "id": 9,
        "lesson": "Vue.js Animations and Transitions",
        "subLessons": [
          "Using Vue.js transitions for visual effects",
          "Handling CSS transitions and animations",
          "Integrating third-party libraries for complex animations",
          "Using Vue's transition hooks for custom effects"
        ]
      },
      {
        "id": 10,
        "lesson": "Vue.js Best Practices",
        "subLessons": [
          "Organizing Vue components for maintainability",
          "Managing large applications with Vue.js",
          "Code splitting and lazy loading in Vue.js",
          "Optimizing performance in Vue.js applications"
        ]
      },
      {
        "id": 11,
        "lesson": "Vue.js with APIs",
        "subLessons": [
          "Making HTTP requests with Axios",
          "Handling API responses and errors",
          "Using Vue's async/await for async operations",
          "Integrating external APIs into Vue.js applications"
        ]
      },
      {
        "id": 12,
        "lesson": "Testing in Vue.js",
        "subLessons": [
          "Introduction to testing Vue components",
          "Unit testing Vue components with Jest",
          "Mocking HTTP requests in tests",
          "End-to-end testing with Cypress"
        ]
      },
      {
        "id": 13,
        "lesson": "Deploying Vue.js Applications",
        "subLessons": [
          "Preparing your Vue.js application for production",
          "Deploying Vue.js apps to Netlify, Vercel, and other services",
          "Optimizing your app for performance and SEO",
          "Configuring Vue.js for server-side rendering (SSR)"
        ]
      },
      {
        "id": 14,
        "lesson": "Building a Complete Vue.js Project",
        "subLessons": [
          "Defining project scope and structure",
          "Building components and implementing routing",
          "State management with Vuex",
          "Deploying the completed project to a live server"
        ]
      }
    ]
  },
  {
    "id": 7,
    "cours": "Figma",
    "desc": "Learn Figma, a powerful design tool, to create user-friendly and visually appealing UI/UX designs with ease.",
    "img": "7.png",
    "url": "/courses/figma",
    "categorie": "UX-UI Design",
    "logo": "figma.png",
    "totalTime": "1 Month",
    "lessons": [
      {
        "id": 1,
        "lesson": "Introduction to Figma",
        "subLessons": [
          "What is Figma and why is it popular?",
          "Setting up your Figma account and workspace",
          "Overview of the Figma interface",
          "Creating your first design file"
        ]
      },
      {
        "id": 2,
        "lesson": "Designing with Shapes and Frames",
        "subLessons": [
          "Working with basic shapes (rectangles, circles, lines)",
          "Using frames for structuring designs",
          "Creating and grouping objects",
          "Aligning and distributing elements"
        ]
      },
      {
        "id": 3,
        "lesson": "Typography in Figma",
        "subLessons": [
          "Setting up text styles in Figma",
          "Adjusting font size, weight, and line height",
          "Working with text alignment and spacing",
          "Using Google Fonts and custom fonts in Figma"
        ]
      },
      {
        "id": 4,
        "lesson": "Colors and Gradients",
        "subLessons": [
          "Choosing and applying colors in Figma",
          "Creating color palettes and themes",
          "Using gradients for background effects",
          "Working with color opacity and blending modes"
        ]
      },
      {
        "id": 5,
        "lesson": "Working with Images and Icons",
        "subLessons": [
          "Importing and placing images in Figma",
          "Resizing and cropping images",
          "Using vector icons and integrating them into designs",
          "Creating custom icons in Figma"
        ]
      },
      {
        "id": 6,
        "lesson": "Design Systems in Figma",
        "subLessons": [
          "What is a design system?",
          "Creating and managing reusable components",
          "Using Figma's Styles for consistent design",
          "Building and maintaining a design system library"
        ]
      },
      {
        "id": 7,
        "lesson": "Prototyping in Figma",
        "subLessons": [
          "Creating interactive prototypes in Figma",
          "Adding links and animations between frames",
          "Using smart animate for transitions",
          "Previewing and testing prototypes"
        ]
      },
      {
        "id": 8,
        "lesson": "Collaboration and Feedback in Figma",
        "subLessons": [
          "Inviting collaborators to your Figma files",
          "Real-time design collaboration",
          "Using Figma's commenting and feedback features",
          "Managing version history and file updates"
        ]
      },
      {
        "id": 9,
        "lesson": "Design Handoff in Figma",
        "subLessons": [
          "Preparing designs for developers",
          "Using Figma's Inspect panel for design handoff",
          "Exporting assets from Figma",
          "Creating style guides and design documentation"
        ]
      },
      {
        "id": 10,
        "lesson": "Advanced Figma Techniques",
        "subLessons": [
          "Using auto-layout for responsive designs",
          "Creating complex interactions and animations",
          "Working with constraints and grids",
          "Mastering Figma's vector editing tools"
        ]
      },
      {
        "id": 11,
        "lesson": "Figma for UX/UI Design Process",
        "subLessons": [
          "Understanding the UX/UI design process",
          "User research and wireframing in Figma",
          "Creating user flows and journey maps",
          "Designing and testing interactive prototypes"
        ]
      },
      {
        "id": 12,
        "lesson": "Designing a Complete UI/UX Project in Figma",
        "subLessons": [
          "Defining project scope and requirements",
          "Sketching and wireframing your project",
          "Building high-fidelity UI designs in Figma",
          "Prototyping and presenting the final project"
        ]
      }
    ]
  },
  {
    "id": 8,
    "cours": "Docker",
    "desc": "Master Docker, a containerization platform, to streamline application development, deployment, and scaling.",
    "img": "8.png",
    "url": "/courses/docker",
    "categorie": "DevOps & Microservices",
    "logo": "docker.png",
    "totalTime": "1 Months, 3 Weeks",
    "lessons": [
      {
        "id": 1,
        "lesson": "Introduction to Docker",
        "subLessons": [
          "What is Docker and why use it?",
          "Setting up Docker on your machine",
          "Understanding Docker images, containers, and Docker Hub",
          "Creating and running your first Docker container"
        ]
      },
      {
        "id": 2,
        "lesson": "Docker Images and Containers",
        "subLessons": [
          "What is a Docker image?",
          "Building custom Docker images with Dockerfile",
          "Running containers from images",
          "Managing Docker containers (start, stop, remove)"
        ]
      },
      {
        "id": 3,
        "lesson": "Working with Docker Volumes",
        "subLessons": [
          "What are Docker volumes?",
          "Using volumes for persistent data storage",
          "Mounting volumes in Docker containers",
          "Managing Docker volumes"
        ]
      },
      {
        "id": 4,
        "lesson": "Docker Networking",
        "subLessons": [
          "Understanding Docker networking concepts",
          "Creating and managing Docker networks",
          "Connecting containers through networks",
          "Using bridge, host, and overlay networks"
        ]
      },
      {
        "id": 5,
        "lesson": "Docker Compose",
        "subLessons": [
          "What is Docker Compose?",
          "Setting up multi-container applications with Docker Compose",
          "Defining services and networks in docker-compose.yml",
          "Scaling services using Docker Compose"
        ]
      },
      {
        "id": 6,
        "lesson": "Docker Registries and Docker Hub",
        "subLessons": [
          "What is a Docker registry?",
          "Pushing and pulling images to/from Docker Hub",
          "Using private Docker registries",
          "Managing Docker images on Docker Hub"
        ]
      },
      {
        "id": 7,
        "lesson": "Advanced Docker Features",
        "subLessons": [
          "Using Docker Multi-Stage builds",
          "Building optimized Docker images",
          "Understanding Docker layers and caching",
          "Working with Docker Swarm for orchestration"
        ]
      },
      {
        "id": 8,
        "lesson": "Docker in Development Environments",
        "subLessons": [
          "Using Docker for local development environments",
          "Setting up a development stack with Docker Compose",
          "Using Docker for testing and continuous integration",
          "Managing dependencies in a Dockerized environment"
        ]
      },
      {
        "id": 9,
        "lesson": "Docker in Production",
        "subLessons": [
          "Deploying Docker containers to production",
          "Docker orchestration with Kubernetes and Docker Swarm",
          "Best practices for Docker container security",
          "Monitoring and logging Docker containers"
        ]
      },
      {
        "id": 10,
        "lesson": "Docker for Microservices",
        "subLessons": [
          "Introduction to microservices architecture",
          "How Docker facilitates microservices deployment",
          "Building and managing microservices with Docker",
          "Scaling microservices with Docker Swarm or Kubernetes"
        ]
      },
      {
        "id": 11,
        "lesson": "Docker Security Best Practices",
        "subLessons": [
          "Understanding Docker security concerns",
          "Securing Docker images and containers",
          "Using Docker Content Trust and security scanning",
          "Implementing least privilege in Docker containers"
        ]
      },
      {
        "id": 12,
        "lesson": "CI/CD with Docker",
        "subLessons": [
          "Setting up continuous integration with Docker",
          "Building Docker images in CI pipelines",
          "Deploying Docker containers in continuous deployment pipelines",
          "Integrating Docker with Jenkins, GitLab CI, and other CI tools"
        ]
      },
      {
        "id": 13,
        "lesson": "Docker for Cloud Deployment",
        "subLessons": [
          "Deploying Docker containers to AWS, Google Cloud, or Azure",
          "Using Docker with cloud-native services (ECS, GKE, AKS)",
          "Scaling applications with Docker in the cloud",
          "Managing cloud infrastructure with Docker"
        ]
      },
      {
        "id": 14,
        "lesson": "Building and Deploying a Complete Docker Project",
        "subLessons": [
          "Defining project scope and requirements",
          "Building a multi-container application with Docker Compose",
          "Testing and deploying the Dockerized app",
          "Managing the production environment with Docker"
        ]
      }
    ]
  },
  {
    "id": 9,
    "cours": "Adobe XD",
    "desc": "Get started with Adobe XD, a vector-based tool for designing and prototyping user interfaces and experiences.",
    "img": "9.png",
    "url": "/courses/adobexd",
    "categorie": "UX-UI Design",
    "logo": "adobexd.png",
    "totalTime": "3 Month",
    "lessons": [
      {
        "id": 1,
        "lesson": "Introduction to Adobe XD",
        "subLessons": [
          "What is Adobe XD and its purpose?",
          "Setting up Adobe XD and creating your first file",
          "Navigating the Adobe XD interface",
          "Understanding artboards and the design workspace"
        ]
      },
      {
        "id": 2,
        "lesson": "Designing with Shapes and Text",
        "subLessons": [
          "Working with vector shapes and the shape tools",
          "Using the text tool for typography in XD",
          "Aligning, spacing, and distributing elements",
          "Applying colors and styles to shapes and text"
        ]
      },
      {
        "id": 3,
        "lesson": "Creating and Using Components",
        "subLessons": [
          "What are components and why use them?",
          "Creating reusable components",
          "Using the Assets panel to manage components",
          "Making changes to components and auto-updating instances"
        ]
      },
      {
        "id": 4,
        "lesson": "Prototyping in Adobe XD",
        "subLessons": [
          "Introduction to prototyping in Adobe XD",
          "Creating interactive links between artboards",
          "Setting up triggers and actions for interactions",
          "Previewing and testing prototypes"
        ]
      },
      {
        "id": 5,
        "lesson": "Working with UI Kits and Design Systems",
        "subLessons": [
          "Using Adobe XD UI kits to speed up design",
          "Integrating design systems into your projects",
          "Managing reusable assets and styles",
          "Consistency in design with shared styles and components"
        ]
      },
      {
        "id": 6,
        "lesson": "Working with Images and Icons",
        "subLessons": [
          "Importing and managing images in Adobe XD",
          "Masking images with shapes",
          "Using vector icons and customizing them",
          "Optimizing images for web and mobile use"
        ]
      },
      {
        "id": 7,
        "lesson": "Responsive Design in Adobe XD",
        "subLessons": [
          "Creating adaptive layouts for different screen sizes",
          "Using responsive resize for dynamic designs",
          "Setting constraints and padding in artboards",
          "Previewing responsive designs on different devices"
        ]
      },
      {
        "id": 8,
        "lesson": "Advanced Prototyping in Adobe XD",
        "subLessons": [
          "Creating advanced interactions and animations",
          "Using auto-animate for smooth transitions",
          "Linking multiple artboards for complex flows",
          "Integrating voice triggers and gestures"
        ]
      },
      {
        "id": 9,
        "lesson": "Collaborating and Sharing with Adobe XD",
        "subLessons": [
          "Sharing your design for feedback and review",
          "Collaborating in real time with multiple designers",
          "Using the Creative Cloud Libraries for asset management",
          "Exporting designs and assets for developers"
        ]
      },
      {
        "id": 10,
        "lesson": "User Testing and Feedback in Adobe XD",
        "subLessons": [
          "Setting up a user testing environment",
          "Recording user feedback within Adobe XD",
          "Making design improvements based on feedback",
          "Conducting usability tests and iterating designs"
        ]
      },
      {
        "id": 11,
        "lesson": "Integrating Adobe XD with Other Tools",
        "subLessons": [
          "Integrating Adobe XD with Photoshop and Illustrator",
          "Using third-party plugins in Adobe XD",
          "Working with wireframing tools and handoff tools",
          "Exporting and importing assets across platforms"
        ]
      },
      {
        "id": 12,
        "lesson": "Building a Complete UI/UX Project in Adobe XD",
        "subLessons": [
          "Planning and defining your project scope",
          "Designing a fully functional prototype",
          "Creating and refining interactive elements",
          "Finalizing the design for presentation"
        ]
      }
    ]
  },
  {
    "id": 10,
    "cours": "MongoDB",
    "desc": "Explore MongoDB, a NoSQL database, to efficiently store, query, and analyze large sets of unstructured data.",
    "img": "10.png",
    "url": "/courses/mongodb",
    "categorie": "Databases",
    "logo": "mongodb.png",
    "totalTime": "2 Weeks",
    "lessons": [
      {
        "id": 1,
        "lesson": "Introduction to MongoDB",
        "subLessons": [
          "What is MongoDB and how does it differ from relational databases?",
          "Installing and setting up MongoDB",
          "Understanding MongoDB’s NoSQL architecture",
          "Connecting to MongoDB using Mongo Shell and MongoDB Compass"
        ]
      },
      {
        "id": 2,
        "lesson": "MongoDB Data Model",
        "subLessons": [
          "Understanding MongoDB's document-based data model",
          "Collections and documents in MongoDB",
          "Storing different data types in MongoDB",
          "Designing data models for NoSQL databases"
        ]
      },
      {
        "id": 3,
        "lesson": "CRUD Operations in MongoDB",
        "subLessons": [
          "Creating documents in MongoDB using insertOne and insertMany",
          "Reading data from MongoDB with find and findOne",
          "Updating documents using updateOne, updateMany, and replaceOne",
          "Deleting documents with deleteOne and deleteMany"
        ]
      },
      {
        "id": 4,
        "lesson": "MongoDB Query Language (MQL)",
        "subLessons": [
          "Basic queries using find() and query operators",
          "Sorting, limiting, and skipping results",
          "Using projection to limit data fields",
          "Filtering documents with comparison, logical, and element operators"
        ]
      },
      {
        "id": 5,
        "lesson": "Indexing in MongoDB",
        "subLessons": [
          "What are indexes in MongoDB and why are they important?",
          "Creating and using indexes in MongoDB",
          "Understanding compound and multi-key indexes",
          "Optimizing query performance with indexes"
        ]
      },
      {
        "id": 6,
        "lesson": "Aggregation Framework in MongoDB",
        "subLessons": [
          "Introduction to MongoDB's aggregation framework",
          "Using aggregation operators like $match, $group, and $project",
          "Building complex queries with $unwind, $lookup, and $sort",
          "Optimizing aggregation queries"
        ]
      },
      {
        "id": 7,
        "lesson": "Data Validation in MongoDB",
        "subLessons": [
          "Schema validation in MongoDB",
          "Using JSON Schema for validation",
          "Enforcing data integrity with validation rules",
          "Validating and managing document structure"
        ]
      },
      {
        "id": 8,
        "lesson": "MongoDB Security and Authentication",
        "subLessons": [
          "Setting up authentication and authorization in MongoDB",
          "Understanding MongoDB user roles and privileges",
          "Using SSL for secure connections",
          "Best practices for MongoDB security"
        ]
      },
      {
        "id": 9,
        "lesson": "Replication and Sharding in MongoDB",
        "subLessons": [
          "What is replication and why is it important?",
          "Setting up replica sets in MongoDB",
          "Understanding the replication process and failover",
          "Sharding in MongoDB for horizontal scaling"
        ]
      },
      {
        "id": 10,
        "lesson": "Backup and Restore in MongoDB",
        "subLessons": [
          "Backing up data in MongoDB using mongodump and MongoDB Atlas",
          "Restoring data with mongorestore",
          "Managing backups in replica sets and sharded clusters",
          "Automating backups in MongoDB"
        ]
      },
      {
        "id": 11,
        "lesson": "Performance Tuning in MongoDB",
        "subLessons": [
          "Monitoring MongoDB performance with tools like mongostat and mongotop",
          "Optimizing queries and indexes",
          "Analyzing slow queries with MongoDB logs",
          "Configuring MongoDB for better performance"
        ]
      },
      {
        "id": 12,
        "lesson": "Integrating MongoDB with Node.js",
        "subLessons": [
          "Setting up MongoDB with Node.js and Mongoose",
          "Performing CRUD operations from a Node.js application",
          "Using MongoDB's native Node.js driver",
          "Creating and managing MongoDB schemas in Mongoose"
        ]
      },
      {
        "id": 13,
        "lesson": "MongoDB Atlas: Cloud Database Service",
        "subLessons": [
          "What is MongoDB Atlas and how does it work?",
          "Creating and managing clusters on MongoDB Atlas",
          "Configuring MongoDB Atlas for high availability and performance",
          "Integrating MongoDB Atlas with your application"
        ]
      },
      {
        "id": 14,
        "lesson": "Building and Deploying a MongoDB-based Application",
        "subLessons": [
          "Defining project scope and requirements",
          "Building a full-stack application with MongoDB",
          "Connecting a front-end application to MongoDB",
          "Deploying the MongoDB application to production"
        ]
      }
    ]
  }
]

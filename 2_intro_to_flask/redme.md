This is the start of a simple flask app

# Installing flask

- pip install flask

and we are ready to go!

# making the app

> create a python file
> import the flask module

```python
from flask import Flask
```

> create an instance of the flask class

```python
app = Flask(__name__)
```

> create a funstion that will be rendered and add the app.route decorator

```python
@app.route('')
def home():
   return 'Hello World'
```

> run the app

````python
if __name__ == '__main__':
   app.run()```
````

whatever's returned in the fucntion will be rendered and displayed in the browser
*here the app.route decorator is used to tell the flask to map the url to the function
*inside the function you can add a path that will be rendered to the browser
\*and display the string 'Hello World'

for example:

```python
@app.route('/hello')
def hello():
   return 'Hello World'
```

> the app.route have '/hello' as the path.

    so the url will be 'http://127.0.0.1:5000/hello' will render the hello function
    that will display 'Hello World'

    > you can run the app to see the result.

# Rendering HTML files

- lets make a html file but first we need to create a folder called templates
- inside the templates folder we need to create a HTML file, in my case home.html
- open the HTML file and add some html code.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
```

- Save the file.

- now go to the flask app file and import the render_template function

```python
from flask import render_template
```

- now edit the home function.

```python
@app.route('/')
def home():
   return render_template('home.html')
```

- here you dont need to add the file path to templates/home.html, because flask will look for the file in the templates folder automatically.

- So, we can make another page called about.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>About</h1>
  </body>
</html>
```

- we can now render this page.

```python
@app.route('/about')
def about():
    return render_template(about.html)
```

# Navigation Menu

- A navigation bar will have a link to the home page and a link to the about page,we will call it layout.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>Layout</h1>
    <nav>
      <a href="/">Home</a>
      <a href="/about">About</a>
    </nav>
  </body>
</html>
```

- here we have a link to the home page and a link to the about page inside the navigation tag.

```html
<nav>
  <a href="/">Home</a>
  <a href="/about">About</a>
</nav>
```

- here the href contains the url of home and about.

- after creating the function for the layout we can now add it to the app.route decorator.

```python
@app.route('/layout')
def home():
   return render_template('layout.html')
```

- here the layout.html will be rendered to the browser.

- so, after we run the app and got to 'http://127.0.0.1:5000/layout' we will see the navigation bar.

# Template Inheritance

- We made a navbar that has a link to the home page and a link to the about page.
- But its in a different page rendered to the browser.
- So we need to add a template inheritance. SO, that we can render the navbar to all the pages.

-so, to do that, we need to edit the layout page.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>Hello World</h1>
    <nav>
      <a href="/">Home</a>
      <a href="/about">About</a>
    </nav>
    <div>{% block content %} {% endblock %}</div>
  </body>
</html>
```

- nothing fancy here.
- we just added the {% block content %}{% endblock %} tag inside a new <div> after the <nav> tag.

```html
<div>{% block content %} {% endblock %}</div>
```

- now we can render the navbar to all the pages.

- first lets inherit the navbar in the home page.

```html
{% extends 'layout.html' %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
```

- just added the {% extends 'layout.html' %} tag. which will render the navbar from the layout.html file. if we go to the home page we will see the navbar

- But the is problem. lets change <h1> in the body of the home page.

```html
<h1>Home page</h1>
```

- now after restarting the flask app we will not see anything but the navbar.
- that becuase when we inherit the navbar in the home page, we are not inheriting the navbar in the about page, we are actually rendering the home page inside the layout page.

- the {% block content %}{% endblock %} is like a place holder. where the home page will be rendered.

- So, after {%extends 'layout.html'%} we can add the {% block content %}{% endblock %} tag in the home page. And we can also remove some other boilerplate code too.

```html
{% extends 'layout.html' %} {block content %}
<h1>Home page</h1>
{% endblock %}
```

- now we can see home page, and in this process the html code is way cleaner and shorter because the Layout template is inheriting the home page.

- to make the about page inherit the navbar we can follow the same process.

```html
{%extends 'layout.html' %}
{%block content %}
<h1>About page</h1>
{%endblock %}
```
- now if we go to the about page we will see the navbar.

- now if we edit the navbar we will see the changes everywhere.

```html
.....
<h1>LOGO</h1>
.....
```

- i kept everything same but changed the <h1> tag to LOGO.

- Now we can just remove the layout function from the main app file.

```python

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)

```

- And we need to fix a simple issue with the hrefs in layout.html file.

```html
....
<a href="{{ url_for('home') }}">Home</a> <!-- url_for is used to get the url of a page -->
<a href="{{ url_for('about') }}">About</a>
....
```

- we changed the href to url_for('home') and url_for('about') in the layout.html.
- So, that if we ever change the url for home or about we will see the changes everywhere, We dont get error when to use the navbar.

#### now we are ready to go


# Stylling 

- Just use Chatgpt..... ✌😉
- Im not a designer, I just write code. Sooooooo,
- Using the revolutionary design tool Chatgpt i styled the layout template with Tailwind CDN.😎😎


```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <title>Document</title>
  </head>
  <body class="bg-gray-100">
    <div class="container mx-auto p-4">
      <h1 class="text-3xl font-bold mb-4">LOGO</h1>
      <nav class="mb-4">
        <a href="{{ url_for('home') }}" class="mr-4 text-blue-500">Home</a>
        <a href="{{ url_for('about') }}" class="text-blue-500">About</a>
      </nav>
      <div class="bg-white p-4 shadow">
        {% block content %} {% endblock content %}
      </div>
    </div>
  </body>
</html>
```

- for home page.

```html
{% extends 'layout.html' %} 
{% block content %}
<div class="container mx-auto p-4">
  <h1 class="text-3xl font-bold mb-4">Home Page</h1>
  <p class="mb-4">Welcome to the Home page.</p>
  <a href="{{ url_for('about') }}" class="text-blue-500">Learn more about us</a>
</div>
{% endblock content %}

```

- for about page.
```html
{% extends 'layout.html' %} 
{% block content %}
<div class="container mx-auto p-4">
  <h1 class="text-3xl font-bold mb-4">About Page</h1>
  <p class="mb-4">This is the About page content.</p>
  <a href="{{ url_for('home') }}" class="text-blue-500">Back to Home</a>
</div>
{% endblock content %}

```

# Congo!!! U Have  made a Double Page Dynamic Website without any database 😒😒
## Using the Flask Web Framework of python...
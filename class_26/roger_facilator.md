# Class 26 - Introduction to Django

## Review the second Half of class

- Pull up the readme at the root of the class repo.  Quick overview.

## Whiteboard

- Keep it simple with an easy problem domain to get them back in the swing
- split into groups of 4

## Warmup

```python
def reverse(alist):

   #intializing pointers
   left = 0
   right = len(alist)-1

   #condition for termination
   while left < right:

       #swapping
       temp = alist[left]
       alist[left] = alist[right]
       alist[right] = temp

       #updating pointers
       left += 1
       right -= 1

   return alist

print(reverse([1,2,3,4,5, 6]))
```

## Django Talking Points

- **Why**
  - A **LOT** of websites have been built.
  - 1.13 billion
    - Currently, there are around 1.18 billion websites in the World. 18% of these websites are active, 82% are inactive.
  - In the process certain practices have turned out to be more useful than others.
  - The practices that have shown to be consistently good and signifigantly better
  - to enough people take on the label "best practices"
  - The term "best practices" is subjective, sometimes a cause for debate, and often
  - used too usely.
  - But the impulse behind the term is a good thing and can be expressed in
  - other ways...
    - work smart not harder
    - work smarter not harder - this leaves in the idea that you'll still be working hard ;)
    - do more of the good stuff and less of the bad
    - Don't reinvent the wheel
  - MVC Architecture - The MVC (Model-View-Controller) architecture enables easy distinction between different layers of a web app. You can work with the application’s visual presentation and logic independently, and Django will automatically update and sync the changes. MVT or Model-View-Template architecture is another way Django developers like you refer to the Django architecture as it uses templates instead of components.
  - Templates - Django has a powerful templating engine that works on its personal markup language. Templates are HTML code files that are used to display data- be it static or dynamic. Templates contain no application logic, only having information regarding visual content.

  The Django templates are used for generating dynamic HTML web pages.

  - DRY Principle - “Don’t repeat yourself” Python employs philosophy to provide developers with a clean, manageable working environment. Django enforces the DRY principle in everything, creating a single space for storing each distinct object. Django normalizes the values everywhere removing redundancies and allowing the developer to focus on the application logic.

  - Authentication and Security Developers chose Django because it comes with a full-featured, secure user authentication system. It handles user accounts, manages cookies, user groups, and sessions, and keeps track of permissions. This lets you easily build sites that allow users to create accounts and safely sign in and out of the accounts.

  Django has a state-of-the-art security system that helps developers against common security lapses such as SQL injection, cross-site scripting, clickjacking, and cross-site request forgery.

  - DRF - The Django REST framework (DRF) is a component toolkit built on top of the Django framework for creating REST APIs. An API is an interface for interacting with databases. RESTful APIs are conformed to the REST architecture and are used for listing, modifying, creating, and deleting data on web servers using the HTTP protocols.

With DRF, developers have access to web browsable APIs with a huge Django community backing and easy-to-use documentation.

- **What**
  - Sometimes you'll get enough people agreeing on the best ways to combine those practices and a "framework" emerges.
  - One of the most popular, and long lasting, frameworks around is [Django](https://www.djangoproject.com/).
    - Check out the first qoute you see "Django makes it easier to build better Web apps more quickly and with less code."
    - Who usus Django?  Instagram, Spotify, YouTube, The Wa Post, , The Guardian, the NY Post, bitBucket, DropBox, Pinterest, Mozilla, NASA, National Georgaphic, and a big one.  Google Search, Reddit, 
    - Highlight the page title "The Web Framework for Perfectionists with Deadlines"
    - Head down to the **Meet Django** section and tease out the common themes like rapid, fast, clean and pragmatic.
- **How**
  - Django is quite mature and is very clear on what it wants to do.
  - Django is an "opinionated" framework
    - Django makes many of the upfront choices about starting a project
    - Though there is flexibility to make changes as needed
  - The best way to proceed with Lecture is to expand upon the "how" of Django in the [Demo](./DEMO.md)
    - Make sure to frame the steps in a "why/what/how" style.
    - E.g. In the demo when talking about settings
    - Why: Django wants you to get up and running quickly while being flexible if needed
    - What: So Django starts us with a sqlite database by default so we can skip the more complex setup of other *RDBMS*(Relational Database Management System).
    - How: But if you head down to `settings/#DATABASE_SETTINGS` you can switch over to Postgres, etc. when you're ready. (We will see this later this week)

## Django - Typical Steps to Start Django Project

- create project
- define app
  - add app to project
  - add views
  - add urlpatterns
  - add templates
  - add tests

### Create Project

- > mkdir django-things
- > cd django-things
- > vi "python3 -m venv .venv"
- > vs "source ./.venv/bin/activate && python -m pip install -U pip"
- > pip install django
- > django-admin startproject django_things_project .
  - **NOTE:** the dot at end
- > $ tree django-things
  - discuss the files that were generated
  - give a high level account of each file
    - point out which ones that are typically edited and which are left as is
      - manage.py - This script will run administrative tasks
        - asgi.py - A way for clients to slip messages into server protocols. (We won't be altering this file)
        - settings.py - central configuration for django (We do a lot in here)
        - urls.py - Django uses this to match routes to use in your application.
        - wsgi.py - Used for deployment only (non-dev) or when using docker. (We will not be altering this file)
        - db.sqlite3 - Our simple Database

    ```python
    python manage.py runserver
    ```

  - note the unapplied migrations and explain we'll be coming back to that
  - open the browser and navigate to home page
    > Look at this folks.  We have a running server just that quick.
    > point out the 'You are seeing this page because DEBUG=True
    > Show where that it in settings, change it and re-run the server
    - Will have to add allowed hosts of '127.0.0.1' and restart server
    - Put debut back to True
  - discuss development server, it's strengths and limitations and how it is not meant for production
- stop the dev server and address the unapplied migrations warning.
  - Note how the output gives the code to apply the migration. The message even tells you what to do.
- > $ python manage.py migrate
  - discuss what just happened, discuss what a migration is high level and point out we'll be moving into models/persistence in next class
- restart dev server and note that warning is gone

### Create App

- Stop dev server

```python
python manage.py startapp things
```

- > $ tree
  - discuss the files that were generated
  - discuss difference between a *project* and an *app*
  - discuss how a project can (and usually does) contain multiple apps
  - give high level description of each file in things folder
- note that even though the app has been created it has not been integrated into the project as a whole

### Install App

Explain that there's a multi-step process that takes place whenever an App is added.
The key components are **views**, **urls**, **templates**.

We'll cover **tests** a little later.

We'll cover **models**, **migrations** and **admin** in next class.

Edit `settings.py`

```python
'things' # add to INSTALLED_APPS list
```

Optionally mention briefly using `things.apps.ThingsConfig` instead

Edit `things/views.py`

```python
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name='home.html'
```

Discuss the use of TemplateView and how it is not required but is a common best practice.

Note that *home.html* doesn't exist yet, but will soon. You have to start somewhere.

Create App urls

> $ touch things/urls.py

Note that you pretty much always create urls.py for your app and it's a little odd that Django doesn't do that for you.

Edit `things/urls.py`

```python
from django.urls import path

from .views import HomePageView

urlpatterns=[
    path('', HomePageView.as_view(), name='home'),
]
```

- Note that *HomePageView* is the class we just defined in *views.py*
- Note the use use of *as_view()*
- Note the path *name* key word argument
- Note the case of *urlpatterns*

### Add the App urls to the Project urls

- Edit `django_things_project/urls.py`
- Note that the included comments give an example for us

```python
from django.urls import path, include # add include to this statment

path('', include('things.urls')) # add to urlpatterns
```

### Create Templates

```console
> $ mkdir templates
> $ touch templates/base.html
> $ touch templates/home.html
```

- Note that *base.html* isn't required but is a common practice and explain it's benefits
- Edit `base.html`
- Generate an html document using emmet abbreviation ! in VS Code
- Add markup below with the body tag

```html

{% block content %}
<!-- child template content goes here -->
{% endblock content %}

```


**Note** the bracket and percentage sign syntax that is part of [Django template language](https://docs.djangoproject.com/en/4.1/ref/templates/language/)

Edit `home.html`

```html
{% extends 'base.html' %}

{% block content %}
<h1>Home Page</h1>
{% endblock content %}

```

### Add the templates folder

- Note that we need to tell project where to find the templates
- There is a default location for templates but many prefer a templates folder in root of project
  - That is the convention we will be using in class
  - This is example of Django's "opinions" not being perfect fit for our needs.
  - Not a big deal to change when needed.
- Edit `settings.py`
  - Find **TEMPLATES['DIRS']** section
  - Add to list...

```python
BASE_DIR /'templates'
```

### See the page in browser

- Run dev server
  - > $ python manage.py runserver

### Add tests

- Edit `things/tests.py`
- Note that we use `SimpleTestCase` vs. `TestCase`
  - `TestCase` will be used soon once Models are introduced.
- Discuss that Django has own testing framework that is similar to PyTest but more Django focused.
- Create and run tests one at a time.

```python
from django.test import SimpleTestCase
from django.urls import reverse

class ThingsTests(SimpleTestCase):
    def test_home_page_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_templete(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')
```

- stop server
- > $ python manage.py test

### Using context in template

The `Django template language` gives access context data by using `variables` and `tags`.

#### Variables

Variables look like this: `{{ variable }}`.

When the template engine encounters a variable, it evaluates that variable and replaces it with the result.

#### Tags

Tags look like this: `{\% tag \%}`.

Tags are more complex than variables: Some create text in the output, some control flow by performing loops or logic, and some load external information into the template to be used by later variables.

Some tags require beginning and ending tags (i.e. `{\% tag \%} ... tag contents ... {\% endtag \%}`).

```django
{\% for thing in things \%}
  <h2>Name: {{ thing.name }}</h2>
  <p>Description: {{ thing.description }}
{\% endfor \%}
```

Run the dev server. If you're seeing names and descriptions then that's good enough for now.

### Add another page

> touch templates/about.html

```html

{% extends 'base.html' %}

{% block content %}
<h1>About Page</h1>
{% endblock content%}

```

- Add a nav
- Edit *base.html*
- Note the url django template keyword
- Note the use of 'home' and 'about' and what they must match

```html
<nav>
    <a href="{% url 'home' %}">Home</a>
    |
    <a href="{% url 'about' %}">About</a>
</nav>
{% block content %}
<!-- child template content goes here -->
{% endblock content %}
```

**Note** the use of `url` for the `href`

- Edit *things/urls.py*
  - import AboutView
  - add `path('about', AboutView.as_view(), name='about'),`
- Edit *things/views.py* to add...

```python
class AboutView(TemplateView):
    template_name = 'about.html'
```

- Note that we do not need to update project urls because it's already wired up with the app
- Note that we added templates, views and urls in different order this time - and that's fine.
- Re/Start the server and navigate between the pages

## Add new tests

- Edit *things/tests.py* and add ...

```python
def test_about_page_status_code(self):
    url = reverse('about')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

def test_about_page_templete(self):
    url = reverse('about')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'about.html')
    self.assertTemplateUsed(response, 'base.html')
```

- > python manage.py test
- DONE!

## Wrapping Up

You've now got a working Django site! But it doesn't have much style. For that we need CSS. So let's head over to the [next demo](./DEMO-TAILWIND.md)



# Django with TailWind + Flowbite

## TailwindCSS

[TailwindCSS](https://tailwindcss.com/){:target="_blank"} is a `utility-first` css framework that represents a fresh (and sometimes controversial) take on styling web sites. Lots of developers find this approach faster and more maintainable than previous approaches. We're all going to try this tool out today.

## Flowbite

[Flowbite](https://flowbite.com/){:target="_blank"} is a very handy tool that builds on top of TailwindCSS and gives access to an excellent set of components. It also includes tools for integrating with popular frameworks, including Django of course!

## Setting up Flowbite with Django

In order to integrate Flowbite with Django it takes a few steps.

**NOTE:** These getting started steps were based on the excellent [Tailwind CSS Django - Flowbite](https://flowbite.com/docs/getting-started/django/){:target="_blank"}, just with some tweaks to work better for our labs. Thanks Flowbite!

### Django Compressor

Install `django-compressor` by running the following command in your terminal:
> `pip install django-compressor`

Add compressor to the installed apps inside the settings.py file:

```python
# config/settings.py

INSTALLED_APPS = [
    ...
    'compressor',
    ...
]
```

1. Configure the compressor inside the settings.py file:

```python
COMPRESS_ROOT = BASE_DIR / 'static'

COMPRESS_ENABLED = True

STATICFILES_FINDERS = ('compressor.finders.CompressorFinder',)
```

1. Create two new folders and an input.css file inside the static/src/ folder:

```text
static
└── src
    └── input.css
```

## Edit base.html

Edit `base.html` file inside the templates/ directory:

```html
<!-- templates/base.html -->

{% load compress %}
{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django + Tailwind CSS + Flowbite</title>

    {% compress css %}
    <link rel="stylesheet" href="{% static 'src/output.css' %}">
    {% endcompress %}

</head>

<body class="bg-green-50">
    <div class="container mx-auto mt-4">
        {% block content %}
        {% endblock content %}
    </div>
</body>

</html>
```

### Edit home.html

Edit the homepage markup:

```html
<!-- templates/index.html -->

{% extends "base.html" %}

{% block content %}
  <h1 class="text-3xl text-green-800">Django + Tailwind CSS + Flowbite</h1>
{% endblock content %}
```

### Install Tailwind CSS

Run the following command the install Tailwind CSS as a dev dependency using NPM:
> `npm install -D tailwindcss`
Using the Tailwind CLI create a new tailwind.config.js file:
> `npx tailwindcss init`

Configure the template paths using the content value inside the Tailwind configuration file:

```javascript
module.exports = {
  content: [
      './templates/**/*.html'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Import the Tailwind CSS directives inside the input.css file:

```css
/* static/src/input.css */

@tailwind base;
@tailwind components;
@tailwind utilities;
```

Run the following command to watch for changes and compile the Tailwind CSS code:
> `npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch`

**NOTE: This could take a min or 2 to finish.** 

Open `localhost:3000` in your browser and you’ll see working HTML with Tailwind CSS code.

### Install Flowbite

Now that you have configured both Django and Tailwind CSS you can also set up Flowbite to get access to the whole collection of interactive components like navbars, modals, dropdowns, buttons, and more to make development even faster.

About Flowbite #

Flowbite is an open source library of interactive components built on top of Tailwind CSS and it can be installed using NPM and required as a plugin inside Tailwind CSS.

Install Flowbite as a dependency using NPM:
> `npm install flowbite`

Require Flowbite as a plugin inside the tailwind.config.js file:

```javascript
module.exports = {

    plugins: [
        require('flowbite/plugin')
    ]

}
```

Include Flowbite inside the content value of the tailwind.config.js file:

```javascript
module.exports = {
  content: [
      './templates/**/*.html',
      './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Include Flowbite’s JavaScript file inside the base.html file just before the end of the <body> tag using CDN or by including it directly from the node_modules/ folder:

```javascript
<script src="https://cdnjs.cloudflare.com/ajax/libs/flowbite/1.6.2/flowbite.min.js"></script>
```

Now that you have everything configured you can check out the components from Flowbite such as navbars, modals, buttons, datepickers, and more.

## Flowbite components

In this section I’ll show you how you can search for and use the interactive components from Flowbite.

Let’s start by adding a Navbar component inside the base.html file:

```html
<!-- templates/base.html -->

{% load compress %}
{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django + Tailwind CSS + Flowbite</title>

    {% compress css %}
    <link rel="stylesheet" href="{\% static 'src/output.css' \%}">
    {% endcompress %}

</head>

<body class="bg-green-50">

    <!-- Add this -->
    <nav class="bg-green-50 border-gray-200 px-2 sm:px-4 py-2.5 rounded dark:bg-gray-800">
        <div class="container flex flex-wrap items-center justify-between mx-auto">
          <a href="{{ .Site.Params.homepage }}/" class="flex items-center">
              <img src="/docs/images/logo.svg" class="h-6 mr-3 sm:h-9" alt="Flowbite Logo" />
              <span class="self-center text-xl font-semibold whitespace-nowrap dark:text-white">Flowbite Django</span>
          </a>
          <button data-collapse-toggle="mobile-menu" type="button" class="inline-flex items-center p-2 ml-3 text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600" aria-controls="mobile-menu" aria-expanded="false">
            <span class="sr-only">Open main menu</span>
            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd"></path></svg>
            <svg class="hidden w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
          </button>
          <div class="hidden w-full md:block md:w-auto" id="mobile-menu">
            <ul class="flex flex-col mt-4 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium">
              <li>
                <a href="#" class="block py-2 pl-3 pr-4 text-white bg-green-700 rounded md:bg-transparent md:text-green-700 md:p-0 dark:text-white" aria-current="page">Home</a>
              </li>
              <li>
                <a href="#" class="block py-2 pl-3 pr-4 text-gray-700 border-b border-gray-100 hover:bg-gray-50 md:hover:bg-transparent md:border-0 md:hover:text-green-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">About</a>
              </li>
              <li>
                <a href="#" class="block py-2 pl-3 pr-4 text-gray-700 border-b border-gray-100 hover:bg-gray-50 md:hover:bg-transparent md:border-0 md:hover:text-green-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">Services</a>
              </li>
              <li>
                <a href="#" class="block py-2 pl-3 pr-4 text-gray-700 border-b border-gray-100 hover:bg-gray-50 md:hover:bg-transparent md:border-0 md:hover:text-green-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">Pricing</a>
              </li>
              <li>
                <a href="#" class="block py-2 pl-3 pr-4 text-gray-700 hover:bg-gray-50 md:hover:bg-transparent md:border-0 md:hover:text-green-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent">Contact</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    <!-- End of new HTML -->

    <div class="container mx-auto mt-4">
        {% block content %}
        {% endblock content %}
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/flowbite/1.6.2/flowbite.min.js"></script>
</body>

</html>
```

This way you already have a functional and responsive navigation bar added to all pages.

Let’s take a look how can added more content directly to the view templates, not just the base template.

Check out one of the Card components from Flowbite and add it to the index.html file:

```django
<!-- templates/index.html -->

{\% extends "base.html" \%}

{\% block content \%}

<h1 class="mb-6 text-3xl text-green-800">Django + Tailwind CSS + Flowbite</h1>
<div class="max-w-sm bg-white border border-gray-200 rounded-lg shadow-md dark:bg-gray-800 dark:border-gray-700">
    <a href="#">
        <img class="rounded-t-lg" src="/docs/images/blog/image-1.jpg" alt="" />
    </a>
    <div class="p-5">
        <a href="#">
            <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Noteworthy technology
                acquisitions 2021</h5>
        </a>
        <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">Here are the biggest enterprise technology
            acquisitions of 2021 so far, in reverse chronological order.</p>
        <a href="#"
            class="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-green-700 rounded-lg hover:bg-green-800 focus:ring-4 focus:outline-none focus:ring-green-300 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800">
            Read more
            <svg class="w-4 h-4 ml-2 -mr-1" fill="currentColor" viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd"
                    d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                    clip-rule="evenodd"></path>
            </svg>
        </a>
    </div>
</div>

{\% endblock content \%}
```

## Improving Home Page

Grab the [Flowbite Card with Image](https://flowbite.com/docs/components/card/#card-with-image) and use it to render out a `card` for each `thing` in data. This will require adjustments from the Flowbite's sample code. See `home.html` in demo for final version.

## Improving About Page

Follow the same process for About page using [Flowbite User profile card](https://flowbite.com/docs/components/card/#user-profile-card). This will require adjustments from the Flowbite's sample code. See `about.html` in demo for final version.

## Wrapping Up

At this point you can use any of the components to build user interfaces easier and faster together with Django, Tailwind CSS and Flowbite.

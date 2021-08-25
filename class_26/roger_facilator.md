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
  - There are 1,197,982,359 websites in the World as of January 2021.
  - In the process certain practices have turned out to be more useful than others.
  - The practices that have shown to be consistently good and signifigantly better
  - to enough people take on the label "best practices"
  - The term "best practices" is subjective, sometimes a cause for debate, and often
  - used too usely.
  - But the impulse behind the term is a good thing and can be expressed in \
  - other ways...
    - work smart not harder
    - work smarter not harder - this leaves in the idea that you'll still be 
    - working hard ;)
    - do more of the good stuff and less of the bad
    - Don't reinvent the wheel

- **What**
  - Sometimes you'll get enough people agreeing on the best ways to combine those practices and a "framework" emerges.
  - One of the most popular, and long lasting, frameworks around is [Django](https://www.djangoproject.com/).
    - Check out the first qoute you see "Django makes it easier to build better Web apps more quickly and with less code."
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

- > $ mkdir django-things
- > $ cd django-things
    > We are not going to run poetry new because that is going to give us more than we want
    > We are going to rely on django giving us the things that we need.
- > $ poetry init -n
- > $ poetry add django
- > $ poetry shell
- > $ django-admin startproject django_things_project .
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
{% raw  %}
<nav>
    <a href="{% url 'home' %}">Home</a>
    |
    <a href="{% url 'about' %}">About</a>
</nav>
{% block content %}
<!-- child template content goes here -->
{% endblock content %}
{% endraw  %}
```

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

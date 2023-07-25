# Review any pain points in Django so far

## Warm up for today

> Given a linked list of students, get a "roll call" of students from last to first.

```text
Input: { Ashley } => { Mario } -> { Zelda } -> None
Result:
Print out -
  Zelda
  Mario
  Ashley
```

- Print each students name starting at end (aka tail) of list.

## Todays Jokes

- What do you call security guards working outside Samsung shops? Guardians of the Galaxy.
- Why can't you give Elsa a balloon? Because she will Let it go.

## Add movies to Django Movies

- The Start

  - Start today's demo from scratch adjusting the pace as needed and eliciting questions along the way.
  - Before starting prep/review ask students for particular pain points and keep them in mind during build out.
  - > mkdir starwars-movie-rater
  - > cd starwars-movie-rater
  - > python3 -m venv .venv
  - > pip install django
  - > source ./.venv/bin/activate
  - > django-admin startproject movie_rater_project .
  - > SAY: From Experience I know I need to run my migrations and add my app
  - > QUESTION: What is the command to migrate?
  - > python manage.py migrate
  - > python manage.py startapp movies
  - Edit `movie_rater_project/settings.py`
  - add `movies` to `INSTALLED_APPS` list

## Models

- **Why**
  - Python tends to express in terms of Objects
  - Databases are oriented around Tables/Rows/Columns and communicate via SQL
  - This dissonance can make it more difficult to reason about the problem domain
- **What**
  - Object Relational Mappers or mapping ( ORM ) bridges that gap by allowing developers to *mostly* think about Objects while the mappers handles interaction with the database.
  - You worked with Mongo in 301.  Post Gres is a little different. You will see thing in SQL look like this:

```sql
SELECT * FROM users WHERE school = "CodeFellows';
```

> Object-relational-mapping is the idea of being able to write queries like the one above, using our preferred programming language.  Long story short, we are trying to interact with our database using python instead of SQL.

- **How**
  - Django's ORM is called a Model
  - A model can be corresponds to a Database Table but is authored as a Python class
  - The model's attributes are comparable to the columns in a table
  - The values of those attributes are like the DB table rows

### Creating a Model

- Edit `movies/models.py` and add...

```python
from django.contrib.auth import get_user_model

class Movie(models.Model):
    name = models.CharField(max_length=256)
    rating = models.IntegerField(default=0)
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
```

- > NOTE: The cascade will delete ay object that was created by a deleted user.

- python manage.py makemigrations movies
- python manage.py migrate
- Go ahead and run the server really quick and go to the admin page
- python manage.py createsuperuser
- python manage.py runserver
- log in to admin
  - show how awesome but that it's missing Movies
- update *admin.py* to register Movies model

#### Edit the Admin

- Edit `movies/admin.py` and add...

```python
from .models import Movie

admin.site.register(Movie)
```

- REFRESH WEB SITE
- Now see the movie.
- Create a Movie
  - Notice the less than ideal display of *Movie object(1)*
- Update **Movie model** with `__str__` method that returns self.name

```python
    def __str__(self):
        return f'{self.name} reviewed by {self.reviewer} with a score of {self.rating}'
```

### Inspecting the Database

- [DB Browser for SQLite](https://sqlitebrowser.org/)
- open `db.sqlite3` with DB Browser
- briefly touch on all the other tables created by Django
- Under Tables select `moviews_movie`
  - review the schema
- Select Browse Data tab
  - choose `moview_movie` from drop down
  - look at the movie

### View + Model

- **Why**
  - While it's nice to see our `movies` in admin panel, that's not meant for end users
  - We need for those models to be viewable (and eventually editable) by end user
- **What**
  - It is possible create custom views that interact with models
  - But often times model data is displayed in common ways
- **How**
  - Django provides `generic` class based views that make interacting with surprisingly little code

- Update views.py for a MovieListView

```python
from django.views.generic import ListView
from .models import Movie

class MovieListView(ListView):
    template_name = "movie_list.html"
    model = Movie
```

### Add URLS

- update project urls.py
- create/update movies/urls.py for new view

```python
from django.urls import path

from .views import MovieListView

urlpatterns = [
    path('', movieListView.as_view(), name="movie_list"),
]
```

- update project urls.py

```python
from django.urls import path, include
urlpatters = [
    path('', include('movies.urls')),
]
```

- Customize template directory location
  - `'DIRS': [ BASE_DIR / 'templates' ],` in settings `TEMPLATE` section
  - Explain briefly that this is a very common step, but not the default
- Create `templates/base.html` with common html and content block
- In vs-code can use keyword html:5

- create a base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>THings</title>
</head>
<body>
    {% block content %}
    {% endblock content %}
</body>
</html>
```

- Create `templates/movie_list.html with:

```html
{% extends 'base.html' %}

{% block content %}
  {% for movie in object_list %}
  <p>{{ movie.name }}</p>
  {% endfor %}
{% endblock content %}
```

- You may be asking yourself.  How does django know waht onject_list is referring to. This is because of the object_list.  This is part of the generic import in the models.  You can also set this manually.

In views.py

```python
class MovieListView(ListView):
    template_name = 'movie_list.html'
    model = Movie
    context_object_name = 'sw_movies' # <-- Add this
```

Then in the movie_list.html

```django
{% extends 'base.html' %}

{% block content %}
    {% for movie in sw_movies %} # <--Change object_list to this (or whatever you set in views)
        <h2>{{ movie.name }} </h2>
    {% endfor %}
{% endblock content %}
```

## DetailView

- Update views.py to add a Detail View
  - Before import DetailView talk about how intuitive these names are.
  - Even better, see if students can guess what the base class name might be

```python
class MovieDetailView(DetailView):
    template_name = "movie_detail.html"
    model = Movie
```

- Update urls.py

```html
from django.urls import path

from .views import movieListView, MovieDetailView

urlpatterns = [
    path('', MovieListView.as_view(), name="movie_list"),
    path('<int:pk>/', MovieDetailView.as_view(), name="movie_detail"),
]
# The int is specifying that it will get an integer back in the form of a primary key. You use this when your view is guranteed to revieve an int.
```

- Add templates/movie_detail.html

```html
{% extends 'base.html' %}

{% block content %}
  <section>
    <h2>{{ movie.name }}</h2>
    <p>Rating: {{ movie.rating }}</p>
    <p>Reviewer: {{ movie.reviewer }}</p>
  </section>
{% endblock content %}
```

- Update templates/movie_list.html

```html
{% extends 'base.html' %}

{% block content %}
  {% for movie in object_list %}
  <h2><a href="{% url 'movie_detail' movie.pk %}">{{ movie.name }}</a></h2>
  {% endfor %}
{% endblock content %}
```

- The way this works is by looking up the URL definition as specified in the movies.urls module. You can see exactly where the URL name of ‘detail’ is defined below:

```python
from django.urls import path

from .views import MovieListView, MovieDetailView

# the 'name' value as called by the {% url %} template tag

urlpatterns = [
    path('', MovieListView.as_view(), name="movie_list"),
    path('<int:pk>/', MovieDetailView.as_view(), name="movie_detail"),
]
```

- Now test out the links in the page and point out the movies/1 in the address bar.

### Testing

```python
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from movies.models import Movie

# Create your tests here.

class MoviesTests(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass")
        self.movie = Movie.objects.create(
            name = 'Empire', rating = 10, reviewer = self.user)
    
    def test_string_representation(self):
        self.assertEqual(str(self.movie), 'Empire')

    def test_movie_name(self):
        self.assertEqual(f'{self.movie.name}', 'Empire')
    
    
    def test_list_page_status_code(self):
        url = reverse("movie_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("movie_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "movie_list.html")
        self.assertTemplateUsed(response, "base.html")
```

run python manage.py test

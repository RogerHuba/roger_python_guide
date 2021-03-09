# Add movies to Django Movies

- The Start

  - Start today's demo from scratch adjusting the pace as needed and eliciting questions along the way.
  - Before starting prep/review ask students for particular pain points and keep them in mind during build out.
  - > mkdir starwars-movie-rater
  - > cd movie-rater
  - > poetry init -n
  - > poetry add django
  - > poetry shell
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
  - You worked with PostgresQL in 301.  You probably remember statments like:

```sql
SELECT * FROM users WHERE school = "CodeFellows';
```

> Object-relational-mapping is the idea of being able to write queries like the one above, using
> our preferred programming language.
>
> Long story short, we are trying to interact with our database using python instead of SQL.

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

- python manage.py makemigrations movies
- python manage.py migrate
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
- Update Movie model with \__str__ method that returns self.name

```python
    def __str__(self):
        return self.name
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
from django.urls import include
urlpatters = [
    path('', include('movies.urls')),
]
```

- Customize template directory location
  - `'DIRS': [ BASE_DIR / 'templates' ],` in settings `TEMPLATE` section
  - Explain briefly that this is a very common step, but not the default
- Create `templates/base.html` with common html and content block
- In vs-code can use keyword html:5

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
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

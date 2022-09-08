# Django CRUD (C)reate (R)ead (U)pdate (D)elete

## House Keeping

- [Make sure you sign up for a library](https://docs.google.com/spreadsheets/d/1nPXDMI5IOAyr0fsJveRDY2iUeNDqaYbEn97zcEqSN90/edit#gid=18456559)

## Warmup

- Scrabble Pieces

## The Django Way and Doc's

> Today is a heavy build out Day.  We are going to Jump right in. Today we are going to talk about CRUD.
> QUESTION: `What does crud stand for?`
> ANSWER: `Create Read Update Delete`
> In our last lab, we added some persistance to our app, but we only implemented that through the admin console in Django.  We want to provide end users the ability to do this as well.  We are going to code this out from scratch There are a few things I will copy/paste to save time, others I'll code out.

## Alias

Show the alias that have been setup for venv.

## Create the File Structure and Environment

```bash
mkdir movies
cd movies
vi
pip install django
vs
django-admin startproject movies_project .
python manage.py runserver
  - Notice the migration warnings
ctrl-c 
```

## Add the Application

> Let's create an application really quick
> If anyone asks about django-admin startapp xxx
> Manage.py is automatically created in each Django project. It does the same
> thing as django-admin but also sets the DJANGO_SETTINGS_MODULE environment
> variable so that it points to your project’s settings.py file.

```python
python manage.py startapp movies
```

> add the 'movies' app into project settings.py
> alternatively add the right way
> 'movies.apps.MoviesConfig'
> You can see the movies.apps path in the movies->apps.py

## Run your Migrate Command

> Point out that there is no db.sqlite3 file and no migration file before this
> This is Django's builtin models.

```python
python manage.py migrate
python manage.py createsuperuser
```

> point out the db file and migration directory.

## Set Environment Variables

```python
poetry add django-environ
touch .env
# Create in the main root but ultmately will need to go into the project root
```

> In settings.py

```python
import environ

env = environ.Env(
    # We are doing a default setting here because even if something happens to the .env, 
    # we set this to false to make sure Django dosn't start pusging out to much information 
    # on the error pages (you know, the good stuff we have been using to debug out 
    # pages until revently)
    DEBUG=(bool, False)
)

# read .env file
environ.Env.read_env()

SECRET_KEY = env.str('SECRET_KEY')
DEBUG = env.bool('DEBUG')
ALLOWED_HOSTS = tuple(env.list('ALLOWED_HOSTS'))
```

> In .env (Note the location of this is not what is expected. Inside project folder)

```env
SECRET_KEY=xxxx
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Create Model

- Open model.py in application

```python
from django.db import models
from django.contrib.auth import get_user_model

class Movie(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(default='')
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
      return self.name
```

## Register in Admin

- Open admin.py in application
  
```python
from .models import Movie

# Register your models here.
admin.site.register(Movie)
```

- Run makemigrations

```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

> Point out the unapplied migration that is showing up.  Resembles
> What we had after creating the project.

```python
python manage.py migrate
```

> Our warning is now gone and we can move on.
> Now I am going to add a templates folder and add some files we will use

## Templates

```bash
mkdir templates
touch templates/base.html
touch templates/movie-create.html
touch templates/movie-delete.html
touch templates/movie-detail.html
touch templates/movie-list.html
touch templates/movie-update.html
```

> Let's also talk a little about adding some css.
> This will go in the base.html

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <link rel="stylesheet" href="{% static 'base.css' %}">
    <title>Movies</title>
</head>
<body>
    <header>
      <h1>Full Stack Movies</h1>
    </header>
    {% block content %}
    <p>Looks like somebody forgot to define this block in child template</p>
    {% endblock content %}
    <footer></footer>
</body>
</html>
```

> QUESTION: Does anyone know what CDN stand for?
> ANSWER: Content Delivery Network
> Media rich companies use them all the time: Netflix, ESPN etc.
> Lag matters, Disney does not just have a server in LA to service China. Can mention load servers and content that does not change Django refers to this as static
> In order to handle this, you need to add {% load static %} to the top of the base.html
> You will also need to create a folder called static
> Then add your style.css file there
> While I am running in development mode, I will use my static folder. In my case right here I am using bootstrap so I could get away with not loading static.
> I have my base template set up, lets get the other files to extend the base.

```html
{% extends 'base.html' %}

{% block content %}
<h1> Coming Soon</h1>
{% endblock content %}
```

> We have some templates. We can't reach them yet!
> We added our model earlier, we need to add some paths and views.

## Views

```python
from django.views.generic import ListView, DetailView
```

> Question: In a perfect world if we needed to add in a view to create, what would we use?
> ANSWER: CreateView
> How about for update something? How about Delete?

```python
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class MovieListView(ListView):
    pass

class MovieDetailView(DetailView):
    pass

class MovieCreateView(CreateView):
    pass

class MovieUpdateView(UpdateView):
    pass

class MovieDeleteView(DeleteView):
    pass
```

> QUESTION: Does anyone remember what we needed for a ListView?

```python
from .models import Movie

class MovieListView(ListView):
    template_name = 'movie-list.html'
    model = Movie
```

> It will be similar for the rest (For now / maybe).

```python
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Movie

class MovieListView(ListView):
    template_name = 'movie-list.html'
    model = Movie

class MovieDetailView(DetailView):
    template_name = 'movie-detail.html'
    model = Movie

class MovieCreateView(CreateView):
    template_name = 'movie-create.html'
    model = Movie

class MovieUpdateView(UpdateView):
    template_name = 'movie-update.html'
    model = Movie

class MovieDeleteView(DeleteView):
    template_name = 'movie-delete.html'
    model = Movie
```

> Will this work? We won't know until we get everything else wired up
> We have model, templates, views, only one thing left, what is that?

## URLS

> URLS...
> Project URL

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
]
```

> App URLS

```bash
touch movies/urls.py
```

```python
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import MovieDetailView, MovieListView, MovieCreateView, MovieUpdateView, MovieDeleteView

urlpatterns = [ 
    path('', MovieListView.as_view(), name='list_view'),
    path('<int:pk>', MovieDetailView.as_view(), name='detail_view'),
    path('', CreateView.as_view(), name='create_view'),
    path('', UpdateView.as_view(), name='update_view'),
    path('', DeleteView.as_view(), name='delete_view'),
]
```

## Other Updates

> Are there anythings we may have missed to this point?
> I can think of one for sure. TEMPLATES

```python
'DIRS': [BASE_DIR / 'templates'],
```

> Point out that STATIC_URL is set by default to be at /static
> Time to run server if not already running
> We get a 404 with a Page not found.  Ideas on the issue?
> Look at our url patterns.  We are looking for /movies
> We have a page up and running now. Lets get some Movies up.
> We can start with updating our template

## Movie List

```python
{% extends 'base.html' %}

{% block content %}

<ul>
  {% for movie in object_list %}
        <li>
            <a href="{% url 'movie_detail' movie.pk %}">{{ movie.name }}</a>
        </li>
  {% endfor %}
</ul>

{% endblock content %}
```

> We need to add in our movie_detail view in the app urls.py

```python
from .views import MovieListView, MovieDetailView

path('<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
```

> Should be able to see movie and click on Full Stack
> Lets work on our create next in our urls

## Create

```python
from .views import MovieListView, MovieDetailView, MovieCreateView

path('new/', MovieCreateView.as_view(), name='movie_create'),
```

> runserver and go to the /new route
> We get this without the fields, we something about forms here as well.
> After a bit of digging in the docs you would find out
> This is something else we are getting for free here. In order to do
> we need to add in some fields to our views.

```python
class MovieCreateView(CreateView):
    template_name = 'movie-create.html'
    model = Movie
    fields = ['name', 'description', 'owner']
```

> It does give us some stuff for free but there are some small
> things we do need to handle here. Lets go over to our movie-create.html

```html
{% extends 'base.html' %}

{% block content %}

<h1>Create Movie</h1>

<form action="" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit" value="SAVE">
</form>

{% endblock content %}
```

> Yea, we had to make a form here but this is not overkill for us. Lets see if this works and we will come back from there. Is it lovely, maybe not but you get it at a low cost. Lets dig into a couple lines of that code.
> 2 Things that matter here.
> `ALWAYS add {% csrf_token %}`
>Cross Site Request Forgery protection
The CSRF middleware and template tag provides easy-to-use protection against Cross Site Request Forgeries. This type of attack occurs when a malicious website contains a link, a form button or some JavaScript that is intended to perform some action on your website, using the credentials of a logged-in user who visits the malicious site in their browser. A related type of attack, ‘login CSRF’, where an attacking site tricks a user’s browser into logging into a site with someone else’s credentials, is also covered.

The first defense against CSRF attacks is to ensure that GET requests are side effect free. Requests via ‘unsafe’ methods, such as POST, PUT, and DELETE, can then be protected by following the steps below in a smililar

> Stands for `cross site request forgery`. There are major security flaw in web applications, and you don't want yours to be one of them. This one line gets rid of a lot of bad actors / hackers. This is more than locking the doors to your vehicle, it is the equivalent of low jack. Little cost for a lot of help. 
> The official: 
> The other thing that is happening is the form is rendering out each field represented in the fields list as a paragraph Show that we can take one of the fields away. Lets move on to the last ones, update and delete.
> The other item here is `form.as_p`. This renders the form in a p tag. There are some other methods avaliable such as form.as_table and form.as_ul

## Update

```html
{% extends 'base.html' %}

{% block content %}

<h1>Update Movie</h1>

<form action="" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit" value="SAVE">
</form>

{% endblock content %}
```

> Now we need to update

```python
path('<int:pk>/edit', MovieUpdateView.as_view(), name='movie_update'),
```

> Go to the route movies/1/edit
> Should get a prohibited error
> Need to add fields to update

```python
fields = ['name', 'description', 'owner']
```

## Delete

> Now just need to do the delete
> We can do the url

```python
    path('<int:pk>/delete', MovieDeleteView.as_view(), name='movie_delete'),
```

> update the delete html template

```html
{% extends 'base.html' %}

{% block content %}

<h1>Delete Movie</h1>

<form action="" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <p>Do you really want to delete "{{ movie.name }}"?</p>
  <input type="submit" value="OK">
</form>

{% endblock content %}
```

> When we click on ok, we get another error. We need to prove a success URL

```python
from django.urls import reverse_lazy

class MovieDeleteView(DeleteView):
    template_name = 'movie-delete.html'
    model = Movie
    success_url = reverse_lazy('movie_list')
```

> This reverse_lazy is needed because this success could see urls that might not be known yet at the point this class is instanciated. This is a safe way for it to only do so when ready. Show that we can in fact delete the movies. The only thing that is left is to tie all of this together so we don't have to manually enter the routes in the browser bar.

## Final Update to Movie List

```html
{% extends 'base.html' %}

{% block content %}

<h1>Movies</h1>
<a href="{% url 'movie_create' %}">+ New Movie</a>
<ul>
    {% for movie in object_list %}
      <li>
          <a href="{% url 'movie_detail' movie.pk %}">{{ movie.name }}</a>
      </li>
  {% endfor %}
</ul>

{% endblock content %}
```

> Reload the page and add a new movie. Should get improperly configured exception
> No URL to re-direct to.
> That makes sense
> We do have options, an absolute on the model or a url
> Lets do the absolute in the models.

```python
from django.urls import reverse

    def get_absolute_url(self):
        return reverse('movie_detail', args=[str(self.id)])
```

> Looks good. Now details is not doing much because we havn't told it to yet.

```html
{% extends 'base.html' %}

{% block content %}

<h2>Details about {{ movie.name }}</h2>
<h2>Owner: {{ movie.owner }}</h2>
<p>{{ movie.rating }}</p>
<a href="{% url 'movie_update' movie.pk %}">+ Update Movie</a>
<a href="{% url 'movie_delete' movie.pk %}">+ Delete Movie</a>

{% endblock content %}
```

## Testing

- python manage.py test

```python
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Movie


class MovieTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester', email='tester@email.com', password='pass'
        )

        self.movie = Movie.objects.create(
            name='The Blob', description='Movie about the Blob', owner=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.movie), 'The Blob')

    def test_movie_content(self):
        self.assertEqual(f'{self.movie.name}', 'The Blob')
        self.assertEqual(f'{self.movie.owner}', 'tester')
        self.assertEqual(f'{self.movie.description}', 'Movie about the Blob')

    def test_movie_list_view(self):
        response = self.client.get(reverse('movie_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The Blob')
        self.assertTemplateUsed(response, 'movie-list.html')

    def test_movie_detail_view(self):
        response = self.client.get(reverse('movie_detail', args='1'))
        no_response = self.client.get('/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Owner: tester')
        self.assertTemplateUsed(response, 'movie-detail.html')

    def test_movie_create_view(self):
        response = self.client.post(
            reverse('movie_create'),
            {
                'name': 'Raker',
                'description': 'test',
                'owner': self.user.id,
            }, follow=True
        )

        self.assertRedirects(response, reverse('movie_detail', args='2'))
        self.assertContains(response, 'Details about Raker')



    def test_movie_update_view_redirect(self):
        response = self.client.post(
            reverse('movie_update', args='1'),
            {'name': 'Updated name','description':'new description','reviewer':self.user.id}
        )

        self.assertRedirects(response, reverse('movie_detail', args='1'))

    def test_movie_delete_view(self):
        response = self.client.get(reverse('movie_delete', args='1'))
        self.assertEqual(response.status_code, 200)
```

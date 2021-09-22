# Demos: Django REST Framework & Docker

Use this document to describe the demo(s). Generally, this is going to take the format of either how to build the demo step by step, or less specifically, talking points surrounding the outcomes of the demo segment and code snippets to highlight.

## Blog Post API Demo

### Set up Django Project

- > mkdir blog
- > cd blog
- > poetry init -n
- > poetry add django
- > poetry shell
- > django-admin startproject blog_api_project .
  - remind students to remember dot at the end

For this demo we will not be doing a custom user so we can run our migration

- > python manage.py migrate

Now lets make sure the server starts up

- > python manage.py runserver
- shut down server

Lets go ahead and add an app called 'posts'

- > python manage.py startapp posts

I know I am going to need my admin console so I am going to create my superuser now

- > python manage.py createsuperuser
  - Use `admin` for name and password, `admin@admin.com` for email

---

Let's open up code editor and make our overall project aware of our app.

Where do we do this?

- Go to `settings.py`
- Add `posts` to bottom of `INSTALLED_APPS` list

Lets move on to our model

Open `posts/models.py`

```python
from django.contrib.auth import get_user_model
from django.db import models

class Posts(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

This looks good for our models.  We have made some changes to our models.  What is our next step?

- > python manage.py makemigrations posts
- > python manage.py migrate

If we want our model to be accessible from the Django Admin panel

Lets open `posts/admin.py`

```python
from django.contrib import admin
from .models import Posts

admin.site.register(Posts)
```

### Tests

From here you could to run the server, check that you can access the admin site, login with the superuser and see posts.

Another way we can test is by running some tests

Open up posts/tests.py

```python
from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Posts

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_post = Posts.objects.create(
            author = testuser1,
            title = 'Green Eggs and Ham',
            body = 'I do not like green eggs and ham, Sam I  am.'
        )
        test_post.save()

    def test_blog_content(self):
        post = Posts.objects.get(id=1)
        actual_author = str(post.author)
        actual_title = str(post.title)
        actual_body = str(post.body)
        self.assertEqual(actual_author, 'testuser1')
        self.assertEqual(actual_title, 'Green Eggs and Ham')
        self.assertEqual(actual_body, 'I do not like green eggs and ham, Sam I  am.')
```

We can now run

- > python manage.py test

We are almost done with the regular Django things.  Only thing left us urls and views.  These things will still matter.  We are not going to be using templates.  Instead we will be using something that will mkae our date into JSON?  From our readings does anyone remember what this will use? **Serializer**

### Adding Django Rest Framework

Let's add our `djangorestframework` to our installed apps

-> poetry add djangorestframework

- open `settings.py`
- add `rest_framework` to `INSTALLED_APPS` list
  - notice that app name differs from package name
  - add just above `posts`
- Often times devs follow a convention of seperating out `INSTALLED_APPS` sections with whitepace and comments
  - `standard library`,`third party` and `local` are common sections

We also need to add to add some REST_FRAMEWORK specific configuration in `settings.py`

I usually add at the bottom of file.

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES' : [
        'rest_framework.permissions.AllowAny',
    ]
}
```

This is already the default in django, but it will not always be the default so lets add it in now.  You do not need to memorize this but it is something to add to your check list.

Now let's add in our project level URLS so we can close the door on the project level stuff.

Note that we must import `include` from `django.urls`

```python
path('api/v1/posts/', include('posts.urls')),
```

Once that is done lets go over to our app level urls, which dosn't exist so we have to make it.

- > touch posts/urls.py
- then edit it

```python
from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail')
]
```

**NOTE:** We don't have a post list or post detail but we will soon.

### Add Serializer

Previousely our view was the relationship between model and our template, but we are not using a template.  But for this we are going to use a serializer so lets go set that up instead. We don't have one.  No biggie, lets make one

- > touch posts/serializers.py

What does a serializer do?  It sets up the connection between the model and allowing that model to have complex data types exposed as JSON. It will also provide deserialization, allowing parsed data to be converted back to complex data types.
The Meta class here is required.  It tells the model what fields to serialize.

```python
from rest_framework import serializers
from .models import Posts

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','author','title','body','created_at')
        model = Posts
```

That is it for this serializer.  This can power a whole bunch of different views.

### Add Views

Lets head over to `posts/views.py`

```python
from rest_framework import generics
from .serializers import PostSerializer
from .models import Posts

class PostList(generics.ListAPIView):

    # Anything that inherits from ListAPI View is going to need 2 things.
    # What is the collection of things, aka the queryset
    # Serializer_class
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


# The postDetail needs the same things
class PostDetail(generics.RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
```

That is it!  This should be done.  Lets check now.

What?  Page not found?  What is going on?

Well we did not set a home-route.

Django is nice enough to tell us right there in the error

So let's navigate to `api/v1/posts/` instead.

No posts showing. But that's ok. We haven't created any.

Lets headover to the admin page and add a post

- Now view `/api/v1/posts/`
- JSON Goodness!!!

Back in the views lets make a little change to something

- change ListAPIView to ListCreateAPIView
- Refresh page and look at the form.
- Add a new post.
- **BOOOM!**

What else can we do?
What other areas of CRUD can we do?

How about viewing a single post...

- `/api/v1/posts/1/`

Back in views make a change

- Change RetrieveAPIView to RetrieveUpdateAPIView
- view page now
- More **booom**

We've got CRU part of CRUD. Now all we need is the D.

- Change RetrieveUpdateAPIView to RetrieveUpdateDestroyAPIView
- refresh page
- See the delete button?
- Ridiculous!

### DRF Summary

That's all it takes to get your Django models served up as JSON instead of html. You're on your way as an API developer!

## Intro to Docker

So that is CRUD via API.  Now we need talk a little about Docker.

Shut down the server and lets get Docker going.

### Installation

First off Docker needs to be installed!

[Get Docker](https://docs.docker.com/get-docker/)

Today, in the case of docker you are going to be pressing the 'I believe button'.

Docker needs a couple files. The first is `Dockerfile`

- > touch Dockerfile

add this

```docker
FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
```

The `Dockerfile` needs to be at the root of your project

That file is responsible for building an `image` that is the basis for the `container`

The container doesn't have Poetry.

So we need to make a `requirements.txt` file by doing this:

- > poetry export -f requirements.txt -o requirements.txt --without-hashes

We'll also need `docker-compose.yml`

- > touch docker-compose.yml

Add this...

```docker
version: '3'

services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
```

### Build & Run Container

To start up the Docker container

- > docker-compose up

Now let's see the site in browser!

You have 2 choices here.

1. Use url `http://127.0.0.1:8000/api/v1/posts/`
2. Use url shown in terminal `http://0.0.0.0:8000/`

If you go with option 2 you'll see an error `Invalid HTTP_HOST header: '0.0.0.0:8000'. You may need to add '0.0.0.0' to ALLOWED_HOSTS.`

So do as error suggests and add '0.0.0.0' to `ALLOWED_HOSTS`

## Docker Summary

You've now `containerized` your Django API.

It might not seem too impressive yet (probably more like a big hassle)

But when it comes time to go into production you're gonna be SO glad you learned Docker.
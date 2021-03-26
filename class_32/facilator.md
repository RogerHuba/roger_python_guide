# Lecture NOTES: Class 32:  Permissions & Postgresql

## Review the Lab

- Show stretch goals and requirements.

## Lambda Functions

- Definition: In Python, a lambda function is a single-line function declared with no name, which can have any number of arguments, but only have one expression. Such a function is capable of behaving similarly to a regular function declared using the Python's def keyword. A lambda function can’t contain any statements. In a lambda function, statements like return, pass, assert, or raise will raise a SyntaxError exception.

> Lets look at some examples:

```python
def this_function(x):
  return x

this_var = this_function(5) 
```

```python
x = lambda x: x

x(5)
```

```python
def add_one(x):
  return x + 1
```

```python
x = lambda x: x + 1

x(10)
```

```python
def sum_all(x, y, z):
  return x + y + z
```

```python
x = lambda x, y, z: x + y + z

x(10)
```

## Topic 1 : Permissions Setup for Demo

- Bring up blogapi-permissions demo
- do a docker-compose up (dcu) to show that posts are avaliable
- show a docker-compose down (dcd)
- run dcu -d to show it in detached mode so you can still use terminal but docker container still running
- run a docker-compose help
- walk through some of the help items
- docker-compose help kill
- You will get use to some of these as you use them.

- Lets move over to Permissions now

> Right now our blog has a serious security problem.
> What is that problem?
> Anyone can look at posts, edit posts, delete posts.  Anyone can do anything anytime.
> How do we deal with that?
> Lets add some permissions to deal with this issue.
> Lets add the ability for app to be aware of a user.
> There is very little code, but it does a whole lot.

- Open `project/settings.py`
- Look at the bottom at REST_FRAMEWORK.

> Looking at the permissions, what does this say? Allow any?  Seems a little 'willy-nilly'

In `project/settings.py`

```python
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ]
}
```

In `project/urls.py` add

```python
path("api-auth/", include("rest_framework.urls")),
```

In `app/permissions.py`

```python
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        # hover over SAFE_METHODS to see which qualify
        if request.method in permissions.SAFE_METHODS:
            return True

        # if we're allowing the purchaser to be null in Model
        # then this will check for that case and allow access
        if obj.owner is None:
            return True

        return obj.owner == request.user
```

**WARNING** Make sure `obj.owner` matches the model field you want. May be `author`,`creator`, etc. depending on resource you are using. If model field differs then update class name as well.

In `app/views.py` add the 2 lines marked `# new`

```python
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Thing
from .permissions import IsOwnerOrReadOnly #new
from .serializers import ThingSerializer


class ThingList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class ThingDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,) #new
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
```

> Now lets look at posts by 2 different users and see how each user can interact with posts
> Log in with Admin, look at post 1.
> Log in with not-admin look at post 2.  Change owner of post 2.

## Topic 2 - Postgres

There are also only a few changes to enable switching to Postgres thanks to Docker and Django

`Dockerfile` is same as last class

```t
# FIRST:  Order Matters in Dockerfiles since they are executed from top-tp-bottom

FROM python:3

# FROM directive is probably the most crucial amongst all others for Dockerfiles. It defines the base image to use to start the build process. It can be any image, including the ones you have created previously. If a FROM image is not found on the host, Docker will try to find it (and download) from the Docker Hub or other container repository. It needs to be the first command declared inside a Dockerfile.


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# The ENV command is used to set the environment variables (one or more). These variables consist of “key value” pairs which can be accessed within the container by scripts and applications alike. This functionality of Docker offers an enormous amount of flexibility for running programs.

# PYTHONDONTWRITEBYTECODE will remove .pyc files from our container which is a good optimization.  
# PYTHONUNBUFFERED will buffer our output so it will look “normal” within Docker for us.

RUN mkdir /code

# Creates a directory / folder

WORKDIR /code

# Then we used the WORKDIR command to create and set /code as our default directory within Docker. That means if in the future we want to run a command like python manage.py runserver we don’t have to also specify it should be run in the /code folder.

COPY requirements.txt /code/

# Copies the file to our workdirectory

RUN pip install -r requirements.txt

# Installs the needed required dependencies into our container

COPY . /code/

# Any code changes locally will be copied over
```

`docker-compose.yml` leaves `web` service largely the same but adds a `db` service

```yml
version: "3.9"

# Our Version

services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    
    # Port that runs in the container

    volumes:
      - .:/code
    ports:
      - "8000:8000"

    # External port / Internal Port mapping  

    depends_on:
      - db
  db:
    image: postgres
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
```

In order for Django to make the switch two things are needed.

1. Some way for python to talk to postgres
1. Updated Database settings

- > poetry add psycopg2-binary
- **BIG SUR WARNING:** Might need to set the system version compatibility
  - > export SYSTEM_VERSION_COMPAT=1
  - then try to add again

Now let's move on to Database settings

- In `project/settings.py` change the `DATABASES` section to...

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",
        "PORT": 5432,
    }
}
```

Make sure the `NAME`, `USER` and `PASSWORD` keys match the corresponding values in `docker-compose.yml`

Believe it or not, that's all the code required.

How does it run?

> docker-compose up --build

View site in browser.

Uh oh. A bunch of errors about relations not existing.

Anybody have a guess why?

Because we are running with a brand new Postgres Database running inside our Docker containe. Not the sqlite file we've been using so far.

The good news is that Django lets you treat them the same (with a few quirks at the edges, but that's rare)

So what did we do when sqlite file wasn't in sync with Django code. Migrate!

But wait, this is all happening **inside** the container and we can't just run `python manage.py migrate` the way we always have, because that is **outside** the container. Outside the container doesn't have Postgres.

The good news is that it's pretty straight forward to reach inside container and run code.

Just start with `docker-compose run [the name of service and whatever else you'd normally type]

> docker-compose run web python manage.py migrate

Easy peasy, just a little extra typing. If the extra typing bugs you then make an alias.

`docker-compose` has a bunch of commands. But we'll mostly be using just a few of them.

We're also going to need to create a super user.

Any guesses how?

> docker-compose run web python manage.py createsuperuser

See, it's not that big a deal to type a few extra words.

### Ephemeral Containers

**GOTCHA ALERT** When `docker-compose down` is run the data is **GONE** when using Postgres.

Ephemeral is a fancy word to mean "not long lasting". You'll see the word alot in the Docker docs. There are some very good reasons containers behave this way. It'll be ok as long as you keep it in mind.

This wasn't the case with Sqlite because it was a file being shared between host file system and container.

So be careful with that. If you want to stop things without losing your data then use `docker-compose stop` and `docker-compose start`, or `docker-compose restart`

Soon we'll be using a 3rd party Database provider so this won't be an issue.

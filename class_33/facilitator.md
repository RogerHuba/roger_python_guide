# Lecture NOTES: Lab: 33 - Authentication & Production Server

## DAD Jokes

- Air used to be free at the gas station, now it's $1.50. You know why? Inflation.
- When I was a kid, my mother told me I could be anyone I wanted to be. Turns out, identity theft is a crime.
- Why couldn't the bicycle stand up by itself? It was two tired!
- What's the difference between a poorly dressed man on a tricycle and a well-dressed man on a bicycle? Attire!
- Why did the invisible man turn down the job offer? He couldn't see himself doing it!
- Why did the stadium get so hot after the game? Because all the fans left.

## Docker Issues

> We had a couple of students that ran into some major docker issues, and one django issue, specifically revolving around Windows and getting docker-compose to install / run.  I want to address this. This is a real thing that you are going to run into on the job. It's is lousey, awful, un-expected, but you are going to run into this often. As technology has increased, setups have gotten better but, there are still things that you will need to figure out. I'm not saying it will be easy, not saying it won't want days to fix, but this is your development environment. These are the tools that you will be using in the industry, so taking the time to learn it now, will only benfit you in the long run.

## Authentication

> Can you prove who you are you say you are

- What are some real world scenarios where you need to authenticae something
  - 21 years old to drink at a bar
  - Movie ticket to get into movie
  - Wrist band at an amusmenet park
  - Stamp on hand at a concert.
- Is this the most efficient way?
  - They could check ID before serving each drink
  - They could go overboard and do retna checks.
  - Check DNA?

Why not?  Want to find the best balance between effectivness and efficiency.

- We do this with wrist-bands
- What is the web equivalent to this?  Token

- How do we do this?  JSON Web tokens.  You did some readings on this.

- There was a little tutorial that was in your reading as well.
[How to Use JWT](https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html)

- Point out:
  - The curl command with the :AuthorizationL Bearer spacing etc.
  - Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9
  - access token short lived
  - refresh token is a bit longer
  - Both are configurable

  If you were to look deeper at JWT you would see somehting like the following:
  ```lots of garbage . lots more junk . and even more un readable things```

  These parts get broken down into a header, payload and a signature which is encoded usoing a theme called Base64.

  header.payload.signature

In this tutorial we are going to partially follow along but make a few tweaks along the way.

> From here load up the demo, have a superuser already created with some data in the database.
> Grab working demo from last class.

Lets start by installing a library

```python
pip install djangorestframework_simplejwt
```

**NOTE** JB did not get 3.8 error with latest libraries as of 3/23/21

We may get an error installing here.  Lets look at the error.  ^3.8 is not compatiable with required packages.  Look at the versions and everything looks good.  Then explain what the version means in pyproject.toml

django = "^3.0.7"
7 = patch level.  No features added
0 = minor version. Enhancments (not breaking anything)
3 = major version. 3 to 4, no gurantee on backwared compatiability
^ = any version as long as it is a 3.*
We see somethinbg else in there.  The '^'

Lets look what this means.
[semver](https://bytearcher.com/articles/semver-explained-why-theres-a-caret-in-my-package-json/)

point out the ~ and the ^
In our case here it means something.  What we want in ours is the ~

Lets make the adjustment in our pyproject for the python version and attempt to re-add our library dependency

Next we need to adjust our settings.py.  Lets add the following tp REST_FRAMEWORK at the bottom of our settings.py:

```python
'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
  ],
```

Our next setps is to add urls and views that are added to app to handle the fact that we are supplying tokens (access and a refresh)


In our project urls.py
> First we need to import a library

```python
from rest_framework_simplejwt import views as jwt_views


path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('api/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
```

Now we have 2 paths, we don't know how they work yet, we don't know what they do exactly, but we do know that when someone hits our site at these url's something is going to happen.

And we see our posts list.  Or do we?  Authentication credentials not provided. How do we do this? So our interaction with this API is not going to be a user but another computer getting some information.  Lets try to replicate this.  You may still have this from previous classes httpie.  You can install this with brew.

**NOTE** May need to brew install httpie

> using httpie lets use the terminal to hit our server:

```bash
http GET localhost:8000/api/v1/blogs  Note you can leave off the localhost
```

We see our Authentication credential error

Lets get a token.  

```python
http POST :8000/api/token/ 
```

We see something missing, username and password

```python
http POST :8000/api/token/ username=admin password=admin
```

Now we have something going on.  We have an access and a refresh token.

Lets grab the access inside the quotes and put in a get request:

```python
http :8000/api/v1/things/ 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgzMTM4NzkyLCJpYXQiOjE2ODMxMzg0OTIsImp0aSI6IjRlZDBkMGEzNTc1NjQ0MmI5NjNjMDM5YTk4ZGQyYjZhIiwidXNlcl9pZCI6MX0.JvWMbsIKsdUnZ1PLCjmUD4RaJyNexP-S7lp1WF_CiV0'
```

if you get a ```HTTP/1.1 301 Moved Permanently``` you are missing a / on the end of the route

Try the token with the request and mess up the token to see the differences.

What other tools could we have used?  Postman?

Let's go back to the login.  We un-intentially broke something that we did not want to break.
Go back and log in with admin and see that it does not work.  How can we fix it?  Add the following to your settings.py

```python
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ]
```

Here is a great site to dig deeper into authentication
[Authentication](https://www.django-rest-framework.org/api-guide/authentication/)

Comment out the default permission classes and show that you no longer need any login to see data

That is all for the authorization portion.  It is not the best or most elegant solution but it works.  Remember that we have to balance the cost vs effenciency.

Next we are going to talk about switching our server runtime from django to gunicorn services for our production server.  This project was not initially set up with docker so lets add that.

```docker
version: '3'

services:
  web:
    build: .
    # command: python /code/manage.py runserver 0.0.0.0:8000
    command: gunicorn blog_api_project.wsgi:application --bind 0.0.0.0:8000 --workers 4
    volumes:
      - .:/code
    ports:
      - '8000:8000'
    depends_on:
    - db

  db:
    image: postgres
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    volumes:
        - postgres_data:/var/lib/postgresql/data/

volumes:
    postgres_data:

```

Point out that we commented out the runserver and not running gunicorn

> workers 4 Said to start 4 individual worker Used to process requests （ One worker It can be understood as a process ）, Will usually worker Number set to CPU Of the core number 2-4 times .


```pip install add gunicorn```

Close down existing running server.

After adding in the dockerfile and docker-compose.yml run a docker-compose up --build.

Expect that it will fail because it is missing the requirements.txt

Before we export to requirements.txt we need to add a couple of dependencies.

```pip
pip freeze requirements.txt > requirements.txt
```

Turn DEBUG to False
re-run docker-compose up --build

go to localhost:8000

Show the new static file
```pip install whitenoise```

add to settings.py
STATIC_ROOT = BASE_DIR / 'staticfiles'

Add to Middleware

```python
MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware', # <--This>
]
```

```pip
pip freeze requirements.txt > requirements.txt
```

> ```docker compose run web python manage.py collectstatic```

```pip install django-cors-headers```

```django
INSTALLED_APPS = [
...
'corsheaders',
...
]

```django
MIDDLEWARE = [
...,
'corsheaders.middleware.CorsMiddleware',
'django.middleware.common.CommonMiddleware',dc
...,
]
```

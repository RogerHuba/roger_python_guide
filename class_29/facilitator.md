# Django X

## Review of This Weeks Feedback

- Should be in the class repo under class-20 readme.md

## Review Todays Lab Requirements

- Give students a glimpse of what is comming up

## Lecture / Demo

> As we have gone through and added to our Django project, we have come across some things(or steps) that we had to complete to get the project up and running. I have teased out a few things like talking about snippits, and templates. Today we are going to push the envelope of "efficient" to the next level. This may inspire you to push the envelope even further on your own.

- You have heard me mention this DjangoX business, lets jump in and see what it is.
- [DjangoX](https://github.com/wsvincent/djangox)
- William S Vincent is the author of the Django for beginners, and the Django for professional, and Django for API book series.
- During the creation of his projects for books, he got tired of doing the same thing over and over again with all of the same steps. The creation process was not very DRY to him. He notices that there were ALOT of similar things that were the same across every site that he had to do before he got into the unique work for that project.  That is how DjangoX was born.
- As we go through the template, we see a few ways to install. What do we notice right off?  No Poetry. Fear not, it is pretty simple to convert over to poetry and get this running.
- Point out what is not talked about here in the Features. The Django custom users. If you apply your migrations, Django creates a user_table in the DB. If you want to make changes to that user table, it is a real pain to do. DjangoX takes care of that up front.
- Talk about whitenoise. We have not had to deal with this yet but when we move to production, you normally do not server your static files from the same place you do your code. You will normally use a Dontent Delivery Network (CDN) because it is cheaper and more efficient. Whitenoise gives us a lot of help.
- How did WVincent get this made. Well, via GitHub of course. You actually have the ability to turn any repository you have now into a template with the click of a button. With this we can use his template, and even create your own template.

> Click on the Use This Template
    > Select an Owner
    > Give it a name things-tracker
    > Give Description
    > Not Grabbing Branches - Create repo from template
> Should only take a few seconds.
> Navigate to my Github and now I have a DjangoX Project
    > This is mine, not a fork, but mine with a nice template. I can do whatever I want with this
> In the upper left corner you can see it was copied from wvincent
> It is mine, and I want to use it, so I think it is time to clone it
> Click the Green Code Dropdown and select clone.
> Clone the repo to computer
> It's time to look at the instructions.  Scroll
> Clone down your repo to your computer
> Walk through looking at pipfile with requirements.
> Lets do a conversion from pipenv to Poetry.
> `poetry init -n`

```python
poetry add Django django-allauth django-crispy-forms django-debug-toolbar whitenoise
poetry add --dev black flake8
```

### Fire up the project

> poetry shell if not already there
> Lets see if this in enough to get up and running
> ALTERNATIVE: Could show pmp. Run alias and show pmp
>`python manage.py runserver`
> Take a little time to go into the .zshrc file and show alias
> `code ~/.zshrc
> Look at the missing migrations. Few more than we are use to.
>`pmp migrate`
> Go through things on the screen like the DjangoX which is a home re-fresh, the login, the sighup, the applied styles.
> One thing to note in the login is the email and password. Django default is username and password.
> We can signup with a email and password. This seems to be wired up pretty good right out of the box
> Now there are some additiional thing we may want to add like, email verification as an example.

### Remove files we don't need and talk a little about them

- Dockerfile
- docker-compose.yml
- requirements.txt
- Pipfile
- Pipfile.lock

> We notice some thing right away that are here.  Templates folder, static folder, instead of a project folde we have a config folder. Look through the settings file and look for things that are normal and then things that are not. We look around as needed.  

## Add Things App to project

- Lets see if we can just add an application to the project
- python manage.py startapp things
- Now there is no way this knew we were going to call the app things so we have to still do some manual things.

## URL Time (Project)

- add `things` to `INSTALLED_APPS`
- Next lets take a look at the project URLS.

> This looks little different. We have this debug setting.

- add `path('things', include('things.urls')),` to urlpatterns.

## URL Time (APP)

- `touch things/urls.py`
- QUESTION:  Does anyone know what is suppose to go in the URLS?
- ANSWER: Rhetorical.  You all know already.
- can point them to:
  - `https://code.visualstudio.com/docs/editor/userdefinedsnippets`
- Use `DJUC`

## Views Time

- Delete what is there
- Anyone remember what to put here?
- Sure would be great if I had a snippit for here.
- use `DJVC`
- That sure is a whole lot easier using snippits
- Notice that this loads everything that I need(almost)
- I will need to add fields for my forms after I update the model.

## Model time

- I don't have a snippit for this. Models are a little different because they are all different.

```python
from django.contrib.auth import get_user_model
from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(default="")
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('thing_detail', args=[str(self.id)])
```

## Admin Time

- Add Thing model to admin.py so it's accessible in Admin

```python
from django.contrib import admin
from .models import Things

admin.site.register(Things)
```

- Do migration for Thing model
- > python manage.py makemigrations thing
- > python manage.py migrate

## Template Time

- go to .oh-my-zsh -> custom -> example.zsh
- Show the template creation alias I have written.
- from the base dir, run crud_templates things things
- Then run tree templates

- In things-list run `dtc`
- point out that we need to add _base.html
  
## TESTING Time

- Lets see if this gets things up and running
- If it does then hit the /things route and we should see Thing List comming soon
- After getting through any errors talk about streamlining things

- If you did not makemigrations after updating model may have to do this.
- Still need to update views with model informaiton in fields "name", "description" etc

- We can update to crispy forms in our templates now pretty easily (something that came with DjangoX)

```raw
{% extends '_base.html' %}
{% load crispy_forms_tags %}

{% block content %}
<h2>Create Snack</h2>
<form method="post" class="uniForm">
  {% csrf_token %}
  {{ form|crispy }}
  <input type="submit" value="SAVE">
</form>
{% endblock content %}

```

### URL Time

- Add `path('snacks/', include('snacks.urls')),` to urlpatterns in `config/urls.py`
  - **NOTE:** snacks is not required to have it's own url path.
    - It could be that pages in `pages` app (or elsewhere) use Snack model as needed.
- create `snacks/urls.py`

```python
from django.urls import path
from .views import SnackListView

urlpatterns = [
    path('', SnackListView.as_view(), name='snack_list')
]
```

- Add rest of CRUD url patterns
- This is also a great time for a snippet

- `python manage.py runserver`

### Tweak model for full CRUD

- For create/update will need to add to `snacks/models.py`

```python
from django.urls import reverse
...
    def get_absolute_url(self):
        return reverse('snack_detail', args=[str(self.id)])
```

### SNACK CRUD

- Run server again and do some CRUD on your snacks

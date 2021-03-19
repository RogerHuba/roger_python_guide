# Django X

## Review of THis Weeks Feedback

- Should be in the class repo under class-20 readme.md

## Review Todays Lab Requirements

- Give students a glimpse of what is comming up

## Lecture / Demo

> Although we are going to be using a tool that will simplify our ability to use a django custom
> user, we left the heavy reading in on how to do it mannually so that you will have an idea 
> what DjangoX is doing to simplify things.  As developers we 

- [DjangoX](https://github.com/wsvincent/djangox)

> Click on the Use This Template
    > Select an Owner
    > Give it a name snacks - x
    > Give Description
    > Not Grabbing Branches - Create
> Navigate to my Github and now I have a DjangoX Project
    > This is mine, not a fork, but mine with a nice template.
> In the upper left corner you can see it was copied from wvincent
> It is mine, and I want to use it, so I think it is time to clone it

- Click the Green Code Dropdown and select clone.
- Clone the repo to computer

> It's time to look at the instructions.  Scroll
> Clone down your repo to your computer
> Walk through looking at pipfile with requirements.
> Manually install items from piplock file
> 
- **WARNING:** On Mac you may get an error and need to re-set the system version compatibility due to upgrade issues with with Big Sur, the name of latest version of Mac OS.
- ```export SYSTEM_VERSION_COMPAT=1```
  - Then do poetry add again
  - Or find a TA
- > poetry add --dev black flake8

### Remove files we don't need and talk a little about them

- Dockerfile
- docker-compose.yml
- requirements.txt
- Pipfile
- Pipfile.lock

> We notice some thing right away that are here.  Templates folder, static folder, instead of a project folde we have a config folder.
> Look through the settings file and look for things that are normal and then things that are not.
> We look around as needed.  
### Fire up the project

- > poetry shell
- > python manage.py migrate
- > python manage.py createsuperuser
- > python manage.py runserver
  - look around
- Point out the log in / sign up features and tease that we'll need to do same in next module.

## Add Snacks App to project

- python manage.py startapp snacks
- add `snacks` to `INSTALLED_APPS`

## Model time

```python
from django.contrib.auth import get_user_model
from django.db import models

class Snack(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(default="")
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


    def __str__(self):
        return self.name
```

- Add Snack model to admin.py so it's accessible in Admin

```python
from django.contrib import admin
from .models import Snack

admin.site.register(Snack)
```

- Do migration for Snack model
- > python manage.py makemigrations snacks
- > python manage.py migrate

### View Time

```python
from django.views.generic import ListView
from .models import Snack

class SnackListView(ListView):
    template_name = 'snacks/snack-list.html'
    model = Snack
```

- Add more views as needed
- This would be a **GREAT** time to use a snippet
- Best way is to use [Snippet Generator](https://snippet-generator.app/){:blank}
- Refer to included [SNIPPETS.md](./SNIPPETS.md){:blank} for examples snippets built with Snippet Generator.


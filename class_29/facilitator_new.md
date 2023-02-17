# Django + Tailwinds + Flowbite

## Review Todays Lab Requirements

- Give students a glimpse of what is comming up in lab

## Lecture / Demo

- Do a quick talk about making a template.  Point out DjangoX and go through a few things.
- [DjangoX](https://github.com/wsvincent/djangox)
- William S Vincent is the author of the Django for beginners, and the Django for professional, and Django for API book series.During the creation of his projects for books, he got tired of doing the same thing over and over again with all of the same steps (like we have done in the most recent labs). The creation process was not very DRY. He notices that there were ALOT of similar things that were the same across every site that he had to do before he got into the unique work for that project.  That is how DjangoX was born.
- As we go through the template, we see a few ways to install with different environments.
- Point out what is not talked about here in the Features. The Django custom users. If you apply your migrations, Django creates a user_table in the DB. If you want to make changes to that user table, it is a real pain to do. DjangoX takes care of that up front. (We are changing this today)
- Talk about whitenoise. We have not had to deal with this yet but when we move to production, you normally do not server your static files from the same place you do your code. You will normally use a Dontent Delivery Network (CDN) because it is cheaper and more efficient. Whitenoise gives us a lot of help.
- How did WVincent get this made. Well, via GitHub of course. You actually have the ability to turn any repository you have now into a template with the click of a button. With this we can use his template, and/or even create your own template.
  
### Get a quick things project / app up and running

```bash
mkdir project folder
initialize ve
pip install django
shell into ve
django-admin startproject settings .
python manage.py startapp things
```

- Add things to project
- Update settings urls.py

```python
# Project urls.py
from django.urls import path, include)
urlpatterns = [
    path('', include('siteapp.urls')),
]
```
- Create urls.py inside of the application

```bash
touch siteapp\urls.py
```

- Add the following code to the app urls.py

```python
from django.urls import path
from .views import ThingListView, ThingDetailView, ThingCreateView, ThingUpdateView, ThingDeleteView, ThingAboutView

urlpatterns = [
    path('', ThingListView.as_view(), name='thing_list'),
    path('create/', ThingCreateView.as_view(), name='thing_create'),
    path('about/', ThingAboutView.as_view(), name='thing_about'),
    path('<int:pk>/', ThingDetailView.as_view(), name='thing_detail'),
    path('<int:pk>/delete/', ThingDeleteView.as_view(), name='thing_delete'),
    path('<int:pk>/update', ThingUpdateView.as_view(), name='thing_update'),
]
```

- Update the App Views
```python
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, DeleteView, CreateView
from .models import Thing
from .forms import ThingCreateForm, ThingUpdateForm  # ADD LATER

class ThingListView(ListView):
    template_name="things-list.html"
    model = Thing
    context_object_name = 'things'

class ThingDetailView(DetailView)
    template_name="thing-detail.html"
    model = Thing

class ThingCreateView(CreateView):
    template_name = "things-create.html"
    fields = '__all__'
    form_class = ThingCreateForm  # ADD LATER and remove fields

class ThingUpdateView(UpdateView):
    template_name = "things-update.html"
    model = Thing
    fields = '__all__'
    form_class = ThingUpdateForm  # ADD LATER and remove fields


class ThingDeleteView(DeleteView):
    template_name = "things-delete.html"
    model = Thing
    success_url = reverse_lazy("thing_list")


class ThingAboutView(TemplateView):
    template_name = "things-about.html"
```

- Do a quick update to Thing model.

```python
from django.db import models
from django.contrib.auth import get_user_model


class Thing(models.Model):
    name = models.CharField(max_length=64, unique=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(default="")

    def __str__(self):
        return self.name
```
- Add the model to admin

```python
from django.contrib import admin
from .models import Thing

admin.site.register(Thing)
```

- create template folder
  
```bash
mkdir templates
touch templates/_base.html
touch templates/thing-list.html
touch templates/thing-detail.html
touch templates/thing-update.html
touch templates/thing-create.html
touch templates/thing-delete.html
touch templates/thing-about.html
```

- add templates to template area in settings.py

- Update _base.html

```html
<!doctype html>
<html lang="en">
<head>
    <title>Things</title>
</head>
<body>
    <nav>
        <ul>
        
        </ul>
    </nav>
    {% block content %}
        <h1>Things in the House!</h1>
    {% endblock content %}
</body>
```

- Update things-list.html
- 
```html
{% extends '_base.html' %}

{% block content %}
      <ul>
      {% for thing in things %}
          <li>
              <a href="{% url 'thing_detail' thing.pk %}">{{ thing.name }}</a>
          </li>
      {% endfor %}
  </ul>
{% endblock content %}
```

- Update things-detail.html
```html
{% extends '_base.html' %}

{% block content %}
    <h1>Things Detail</h1>
    <h2>Name: {{ thing.name }}</h2>
    <h3>Owner: {{ thing.owner }}</h3>
    <p>Description:  {{ thing.description }}</p>

{% endblock content %}
```

-Update things-create.html

```html
{% extends '_base.html' %}

{% block content %}
    Coming Soon
{% endblock content %}
```

-Update things-update.html

```html
{% extends '_base.html' %}

{% block content %}
    Coming Soon
{% endblock content %}
```

-Update things-delete.html

```html
{% extends '_base.html' %}

{% block content %}
    <div>
        <h1>Delete Thing</h1>
        <form action="" method="post">
            {% csrf_token %}
            <p>Do you really want to delete "{{ thing.name }}"?</p>
            <input type="submit" value="OK">
        </form>
    </div>
{% endblock content %}
```

-Update things-about.html

```html
{% extends '_base.html' %}

{% block title %}
    UPDATE ME
{% endblock title %}

{% block content %}
    Coming Soon
{% endblock content %}
```

- python manage.py runserver
- Make sure there are no errors to this point.

### Crispy Forms

- First we pip install django-crispy-forms

- First we need to update templates with the form we are about to create.
- thing_update.html
```html
{% extends 'base-form-page.html' %}

{% block title %}
UPDATE ME
{% endblock title %}
```

- thing_create.html
```html
{% extends 'base-form-page.html' %}

{% block title %}
CREATE ME
{% endblock title %}
```

- thing_delete.html
```html
{% extends '_base.html' %}
{% load crispy_forms_tags %}  ADD THIS

{% block content %}

  <div>

  <h1>Delete Thing</h1>

  <form action="" method="post">
  {% csrf_token %}
  <p>Do you really want to delete "{{ thing.name }}"?</p>
  <input type="submit" value="OK">
</form>
  </div>

{% endblock content %}
```

- Add base-form-page.html
```html
{% extends '_base.html' %}
{% load crispy_forms_tags %}


{% block content %}

{% crispy form %}


{% endblock content %}
```

- Add forms to applicatiopn
```bash
touch siteapp/forms.py
```

- Add the following to forms.py

```python
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from .models import Thing
from django.contrib.auth import get_user_model


class BaseThingForm(forms.ModelForm):
    label = "Submit"

    class Meta:
        model = Thing
        fields = "__all__"

    name = forms.CharField(
        label="Enter a favorite thing.",
        max_length=80,
        required=True
    )

    rating = forms.IntegerField(
        label="Rate your thing",
        required=False,
        min_value=0,
        max_value=10
    )

    reviewer = forms.ModelChoiceField(queryset=get_user_model().objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'description',
            'owner',
            Submit('submit', self.label, css_class="submit"),
        )

        self.helper.label_class = "form-label"
        self.helper.form_class = "form"


class ThingCreateForm(BaseThingForm):
    label = "CREATE"


class ThingUpdateForm(BaseThingForm):
    label = "UPDATE"
    
```

### Custom User Model

- create a account app

```python
python manage.py startapp account
```

- Add app to installed apps
- Build a new custom user mode.
- Update account\models.py

```python
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager  # Perm and Base are after

# The AbstractBaseUser is the integration to Django for the custom user model.

class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    user_name = models.CharField(max_length=30, unique=True)
    about = models.TextField(max_length=500, blank=True)
    last_name = models.TextField(max_length=30, blank=True)
    first_name = models.TextField(max_length=30, blank=True)
    # THESE ARE REQUIRED
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    # If you have a secondary activation methon like email, set the following to false
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # Can add other things: f name, l name, dob, etc...

    # The user_name field is poorly named by Django, but this is what sets the login field.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    # To use the Django built in permissions (suggested), we need to import and extend PermissionsMixin.


    # Now we will write the manager for our custom user model. We will need to import the BaseUserManager

    # Initially we will setup a manager class and 2 methods from BaseUserManager to do our work for us.

class MyAccountManager(BaseUserManager):
       
    def create_superuser():
        pass
       
    def createuser():
        pass
    
class MyAccountManager(BaseUserManager):
    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)

        if not username:
            raise ValueError("User must have a username")

        if other_fields.get('is_admin') is not True:
            raise ValueError("Superuser must be assigned to is_admin=True")

        if other_fields.get('is_staff') is not True:
            raise ValueError("Superuser must be assigned to is_staff=True")

        if other_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True")

        user = self.create_user(email, username, password, **other_fields)
        user.save()
        return user       
                
    def create_user(self, email, username, password, **other_fields):
        # This is all the required fields that are set for an account
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)

        if not username:
            raise ValueError("User must have a user name")

        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user


# add objects in class Account around REQUIRED_FIELDS in Account Class
    objects=MyAccountManager()    
```

- Once all of that is completed in the model, head to the project setting file.

```python
AUTH_USER_MODEL='account.Account'
```
This overwrites the built in user within the app.

- Lastly we need to update the admin.py in account

```python
from django.contrib import admin
from .models import Account

admin.site.register(Account)

```

- Now can makemigrations and migrate
- Before mucking up your database and having to delte everything, you can use the --dry-run flag on makemigrations

```bash
python manage.py makemigrations --dry-run
```

- Notice that it did the dry run in both models.  We are only going to make migrations for account right now.

```bash
python manage.py makemigrations account
```

- Test in admin. Look at the user.  Information is to basic there. Lets update that a little in the admin.py

```python
from django.contrib.auth.admin import UserAdmin

# We can customize our view of things in the admin page
class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'username', 'last_name')
    list_filter = ('email', 'username', 'is_active', 'is_superuser')
    ordering = ('-date_joined',)
    list_display = ('email', 'username', 'is_active', 'is_superuser')
    readonly_fields = ['date_joined', 'last_login']

# Because we are cutomizing, we will need to add the field sets in order to modify a record:

fieldsets = (
    (None, {'fields': ('email', 'username', )}),
    ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    ('Personal', {'fields': ('about', 'last_name', 'first_name')}),
)

# Will also have to customize the add account area

add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'username', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')
    }),
)

admin.site.register(Account, UserAdminConfig)
```

### Time for tailwinds, flowbite

- Update Django a little to prepare
- pip install django-compressor
- add to isntalled apps 'compressor'
- Add to bottom of settings
  COMPRESS_ROOT = BASE_DIR / 'static'
  COMPRESS_ENABLED = True
  STATICFILES_FINDERS = ('compressor.finders.CompressorFinder',)

create file at static/src/input.css

update the _base.html
```
<!-- templates/_base.html -->

{% load compress %}
{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Things with Tailwinds and Flobite</title>

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

- add to things-list.html
```
{% block content %}
  <h1 class="text-3xl text-green-800">Things with Django + Tailwind CSS + Flowbite</h1>
{% endblock content %}
```

- run pmp runserver
- Expect to get an error that the output.css file does not exist. That will be fixed once we install tailwind CSS.

#### Tailwinds CSS

- npm install -D tailwindcss
- npx tailwindcss init
- Configure the template paths using the content value inside the Tailwind configuration file
```
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

- Update the statis/src/input.css with
```
/* static/src/input.css */

@tailwind base;
@tailwind components;
@tailwind utilities;

```

- run this
- ```npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch```

- runserver and show the updates so far
- chance the color of the background in _base.html

#### Flowbite

- run npm i flowbite
- update tailwind.config.js

```
module.exports = {

    plugins: [
        require('flowbite/plugin')
    ]
}
```

- Add content value to list tailwind.config.js

```
'./node_modules/flowbite/**/*.js'
```

- Add to the end of _base.html before the end of the body
```<script src="https://unpkg.com/flowbite@1.6.0/dist/flowbite.min.js"></script>```

- Now it is Time to add a quick nav bar to our application.  Lets update the _base.html.

```html
  <nav class="bg-white border-gray-200 px-2 sm:px-4 py-2.5 rounded dark:bg-gray-900">
    <div class="container flex flex-wrap items-center justify-between mx-auto">
      <a href="https://flowbite.com/" class="flex items-center">
        <img src="https://flowbite.com/docs/images/logo.svg" class="h-6 mr-3 sm:h-9" alt="Flowbite Logo"/>
        <span class="self-center text-xl font-semibold whitespace-nowrap dark:text-white">Thing Tracker</span>
      </a>
      <button data-collapse-toggle="navbar-default" type="button"
              class="inline-flex items-center p-2 ml-3 text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
              aria-controls="navbar-default" aria-expanded="false">
        <span class="sr-only">Open main menu</span>
        <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"
             xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd"
                d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
                clip-rule="evenodd"></path>
        </svg>
      </button>
      <div class="hidden w-full md:block md:w-auto" id="navbar-default">
        <ul
          class="flex flex-col p-4 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
          <li>
            <a href="{% url 'thing_list' %}"
               class="block py-2 pl-3 pr-4 text-white bg-blue-700 rounded md:bg-transparent md:text-blue-700 md:p-0 dark:text-white"
               aria-current="page">Home</a>
          </li>
          <li>
            <a href="{% url 'thing_about' %}"
               class="block py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent">About</a>
          </li>
          <li>
            <a href="{% url 'thing_create' %}"
               class="block py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent">Create</a>
          </li>

          <li>
            <button id="theme-toggle" type="button"
                    class="text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 rounded-lg text-sm p-2.5">
              <svg id="theme-toggle-dark-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20"
                   xmlns="http://www.w3.org/2000/svg">
                <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"></path>
              </svg>
              <svg id="theme-toggle-light-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20"
                   xmlns="http://www.w3.org/2000/svg">
                <path
                  d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"
                  fill-rule="evenodd" clip-rule="evenodd"></path>
              </svg>
            </button>
          </li>

        </ul>
      </div>
    </div>
  </nav>
  ```

  - The following will add a darkmode to your application.
  
  ```javascript
<script>
    
      var themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
      var themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');
    
      // Change the icons inside the button based on previous settings
      if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        themeToggleLightIcon.classList.remove('hidden');
      } else {
        themeToggleDarkIcon.classList.remove('hidden');
      }
    
      var themeToggleBtn = document.getElementById('theme-toggle');
    
      themeToggleBtn.addEventListener('click', function () {
    
        // toggle icons inside button
        themeToggleDarkIcon.classList.toggle('hidden');
        themeToggleLightIcon.classList.toggle('hidden');
    
        // if set via local storage previously
        if (localStorage.getItem('color-theme')) {
          if (localStorage.getItem('color-theme') === 'light') {
            document.documentElement.classList.add('dark');
            localStorage.setItem('color-theme', 'dark');
          } else {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('color-theme', 'light');
          }
    
          // if NOT set via local storage previously
        } else {
          if (document.documentElement.classList.contains('dark')) {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('color-theme', 'light');
          } else {
            document.documentElement.classList.add('dark');
            localStorage.setItem('color-theme', 'dark');
          }
        }
    
      });
    </script>
  ```
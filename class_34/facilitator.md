# Django Project

- Visit [API Quick Start](https://github.com/codefellows/python-401-api-quickstart)
- Encourage students to instepct the template repository
- Maybe create your own template?

> Because we are going to be deploying on the internet, we need to do a few things before we can move forward:

- Update project to use django-environ
- Update settings.py with .env variables
- Update docker-compose.yml to use .env
- Update our DB to the internet
- Update project to use django-cors-headers

- > Start with project from previous class
  - If you have get errors installing on Mac
    - > `export SYSTEM_VERSION_COMPAT=1`
    - > poetry install if copied
    - > poetry shell

## Update .env

- > Touch .env file inside the  project folder

```env
SECRET_KEY=put-real-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
DATABASE_NAME=postgres
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=db
DATABASE_PORT=5432
```

## Update Settings

- `poetry add django-environ`
- Update `project/settings.py` to use `django-environ`
- add `import environ` below path in settings.py

- read in the environment variables on next line
- `environ.Env.read_env()`

- > Add the following:
- > This will force the environment to production if .env missing

```python
env = environ.Env(
    DEBUG=(bool, False)
)

# reading .env file
environ.Env.read_env()
```

- > Change the following items

```python
SECRET_KEY = env.str('SECRET_KEY')
DEBUG = env.bool('DEBUG')
ALLOWED_HOSTS = tuple(env.list('ALLOWED_HOSTS'))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT')
    }
}
```

> Test Container
> Now it is time to update the docker-compose.yml to use variables
[docker-compose variables](https://docs.docker.com/compose/environment-variables/)

touch .env in root folder. Point out that this is different from the .env in the project folder.

```env
DATABASE_NAME=postgres
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
```

-Update docker-compose

```docker
environment:
  - POSTGRES_DB=${DATABASE_NAME}
  - POSTGRES_USER=${DATABASE_USER}
  - POSTGRES_PASSWORD=${DATABASE_PASSWORD}
```

test-local

## Remote Database Time

- Set up an account and [ElephantSQL](https://www.elephantsql.com/)
  - **NOTE:** No credit card required for free tier.
- Create Database with name `blog-api-db` on the free plan.
- Select any available region you like.
- Click on the new DB to get details.
- Update project `.env` file with relevant details from your database.
  - DB_NAME=laxuqqyk
  - DB_USER=laxuqqyk
  - DB_PASSWORD=vXR-YPh867JP-kATaTgh6KsUBNTWdjCG
  - DB_HOST=kashin.db.elephantsql.com
  - DB_PORT=5432

- > Comment out DB stuff in docker-compose.yml

- dcu --build -d
- docker-compose run web python manage.py migrate
- docker-compose run web python manage.py createsuperuser
- Hit admin route and add some stuff, see it there.
- Go to Elephant DB and look at table Data

## Add CORS

> It is time to deply our Django app to the internet. There is one more thing we need to add to our project.  
> django-cors-headers. A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses. This allows in-browser requests to your Django application from other origins.

```python
pip install whitenoise (should already be there)
pip install django-cors-headers
```

Add this to settings.py in INSTALLED_APPS
>'whitenoise.runserver_nostatic',
>'corsheaders',

There are also 2 items in middleware to add:

The corsheader needs to be high up on the middleware and it will handle cross origin issues for us nased on the list we entered.

[CORS SITE](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

```python
MIDDLEWARE = [
    #ADD 'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #ADD 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

- >We also need to add a whitelist for our CORS.
- >We will add this to the bottom of our settings.py

```python
CORS_ORIGIN_WHITELIST = tuple(env.list("ALLOWED_ORIGINS"))
CORS_ALLOW_ALL_ORIGINS = env.bool("ALLOW_ALL_ORIGINS")
```

- > Add this to the .env

```python
ALLOWED_ORIGINS=http://localhost:3000
ALLOW_ALL_ORIGINS=True
```

**NOTE** Be sure to shutdown server, update requirements.

Add project to a GH repository (Don't forget .gitignore)
[Global Git Ignore](http://egorsmirnov.me/2015/05/04/global-gitignore-file.html)

## Deploy Project - AWS

[A Quick Reference](https://stackabuse.com/deploying-django-applications-to-aws-ec2-with-docker/)
[Reference 2](https://testdriven.io/blog/django-docker-https-aws/)
[Reference 3](https://try.digitalocean.com/deploy-django/?utm_campaign=amer_app_platform_kw_en_cpc&utm_adgroup=deploy_django&_keyword=%2Bdjango%20%2Bdeploy&_device=c&_adposition=&utm_content=conversion&utm_medium=cpc&utm_source=google&gclid=CjwKCAjwr_uCBhAFEiwAX8YJgXskoOQkDmIscZOYjfdztw60P2h2mynnRyRPbIgl2mNmAtvNsDU1QRoCCt8QAvD_BwE)
[Reference 4](https://gist.github.com/npearce/6f3c7826c7499587f00957fee62f8ee9)
[Reference 5](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html)

### AWS

- Log into the AWS Console.
- [AWS Login](https://aws.amazon.com/console/)
- Go to EC2 and Launch Instance
- Select Amazon Linux 2 AMI (Free Tier Eligible)
  - Select t2.micro
  - Review and Launch Instance
  - Launch Instance*
  - Create a new Key Pair (things-api)
  - Be sure to download PEM and save file
  - Launch Instance
  - Edit Security Group for Inbound Data
    - Custom TCP 8000 Anywhere 0.0.0.0/0

### SSH

- Navigate to .ssh
  - copy pem file to .ssh
  - run chmod 400 on file. (chmod 400 name-of-file.pem)
- Obtain the Ec2 Instance Public IP
- EC2->Instance->check Box -> Connect ->SSH Client
- ssh -i "blog-api.pem" ec2-user@ec2-54-203-8-100.us-west-2.compute.amazonaws.com

## EC2 Instance

- See updates needed sudo yum update
- sudo yum install git
- clone repo (Be sure to select HTTPS)
  - Add .env stuff in project file
- sudo yum install -y docker
- sudo usermod -a -G docker ec2-user
- sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
- sudo chmod +x /usr/local/bin/docker-compose
- sudo service docker start
- sudo chkconfig docker on
- sudo rm /etc/localtime
- sudo docker swarm init

- sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
- sudo reboot
- Update allowed_hosts with EC2 IP and Change Debug to False

Test the Public IP

## Deploy Project - Heroku Time

- install [heroku cli](https://devcenter.heroku.com/articles/heroku-cli)
- `heroku apps:create snacks-api`
- Check remote with `git remote -v`
- If heroku remote doesn't show then `heroku git:remote -a snacks-api`
- Create `heroku.yml` in root folder.
- Add below text to `heroku.yml`

```yaml
build:
  docker:
    web: Dockerfile
release:
  image: web
  command:
    - python manage.py collectstatic --noinput
run:
  web: gunicorn project.wsgi
```

- **EXTRA IMPORTANT STEP**
- `heroku stack:set container`
- Add/Commit
- `git push heroku main`
- Go to [heroku](https://www.heroku.com/)
- Login takes you to dashboard
- Select your app
- Go to settings
- Click `reveal config vars` button
- Add config vars to match `.env` file
- `ALLOWED_HOSTS` should match the heroku URL for your app.
  - Click `Open app` button to see it
  - Leave out the `https://` and trailing slash.
  - E.g. snacks-api.herokuapp.com
- It can take a minute for the environment variable changes to take effect
- Once site is ready then see if you can log in, create snacks, etc.
  - It will be ugly because the styling was lost.
  - This is due to the Heroku file system's "ephemeral" nature
  - One way to handle issue is to run `collectstatic` locally then commit the `staticfiles` to heroku.

## Stretch

- Handle collecting static files so that styling doesn't go away with DEBUG off
  - There is some trickiness here, especially on Heroku. Often static assets would be on CDN so it's not an issue.

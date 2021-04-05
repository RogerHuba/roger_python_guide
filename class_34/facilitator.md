# Django Project 

- Visit [API Quick Start](https://github.com/codefellows/python-401-api-quickstart)
- Show process of `Use this Template`
  - Encourage students to create their own template repository to their liking
- inspect `pyproject.toml`
  - point out the new (or more recent) libraries
    - django-cors-headers (Cross Origin Resource Sharing)
      - Allows in-browser requests to your Django application from other origins / domains
    - django-environ
      - Used for hiding certain environment variables
    - whitenoise
      - Allows for static content after in production
    - etc.
- > Start with poroject from previous class
  - If you have get errors installing on Mac
    - > `export SYSTEM_VERSION_COMPAT=1`
    - > poetry install if copied
    - > poetry shell

## Update .env

- > Touch .env file in porject folder

```env

SECRET_KEY=put-real-secret-key-here
DEBUG=True

ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
ALLOW_ALL_ORIGINS=True

#DATABASE_ENGINE=django.db.backends.postgresql
#DATABASE_NAME=postgres
#DATABASE_USER=postgres
#DATABASE_PASSWORD=postgres
#DATABASE_HOST=db
#DATABASE_PORT=5432
```

- Name it `.env` in same folder
  - Inspect the `.env` a bit

## Update Settings

- Update `project/settings.py` to use `django-environ`
  - > add `import environ` below path

- read in the environment variables on next line
- `environ.Env.read_env()`
- > Add the following 

- > This will force the environment to production if .env missing
```python
env = environ.Env(
    DEBUG=(bool, False)
)
```

- > Add the following

```python
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
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT')
    }
}
```

## Test Local First

## Remote Database Time

- Set up an account and [ElephantSQL](https://www.elephantsql.com/)
  - **NOTE:** No credit card required for free tier.
- Create Database with name `blog-api-db` on the free plan.
- Select any available region you like.
- Click on the new DB to get details.
- Update `.env` file with relevant details from your database.
  - DB_NAME=laxuqqyk
  - DB_USER=laxuqqyk
  - DB_PASSWORD=vXR-YPh867JP-kATaTgh6KsUBNTWdjCG
  - DB_HOST=kashin.db.elephantsql.com
  - DB_PORT=5432

- > Comment out DB stuff in docker-compose.yml

## Test API Remote

- dcu --build -d
- docker-compose run web ./manage.py migrate

## Add CORS

```python
poetry add whitenoise (should already be there)
poetry add django-cors-headers
```

Add this to settings.py in INSTALLED_APPS
>'whitenoise.runserver_nostatic',
>'corsheaders',

There are also 2 items in middleware to add:

The corsheader needs to be high up on the middleware and it will handle cross origin issues for us nased on the list we entered.

```python
MIDDLEWARE = [
    # 'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
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
ALLOW_ALL_ORIGINS=True
ALLOWED_ORIGINS=http://localhost:3000
```

**NOTE** Be sure to shutdown server, update requirements.

## Deploy Project - AWS
[A Quick Reference](https://stackabuse.com/deploying-django-applications-to-aws-ec2-with-docker/)
[Reverence 2](https://testdriven.io/blog/django-docker-https-aws/)
[Reference 3](https://try.digitalocean.com/deploy-django/?utm_campaign=amer_app_platform_kw_en_cpc&utm_adgroup=deploy_django&_keyword=%2Bdjango%20%2Bdeploy&_device=c&_adposition=&utm_content=conversion&utm_medium=cpc&utm_source=google&gclid=CjwKCAjwr_uCBhAFEiwAX8YJgXskoOQkDmIscZOYjfdztw60P2h2mynnRyRPbIgl2mNmAtvNsDU1QRoCCt8QAvD_BwE)
[Reference 4](https://gist.github.com/npearce/6f3c7826c7499587f00957fee62f8ee9)
[Reference 5](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html)

### AWS

- Log into the AWS Console.
- Go to EC2 and Launch Instance
- Select Amazon Linus 2 AMI
  - Select t2.micro
  - Launch Instance
  - Create a new Key Pair (blog-api)
  - Be sure to download PEM
  - Launch Instance
  - Edit Security Group for Inbound Data Custom TCP 8000 0.0.0.0/0  

### SSH

- Navigate to .ssh
  - copy pem file to .ssh 
  - run chmod 400 on file.
- Obtain the Ec2 Instance Public IP
  - ssh -i blog-api.pem ec2-user@ec2-34-211-158-52.us-west-2.compute.amazonaws.com

## EC2 Instance

- See updates needed sudo yum update
- sudo yum install git
- clone repo
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
- Add missing .env
- Update allowed_hosts


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

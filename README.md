# dj_foo
my minimal django project boilerplate
- has custom user model
- celery setup
- example app with background tasks


## setup steps
- checkout the code
```bash
git clone git@github.com:Omie/dj_foo.git <project-name>
```
- rename the project name in different places as required.

We could have done a cookiecutter template to achieve the same thing faster,
however, since I share this repo to those learning django, I want them to know how it is configured internally
```
- `cd <project-name>; mv dj_foo <project-name>`
- `manage.py:9`
- `<project-name>/celery.py:6`
- `<project-name>/celery.py:8`
- `<project-name>/settings/settings.py:2`
- `<project-name>/settings/settings.py:55`
- `<project-name>/settings/settings.py:73`
- `<project-name>/asgi.py:2`
- `<project-name>/asgi.py:14`
- `<project-name>/wsgi.py:2`
- `<project-name>/wsgi.py:14`
- `<project-name>/urls.py:2`
- `run.sh:5`
- `README.md:1`
```
- install dependencies
```bash
sudo apt update

sudo apt install python3-dev python3-pip python3-venv libpq-dev locales-all build-essential libev-dev libblas-dev liblapack-dev gfortran libxml2-dev libxslt1-dev -y --no-install-recommends

sudo apt install postgresql-server postgresql-server-dev-14 redis
```
- create a virtual env
```bash
python3 -m venv /path/to/venv
```
- activate venv
```bash
source /path/to/venv/bin/activate
```
You can also put this source command in `~/.bashrc`
- install python dependencies
```bash
pip install --upgrade pip
pip install wheel
pip install -r requirements.txt
```
- copy .env.sample to .env to use your specific configurations. View .env.sample file to know more
```bash
cp .env.sample .env
vim .env
```
- run migrations
```bash
python manage.py migrate
```
- create superuser
```bash
python manage.py createsuperuser
```
- run dev server
```bash
python manage.py runserver
```
you can check `http://localhost:8000/admin` in the browser and login as superuser
- run celery beat to keep scheduled tasks running
```bash
celery -A dj_foo beat -l info
```
- run celery worker to process tasks on specific queue
```bash
celery -A dj_foo worker -l INFO -Q scrapers
```





# OronWare

> **OronWare is an app for my friend Karel, where he can manage all informations
> about herbs, illnesses and recipes.**

### Technologies

- Django 1.11
- Python 3.6
- PostgreSQL
- HTML5, CSS3, JavaScript, jQuery

## Quick Start

1.  Create own virtual environment

```
$ python3 -m venv venv
```

and then activate the environment.

2.  Clone repository

```
$ git clone https://github.com/SvetlanaM/oronware.git
```

3.  Install requirements from the project:

```
$ pip3 install -r requirements.txt
```

4.  Create own database settings as a new custom database under existing
    configuration in the settings.py file.
5.  Run database migrations:

```
$ ./manage.py migrate --database="your database name in settings file"
```

6.  Create own admin super user:

```
$ ./manage.py createsuperuser --database="your database name in settings file"
```

7.  Run the app:

```
$ ./manage.py runserver
```

## Branches

Create a new branch which is following the rules: _develop_githubusername_

Do not push to the master branch.

# 403FinalProject
The final project for IS 403 Fall 2021 group 1-15. 

Authors: Kalvin Wettstein, Zachary Heaton, Stephen Williams, Spencer Jackson.

A basic CRUD app with PostgreSQL DB, python/django, and HTML/CSS. Deployed on Heroku

Steps to get set up:

1. Clone Repository
2. In Pgadmin create a "crud_movie" database
3. In Pgadmin run the sql script found in the "db" folder to create your tables and insert some data
4. In the root directory create a a file called ".env" that has the following: (see @kalvinbw or slack for the secret key)
```
DB_PASSWORD={yourPostgresPassword}
SECRET_KEY={theSecretKey}
```
5. Create a virtual env if you want and start it
6. Run the following (on windows replace psycopg2-binary with psycopg)
```
pip install django psycopg2-binary pillow requests dj-database-url django-heroku gunicorn whitenoise python-dotenv
```
7. Run this to create a login
```
python manage.py createsuperuser
```
8. Run this to start server
```
python manage.py runserver
```
9. Visit the [homepage](localhost:8000) to see the site

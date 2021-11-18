# 403FinalProject
The final project for IS 403 Fall 2021 group 1-15. 

Authors: Kalvin Wettstein, Zachary Heaton, Stephen Williams, Spencer Jackson.

A basic CRUD app with PostgreSQL DB, python/django, and HTML/CSS. Deployed on Heroku

Steps to get set up:

1. Clone Repository
2. In the root directory create a media directory with a photos directory in it
3. In Pgadmin create a "crud_movie" database
4. In the root directory create a a file called ".env" that has the following: (see @kalvinbw or slack for the secret key)
```
DB_PASSWORD={yourPostgresPassword}
SECRET_KEY={theSecretKey}
```
6. Create a virtual env if you want. Name it "venv" please
5. Run the following (on windows replace psycopg2-binary with psycopg)
```
pip install psycopg2-binary pillow python-dotenv
```
6. Run this to create the tables in the database
```
python manage.py migrate
```
7. Run this to create a login
```
python manage.py createsuperuser
```
8. Run this to start server
```
python manage.py runserver
```
9. Visit [localhost:8000/admin](localhost:8000/admin) and sign in with credentials from step 7
9. Click on the movies link and fill form to create a movie (see slack for a picture of Thor movie if you want to do that) and click save
10. Visit the [homepage](localhost:8000) to see the site

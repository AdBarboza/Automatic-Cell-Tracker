# Automatic-Cell-Tracker

Web plataform for the Automatic-Cell-Tracker

Requiriments
* Python 3.6
* Pip 18
* Virtualenv 16 (install with pip "pip install virtualenv")
* PostgreSQL 10

Set Up database
* make sure that name, user, password, host and port are correctly on automatic_cell_tracker/setting.py 

Set Up
* python -m venv ./venv
* venv/Scripts/activate
* (venv)$ pip install -r requirements.txt
* (venv)$ python manage.py makemigrations
* (venv)$ python manage.py migrate

When exit from enviroment use
* venv/Scripts/deactivate

When install requirements use
* (venv)$ pip freeze > requirements.txt

For running
-Active Enviroment : .\env\Scripts\activate
(venv)$ python manage.py runserver
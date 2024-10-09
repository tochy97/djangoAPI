# djangoAPI

## Required version
Python ^3.12

## Start new python enviroment

### Create it
`python -m venv .env`
### Start In cmd.exe
`.env\Scripts\activate.bat`
### Start In PowerShell
`.env\Scripts\Activate.ps1`
### Start Linux or MacOS
`source myvenv/bin/activate`

## To test djangoAPI - must be in djangoAPI\ directory with python enviroment started

### Install requirements
`pip install -r requirements.txt`
### Stage changes
`python manage.py makemigrations`
`python manage.py migrate`
### Create superuser
`python manage.py createsuperuser`
### Run server
`python manage.py runserver`


## To test - Docker

### Build image
`docker build -t app .`
### Run image - http://localhost:8000/
`docker run -it -p 8000:8000 app`

SHELL:=/bin/bash

python3 = /usr/local/bin/python3

run: 
	$(python3) manage.py runserver

migrate: 
	$(python3) manage.py migrate

# migrations {app}
migrations: 
	$(python3) manage.py makemigrations

# sqlmigrate {app} {versioning}
sqlmigrate: 
	$(python3) manage.py sqlmigrate

install:
	pip install django psycopg2
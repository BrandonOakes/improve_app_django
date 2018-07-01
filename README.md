# Improve a Django Project

## Python web development project

Take a messy, buggy, badly tested Python code base and improve it. Start with a Django app and identify where it's broken and inefficient. Write and run tests, check for proper validation, analyze views and analyze database calls to improve the site.


## Prerequisites


**Python** 3.5+ Installation
**Django** 2.0 Installation


## Steps:


1. First, set up a virtualenv. There are plenty
of tutorials online, so we won't cover it here.


2. Next, clone to repo to get the code


   git clone https://github.com/BrandonOakes/improve_django_app.git


3. From within the newly-cloned directory, install program requirements


    	pip install - requirements.txt


4. Next, migrate the database


    	python manage.py makemigrations


    	python manage.py migrate


5. Run server


    	python manage.py runserver

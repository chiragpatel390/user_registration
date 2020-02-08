# user_registration

# Setup

- create virtualenv with python3.7.
- install requirements with "pip install -r requirements.txt".
- create a database in postgres with name "user_registration" and with username and password "postgres".
- for database migration run command "python manage.py migrate".
- to create admin run command "python manage.py createsuperuser".
- run command "python manage.py runserver" to start the server.
- after RabbitMQ setup in local machine run command "celery -A user_registration worker -l info" to run celery worker.

# Functionality

- after register with details user will get verification link in registered email account.
- user can login after confirmation of verification link.
- user can add multiple image urls from web and after submit all urls stored with compressed urls by signals.

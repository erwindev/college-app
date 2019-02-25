# Student Microservice

This microservice deals with student information.  

# Setup

* Create virtual environment
```
$ virtualenv -p /usr/local/bin/python3 venv
$ source venv/bin/activate
```
*  Install dependencies
```
$ pip install -r requirements.txt
```
* Set environment variables - make sure to update it according your own settings
```
$ source env.dev
```
* Run database migration - this will create database tables
```
$ alembic upgrade head
```

# Run the application
* Run RabbitMQ using Docker if not already running
```
$ docker run -p 5672:5672 --hostname nameko-rabbitmq rabbitmq:3
```
* Run the microservice
```
$ sh run.sh
```

# Updating the models/table
* Run database migration - this will update or create new tables
```
$ alembic revision --autogenerate -m "add created and updated date"
$ alembic upgrade head
```




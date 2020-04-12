# TICKETING PLATFORM #

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines


## Installation
* install virtualenv using ```sudo pip install virtualenv```.
* Create a Python virtual environemnt for your project using ```virtualenv env_name```.
* activate the virtualenv using ```source bin/activate``` while insude the virtualenv directory. 
* Fork and clone this repository into the virtualenv.
* In that environment,inside your cloned project run ```pip install -r requirements.txt``` inside your project
* Create the local database with ```python manage.py migrate```

## Database Installation (Ubuntu setup)
```python
sudo apt-get update
sudo apt-get install python-pip python3-dev libpq-dev postgresql postgresql-contrib
```
## Create a Database and Database User
* Install postgres if you want to use it locally.
```python
sudo su - postgres
sudo -u postgres psql postgres
```

CREATE DATABASE ticket_db;
CREATE USER ticket WITH login';
ALTER role ticket with password 'ask_for_password';
GRANT ALL PRIVILEGES ON DATABASE ticket_db ;
```

```python
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
```

## Server Installation (Ubuntu setup)
*Install Nginx.
```
   python
sudo apt-get install nginx
```
## Project Setup (Ubuntu setup)

*Install virtualenv globally with SUDO command.
```
   python
sudo apt-get update
export LC_ALL=C
sudo -H pip install virtualenv
```
## License

MIT License

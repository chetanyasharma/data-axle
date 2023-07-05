# data-axle
 Its a system for Rental Car administration where a car can be registred for rent and then return in return of price calculated on the basis of some   factors.
 
# Table of Contents

- [Installation](#installation)
- [Building](#building)
  - [Database](#database)
- [Run APP](#runapp)
- [Testing](#testing)
  - [Unit Testing](#unittesting)
  - [Integration Testing](#integrationtesting)
- [API](#api)

# Installation
- Install virtualenv
  - pip<version> install virtualenv
    eg. pip3 install virtualenv
- Create Virtual Env
  - python<version> -m venv <virtual-environment-name>
    eg: python3 -m venv env
- Activate Env
  - source <virtual-environment-name>/bin/activate
    eg: source env/bin/activate
  - pip install -r requirements.txt
  - note :if facing error on pytest please use this command 
    export DJANGO_SETTINGS_MODULE=test.settings


# Building

## Database
  run these coomands if want to create db via postgres shell
  sudo -u postgres psql
  CREATE DATABASE myproject;
  CREATE USER myprojectuser WITH PASSWORD 'password';
  ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
  ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
  ALTER ROLE myprojectuser SET timezone TO 'UTC';
  GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
  \q

  Note :db name and password is user choice .Please use the above conf in .env file also
#create via pg admin
  - Open pgAdmin
  - Right click on Servers => Create => Server...
  - Give a name (eg.: local) and fill `localhost` in Host name under Connection tab
  - Username: postgres
  - Password: testtest
  - Save

  - Note :.env file is added for the reference puprose .


## Run APP
  - python manage.py makemigrations
  - python manage.py migrate
  - python manage.py runserver



# Testing

## Unit Testing

- To run test cases use ```pytest```.
- To run test cases of particular app/module ```pytest <app_directory>```.
- To run test case of particular function ```pytest <app_directory> -k <function-name>```.
- To run test case with falure logs  ```pytest -rF -l```.
- To run test case with passed logs  ```pytest -rP -l```.
- To run test case with all logs  ```pytest -rA -l```.

## Integration Testing

- To run test cases use ```pytest```.
- To run test cases without applying migrations use ```pytest --no-migrations```.
  Note :- Don't use ```--no-migrtaions``` flag if there are changes in migration files.
## API
- http://localhost:8000/car_rental/rental_registar (method-POST,Body={
    "customer_first_name": "hanumanji",
    "customer_last_name": "ji",
    "phone_number": "010201",
    "current_mileage_pickup": 12.23,
    "car_id":"d2018f83-ca83-448c-b151-9d87992c77db",
    "pickup_pre_book_date":"2022-02-13",
    "picked_up":true,
    "datetime_of_pickup":"2022-02-13"
  })
- http://localhost:8000/car_rental/return_car (method-PUT,Body={
    "customer_booking_number":"611349ff-13d0-429b-851a-14b17dc95a09",
    "current_mileage_return":12.2,
    "kilometer_run":12.4,
    "datetime_of_return":"2023-02-13"
}

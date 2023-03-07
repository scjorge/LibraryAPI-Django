# LibraryAPI-Django

This repository contains the web api code for the **Library** simulation.

This project contains an example of Django Rest Framework project built.

Used technologies:

- Django 4.0.4
- Django Rest Framework 3.14.0
- Postgres 15.2


## Install and configure the project

You have to create a .env variables with this values inside:
```bash
# Database 
DB_NAME=<your db name>
DB_USER=<your db user>
DB_PASSWORD=postgres<your db password>
DB_PORT=<your db port>
DB_HOST=<your db host>

# API Project
DJANGO_DEBUG_MODE=0 # use 0 for production, 1 for develop
DJANGO_SECRET_KEY=<your django token>
```

## API documentation

Use /swagger/ or /redoc/ for access the API documentation endpoint

## Usage 

The base endpoint is /api/v1/viewset/
defaul port is 8000 

there is insomnia.json to test all avalible endpoints

Exemple: 

http://127.0.0.1:8000/api/v1/viewset/category/

## Launch and debug (development mode)

You can use 'docker-compose_dev.yml' file to develop mode. This compose will use the '.env_develop' file, so you can change it as well you need it.

start with: <br>
docker-compose -f docker-compose_dev.yml -p dev up

### VSCode settings

Use devcontainer to develop, some useful extensions I used are in devcontainer.json


## Launch in production mode
Use 'docker-compose.yml' file to production mode. This compose will use the '.env' file, so you can change it as well you need it.

start with: <br>
docker-compose -f docker-compose.yml -p prod up
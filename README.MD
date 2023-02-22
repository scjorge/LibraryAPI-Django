# LibraryAPI-Django

This repository contains the web api code for the **Library** simulation.

This project contains an example of Django Rest Framework project built.

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
DJANGO_DEBUG_MODE=0 # use 0 for production 
DJANGO_SECRET_KEY='django-insecure-hn70y(uzoc_5_g2pnh@+e711i0!d+p&s+4n_3vsb^_@6y#e%sm' # you can change this value
```

## Launch and debug (development mode)

You can use 'docker-compose_dev.yml' file to develop mode. This compose will use the '.env_develop' file, so you can change it as well you need it.

### VSCode settings

Use devcontainer to develop, some useful extensions I used are in devcontainer.json


## Launch in production mode
Use 'docker-compose.yml' file to production mode. This compose will use the '.env' file, so you can change it as well you need it.
# tfeCreative API 💥

## Description

API for tfeCreative, portfolio project consisting of Django API, PostgreSQL database, and Python services.

## Build

Build the project

``` sh
$ docker-compose build
```

## Run

Run the project.

``` 
$ docker-compose up
 ```

 Once the API is running, check the status at:

> http://0.0.0.0:8000/api/status/

or login to the admin portal:

> http://0.0.0.0:8000/admin/

## Configuration

ENV files are required in root directory with keys from [settings.py](tfecreative/settings.py). Docker-compose allows you to pass in environment specific files with  extensions. For example, to build and run the project in development loading .env.dev:

``` 
$ docker-compose -f docker-compose.dev.yml up --build
```

## Technologies

* [Django](https://www.djangoproject.com/) - The Web framework for perfectionists with deadlines.
* [Django REST Framework](https://www.django-rest-framework.org/) - Awesome web-browsable Web APIs.
* [PostgreSQL](https://www.postgresql.org/) - The World's Most Advanced Open Source Relational Database
* [Docker](https://www.docker.com/) - The fastest way to containerize applications
* [Docker Compose](https://docs.docker.com/compose/) - Define and run multi-container Docker applications
* [Wait-for-it](https://github.com/vishnubob/wait-for-it) - Pure bash script that will wait on the availability of a host and TCP port.
* [Pytest](https://docs.pytest.org/en/stable/) - Helps you write better programs

# Initial setup Django + PostgreSQL
[Link di riferimento](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)  

Dati i file docker-compose.yml, .env, django/requirements.txt, django/Dockerfile
```
# The command that will be executed inside the "web" service container. It's a  Django command (django-admin startproject) used to create a new Django project.  The argument djangodockertest is the name of the project being created, and the . specifies the current directory as the location where the project files will be created.
docker-compose run web django-admin startproject djangodocker .

# Adapt django/djangodocker/settings.py and django/manage.py as needed for postgreSQL and network access
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate

docker-compose up
docker-compose down
```

Per entrare nel container possiamo usare
```
docker exec -it <container_id_or_name> bash
```
e per entrare nel database del container `psql -U username -d your_database_name`
se non trova il database cancellare la cartella relativa ai dati e ri-buildare, poi ri-usare makemigrations e migrate
# File permission
Quanto si fa push meglio usare `sudo chown -R <user>:<group> /path/to/directory` perche' le cartelle condivise ai container possono prendere owner diversi e non venire pushate

Ensure the default Django tables were created:

$ docker-compose exec db psql --username=username --dbname=databasename
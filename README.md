# Initial setup Django + PostgreSQL
[Link di riferimento](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)  

Dati i file docker-compose.yml, .env, django/requirements.txt, django/Dockerfile
```
# The command that will be executed inside the "web" service container. It's a  Django command (django-admin startproject) used to create a new Django project.  The argument djangodockertest is the name of the project being created, and the . specifies the current directory as the location where the project files will be created.
$ docker-compose run web django-admin startproject djangodocker .

# Adapt django/djangodocker/settings.py and django/manage.py as needed for postgreSQL and network access
$ docker-compose run web python manage.py makemigrations
$ docker-compose run web python manage.py migrate

$ docker-compose up
$ docker-compose down
```

Per entrare nel container possiamo usare
```
docker exec -it <container_id_or_name> bash
```
e per entrare nel database del container `psql -U username -d your_database_name`
se non trova il database cancellare la cartella relativa ai dati e ri-buildare, poi ri-usare makemigrations e migrate(avendo controllato the i valori in django/djangodocker/settings.py e .env sono presi e usati correttamente)
# File permission
Quanto si fa push meglio usare `sudo chown -R <user>:<group> /path/to/directory` perche' le cartelle condivise ai container possono prendere owner diversi(root) e non venire pushate

# Django apps
I progetti Django sono organizzati in più app, ognuna delle quali gestisce un aspetto particolare dell'applicazione web complessiva.  
(**Encapsulation of Functionality**) Ogni app Django di solito si concentra su un aspetto specifico della funzionalità dell'applicazione, come l'autenticazione degli utenti, la gestione dei contenuti o l'analisi dei dati.  
(**Loose Coupling**) Le app Django sono debolmente accoppiate, il che significa che possono interagire tra loro attraverso interfacce ben definite senza dipendenze strette. Si possono estendere o modificare la funzionalità di un'app senza influenzare altre parti dell'applicazione  

Andremo a creare le seguenti app all'interno per la gestione dei vari componenti
```
$ docker-compose run web django-admin startapp api
```
poi dobbiamo aggiungerle l'app al progetto mettendo in *settings.py*, nel parametro INSTALLED_APPS `\<name\>.apps.\<name class in apps.py\>`
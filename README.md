# Pong in Django container
Here are some general [references](https://www.atariarchives.org/bcc1/showpage.php?page=141)
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

Per aggungere un superuser con cui fare il login in /admin usiamo
```
$ docker-compose run web python manage.py createsuperuser
$ docker-compose run web python manage.py changepassword <username>
```
# File permission
Quanto si fa push meglio usare `sudo chown -R <user>:<group> /path/to/directory` perche' le cartelle condivise ai container possono prendere owner diversi(root) e non venire pushate

# Django apps
I progetti Django sono organizzati in più app, ognuna delle quali gestisce un aspetto particolare dell'applicazione web complessiva.  
(**Encapsulation of Functionality**) Ogni app Django di solito si concentra su un aspetto specifico della funzionalità dell'applicazione, come l'autenticazione degli utenti, la gestione dei contenuti o l'analisi dei dati.  
(**Loose Coupling**) Le app Django sono debolmente accoppiate, il che significa che possono interagire tra loro attraverso interfacce ben definite senza dipendenze strette. Si possono estendere o modificare la funzionalità di un'app senza influenzare altre parti dell'applicazione  

Andremo a creare le seguenti app all'interno per la gestione dei vari componenti
```
$ docker-compose run web django-admin startapp <nome app>
```
poi dobbiamo aggiungerle l'app al progetto mettendo in *settings.py*, nel parametro INSTALLED_APPS `<name>.apps.<name class in apps.py>`

# Models in app
Vogliamo avere views piccole e la maggior parte della logica in models.py. I modelli sono astrazioni/regole dentro django per tabelle nel database.
Nel momento in cui modifichiamo il database aggiungendo un nuovo modello dobbiamo fare
```
$ docker-compose run web python manage.py makemigrations
# Sara mostrato che e' stato aggiunto un modello con il nome che abbiamo dato

$ docker-compose run web python manage.py migrate
```
# Workflow
Per gestire il database mettiamo modelli in app *app_name/models.py*  
Per le risposte in base agli endpoint facciamo delle classi in app *app_name/views.py*  
Che utilizzeranno dei serializer per validare e gestire i dati in ingresso e uscita, facciamo delle classi in app *app_name/serializers.py*  
  
Nel frontend app andremo ad usare Bootstrap, quindi inizializziamo il progetto con `npm init -y` e poi installiamo `npm install bootstrap@5`. npm andra' a gestire tutti i mobuli e ci permettera anche di installarne altri.  
Babel utile per rendere il codice compatibile con piu' browsers.  
Avremo una struttura del genere:
```
project_name/
│
├── manage.py
├── static/
│   └── ...
│
├── project_name/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── app_name/
    ├── migrations/
    │   └── ...
    ├── node_modules/                   (cartella generata da npm, contiene le dipendenze)
    │   └── ...
    ├── static/
    │   └── ...
    ├── templates/
    │   └── app_name/
    │       ├── base.html
    │       └── extension_page.html     (per sfruttare la template inheritance con base.html)
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── package.json                    (file di configurazione npm)
    ├── package-lock.json               (file di blocco delle versioni npm)
    ├── tests.py
    ├── urls.py
    └── views.py
```

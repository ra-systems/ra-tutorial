Ra demo project
================

This is a demonstration project for the powerful [Ra Framework](https://github.com/ra-systems/RA).

The demo site is designed to provide examples of common features and recipes to introduce you to Ra development. Beyond the code, it will also let you explore the admin / reporting interface of the framework.

Note we do _not_ recommend using this project to start your own site - the demo is intended to be a springboard to get you started. Feel free to copy code from the demo into your own project.

### Ra Features Demonstrated in This Demo

This demo is aimed primarily at developers wanting to learn more about the internals of Ra, and assumes you'll be reading its source code. After browsing the features, pay special attention to code we've used for:

-   Creating your models
-   Creating transactions
-   Create Various reports 
-   Example of customizing the Ra Dashboard / adding report widgets  via templates.
-   Lots more

Setup with Virtualenv
---------------------
You can run the Ra demo locally 

#### Dependencies
* Python 3.4, 3.5 or 3.6
* [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
* [PostgresSql](https://www.postgresql.org/download/)
* [VirtualenvWrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) (optional)

### Installation

With [PIP](https://github.com/pypa/pip) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
installed, run:

    mkvirtualenv ra-demo
    python --version

Confirm that this is showing a compatible version of Python 3.x. If not, and you have multiple versions of Python installed on your system, you may need to specify the appropriate version when creating the virtualenv:

    deactivate
    rmvirtualenv ra-demo
    mkvirtualenv ra-demo --python=python3.6
    python --version

Now we're ready to set up the bakery demo project itself:

    cd ~/dev [or your preferred dev directory]
    git clone https://github.com/ra-systems/ra-tutorial.git
    cd ra-tutorial
    pip install -r requirements.txt
    
Next, we'll set up our local environment variables. We use [django-environ](https://github.com/joke2k/django-environ)
to help with this. It reads environment variables located in a file name `.env` next to the settings.py file of the project. The variables we need to set are the `DATABASES`.
 
Database

    Ra only support Postgresql.

    As Django's `QuerySet.distinct(*fields) <https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.distinct>`_ is supported only on Postgres.
    ``distinct(*fields)`` is used by the reporting engine.

To create a postgres database via command line :

Login / switch user to postgres

    sudo su postgres
    
Create a role
    
    psql -c "CREATE USER <DATABASE_USERNAME_HERE> WITH NOCREATEDB ENCRYPTED PASSWORD '<PASSWORD_HERE>'"

Create a Database

    psql -c "CREATE DATABASE <DATABSE_NAME_HERE> WITH OWNER <DATABASE_USERNAME_HERE>"


To set up your database and load initial data, run the following commands:
    
    cd myproject
    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py generate_data
    ./manage.py runserver

Log into the admin with the credentials ``/``.

# Next steps

Hopefully after you've experimented with the demo you'll want to create your own site. To do that you'll want to run the `ra-admin start` command in your environment of choice. You can find more information in the [getting started Ra framework docs](https://ra-framework.readthedocs.io/en/latest/usage/quickstart.html).


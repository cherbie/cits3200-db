# The Funding Opportunities Database

The development of an online searchable database providing access to research funding opportunities from Australian and global sponsors/providers. This will be accessible to UWA staff and students only as it will require a Pheme username and password. This database will be updated and maintained by the UWA Research Development Team (RDT). Staff and students will be able to access open/current opportunities that will be categorised by Faculty. They will be able to filter their search by various options such as opportunities that are targeted to early career researchers, for travel, equipment etc. Each opportunity will contain further details including funding provider, max amounts, max duration, and online links to funding opportunity details.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
How to run the project server:
 1. The _Funding Opportunities Database_ django-project folder name is _"funding_project"_
 3. The manage.py python module will be in this directory. This is the root project file. There are a number of generalised commands to adjusts the state of the project. See the [Django documentation](https://docs.djangoproject.com/en/2.2/ref/django-admin/).
 4. Use the following terminal command to start the server.

     ```
     user@user funding_project % python3 manage.py runserver
     ```


 Django considers the major folders within the __funding_project__ project as applications within the project. The below reference will describe the uses of each project app

### Funding Project App

All project settings and url routing is handled within this application. The creation of a _Django_ project by default creates this folder and is critical to the functionality of the web application.

The following directory structure exists within the application.
```
user@user funding_project % tree .
├── __init__.py
├── __pycache__
│   ├── __init__.cpython-37.pyc
│   ├── settings.cpython-37.pyc
│   ├── urls.cpython-37.pyc
│   └── wsgi.cpython-37.pyc
├── settings.py
├── urls.py
└── wsgi.py
```

Both the *\_\_init.py\_\_* and *\_\_pycache\_\_* facilitate the functionality of the web server and are created by the Django framework. As a general rule, all additional folders created needed to have an empty *\_\_init.py\_\_* file created in order to for the system to recognise all folders and files contained.

The file *\_\_settings.py\_\_* contains all funding database opportunity web server settings including all python module dependencies and configuration environments.

The file *\_\_urls.py\_\_* is the starting point for any web server routing of client requests.

The file *\_\_wsgi.py\_\_* is a file critical to the functionality of the Django framework manager.


### Users App

The *users* django application is responsible for the management, storage and rendering of the web page interface for users with administrator privileges. The following files exist within this directory:

```
user@user funding_project % tree users
users
├── __init__.py
├── __pycache__
│   ├── __init__.cpython-37.pyc
│   ├── admin.cpython-37.pyc
│   ├── apps.cpython-37.pyc
│   ├── forms.cpython-37.pyc
│   ├── models.cpython-37.pyc
│   ├── tokens.cpython-37.pyc
│   └── views.cpython-37.pyc
├── admin.py
├── apps.py
├── forms.py
├── migrations
│   ├── 0001_initial.py
│   ├── __init__.py
│   └── __pycache__
│       ├── 0001_initial.cpython-37.pyc
│       ├── 0002_remove_profile_user.cpython-37.pyc
│       └── __init__.cpython-37.pyc
├── models.py
├── static
│   └── users
│       └── images
│           ├── coolimg.png
│           ├── cover_background.png
│           ├── ezone.png
│           ├── lolwedonthavethis.png
│           ├── uwa_brand.png
│           └── whateverthisis.png
├── templates
│   └── users
│       ├── auth_complete.html
│       ├── auth_confirm.html
│       ├── auth_error.html
│       ├── auth_invalid.html
│       ├── login.html
│       ├── logout.html
│       ├── password_reset.html
│       ├── password_reset_confirm.html
│       ├── password_reset_done.html
│       └── register.html
├── tokens.py
└── views.py
```

The *views.py* file manages the routing of users requests and is effectively the starting point of the machines execution pattern within the app.

*apps.py* is a critical file linking the base project app "*funding_project*" to the users app.

The web application has made use of the default Django user model and seeks to only add upon this functionality by specifying further metadata in the *models.py*, *forms.py* and *tokens.py* files.

The web applications assets related to user management can be found in the folders titled */static* and */templates*.

### FODB App

The Funding Opportunities Database (FODB) application contains all the functionality relating to opportunity listing creation and management. The following directory structure exists:

```
user@user funding_project % tree fodb
fodb
├── __init__.py
├── __pycache__
│   ├── __init__.cpython-37.pyc
│   ├── admin.cpython-37.pyc
│   ├── apps.cpython-37.pyc
│   ├── filters.cpython-37.pyc
│   ├── forms.cpython-37.pyc
│   ├── modelForm.cpython-37.pyc
│   ├── models.cpython-37.pyc
│   ├── pipeline.cpython-37.pyc
│   ├── urls.cpython-37.pyc
│   └── views.cpython-37.pyc
├── admin.py
├── apps.py
├── filters.py
├── forms.py
├── middleware.py
├── migrations
│   ├── 0001_initial.py
│   ├── __init__.py
│   └── __pycache__
│       ├── 0001_initial.cpython-37.pyc
│       └── __init__.cpython-37.pyc
├── models.py
├── pipeline.py
├── static
│   └── fodb
│       ├── css
│       │   ├── filter.css
│       │   ├── landing-page.css
│       │   ├── landing-page.min.css
│       │   ├── research-content.css
│       │   ├── tables.css
│       │   ├── welcome.css
│       │   └── wiki.css
│       ├── images
│       │   ├── Go8Member-blank.png
│       │   ├── ezone.jpg
│       │   ├── favicon.png
│       │   ├── footer-go8.png
│       │   ├── searchbackground.png
│       │   ├── undergrad.jpeg
│       │   └── uwa_brand.png
│       └── main.css
├── templates
│   ├── acc_active_email.html
│   └── fodb
│       ├── base.html
│       ├── db-update.html
│       ├── details.html
│       ├── error.html
│       ├── funding_opportunity_detail.html
│       ├── home-filter.html
│       ├── home.html
│       ├── tables.html
│       └── welcome.html
├── urls.py
└── views.py
```

Once again the *apps.py* allows the system to recognise the application as part of the funding opportunity project and the *views.py* file manages the routing of user requests.

The *admin.py* source file alters the appearance of predefined Django dynamic web pages seen in the administrator's user interface.

The *filters.py* and *forms.py* source files support the search bar and filtering options provided in the home page. In particular *forms.py* handles the filtering *GET* requests of users and *filters.py* actions on the users requests.

The database related to the funding opportunities web application is interacted with and managed using the Django Object Relation Model (ORM). The *models.py* source file defines all additional database tables created on top of standard user tables provided by Django. A log of changes to the database is kept in the */migrations* folder. When changes are made to the *models.py* folder, these changes need to be 'migrated' / actioned by the Django ORM.

The following command can be used to prepare the migrations needing to be made. The text printed to the standard output stream can be used to verify the changes pending are correct.

```
user@user funding_project % python3 manage.py makemigrations
```

Once the pending changes have been reviewed the changes can be implemented within the database using the following command:

```
user@user funding_project % python3 manage.py migrate
```

At this point the Django ORM will have actioned all changes in the database.

The *pipeline.py* source file is responsible for redirecting users who have not entered the appropriate authentication credentials.

The static assets of the web application including all images and jinja templates are referenced from within the */static* folder and the */templates* folder. The names of these folders should not be altered unless the appropriate Django setting is altered in the */funding_project/settings.py* file. By default Django seeks for static files and template files in directories with these titles.

## Dependencies

All funding opportunity web server dependencies can be found in the _requirements.txt_ file. These project dependencies can be simply installed using the python package manager _'**pip**'_.

The list of Django server dependencies can be found within the *requirements.txt* file as shown below:

```
user@user funding_project % cat requirements.txt
backports.csv==1.0.7
certifi==2019.9.11
chardet==3.0.4
class-registry==2.1.2
defusedxml==0.6.0
diff-match-patch==20181111
Django==2.2.4
django-appconf==1.0.3
django-compressor==2.3
django-crispy-forms==1.7.2
-e git://github.com/django-extensions/django-extensions.git@afa8f0c242126197ca0e1eaf9d1c226e615a013b#egg=django_extensions
django-filter==2.2.0
paramiko==2.6.0
-e git+https://github.com/django-import-export/django-import-export.git@4589d4c40bd5b8ecb1b34e69e5f5e6632217de2c#egg=django_import_export
django-libsass==0.7
django-sb-admin==0.3.7
django-suit==0.3a3
djangorestframework==3.7.7
et-xmlfile==1.0.1
filters==1.3.2
idna==2.8
jdcal==1.4.1
libsass==0.19.2
oauthlib==3.1.0
odfpy==1.4.0
openpyxl==3.0.0
Pillow==6.1.0
PyJWT==1.7.1
python-dateutil==2.8.0
python3-openid==3.1.0
pytz==2019.2
PyYAML==5.1.2
rcssmin==1.0.6
regex==2019.8.19
requests==2.22.0
requests-oauthlib==1.2.0
rjsmin==1.1.0
six==1.12.0
social-auth-app-django==3.1.0
social-auth-core==3.2.0
sqlparse==0.3.0
tablib==0.13.0
urllib3==1.25.6
virtualenv==16.7.4
xlrd==1.2.0
xlwt==1.3.0
```

The following command will install all required packages in your python virtual environment.

```
user@user funding_project % pip install -r requirements.txt
```

## Built With

* [django](https://www.djangoproject.com/) - The web framework used
* [jinja](https://jinja.palletsprojects.com/en/2.10.x/) - Templating engine
* [pip](https://pip.pypa.io/en/stable/) - Python package installer
* [bootstrap](https://getbootstrap.com/) - Web page styling
* [Google auth](https://developers.google.com/identity/protocols/OAuth2WebServer) - Authentication

## Authors

- [**Clayton Herbst**](https://github.com/clayton-herbst)
- [**Quoc Viet Nguyen**](https://github.com/I8m90d)
- [**Aaymen Imran Khan**](https://github.com/Amaze-Aims)
- [**Nathan Owen Santoso**](https://github.com/Etrenix)
- [**Yanhang Zhang**](https://github.com/okokok-ok)

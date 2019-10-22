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

###### Funding Project App

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


###### Users App




###### FODB App




### Dependencies

All funding opportunity web server dependencies can be found in the _requirements.txt_ file. These project dependencies can be simply installed using the python package manager '**pip**'.

The list of Django server dependencies can be found by running the following command

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
-e git+https://github.com/django-import-export/django-import-export.git@4589d4c40bd5b8ecb1b34e69e5f5e6632217de2c#egg=django_import_export
django-libsass==0.7
django-sb-admin==0.3.7
django-suit==2.0a1
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

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [pip](https://pip.pypa.io/en/stable/) - Python package installer

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

- **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)
- [**Quoc Viet Nguyen**]()
- [**Clayton Herbst**](https://github.com/clayton-herbst)
- [**Aaymen Imran Khan**]()
- [**Nathan Owen Santoso**]()
- [**Yanhang Zhang**]()

See also the list of [contributors](https://github.com/clayton-herbst/cits3200-db/contributors) who participated in this project.

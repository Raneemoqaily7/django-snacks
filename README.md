# Introduction To Django 
- What is django ?

 Django is a free and open source web application framework written in Python. A framework is nothing more than a collection of modules that make development easier. They are grouped together, and allow you to create applications or websites from an existing source, instead of from scratch.

 Django helps us to build a website with  **LESS TIME** and **LESS CODE**

 - Compainies Using Django 
 1.  YouTube 
 2. Instagram
 3. Spotify
 4. DropBox

 -  Django is a **BATTRIES INCLUDED FRAMEWORK** which means it comes with alot of features out of the box so you dont need to code them from scratch .

 - Django Fatures
 1. The adminn site 
 2. Object-relational mapper (ORM) : A bstract the database,so we can process data without wrotting a lot of SQL code 
 3. Authentication package for identifying user .
 4. Caching Data 

 - Django has a huge community 

# Fundamntal of web development 
- Django is a framework for building web applications 

when the user whants to visit awebsite xxxxxxx.com , this address also calles a url (Uniform Resource Locator ) , the resource can be ( page , image , video , pdf)   , user wrie the web address and hit enter , at this moment browser sent a Request to the webserver  , the webserver takes this request , processs it and return a response back to the client , this data exchange is defined by a protocol calles HTTP (Hypertext Transfer Protocol) , its defined how client and server can communicate .

- Django REST Framework is a wrapper over default Django Framework, basically used to create APIs of various kinds. There are three stages before creating a API through REST framework, Converting a Model’s data to JSON/XML format (Serialization), Rendering this data to the view, Creating a URL for mapping to the viewset.

# Setting up the development environment 
1. Install Python with last version (https://www.python.org/downloads/)

2. Install Code Editor (VisualStudio Code  ,.. )


# Your First Django Project 

- In your terminal create your virtual environmt `poetry new project`
- `poetry install` to install dependices
- `poetry shell` to activate the virtual environment 
- `poetry add django`
- `django-admin startproject django-project` to creat your django project 
- cd into your project 
- `python manage.py migrate`  to prepare your database  
- `python manage.py createsuperuser` and fill the your user info 
- `python manage.py runserver` to run the server 
- `python manage.py startapp django-app` to create yor app ,dont forget to add your app to setting.py file 
- prepear your database table in models.py 
- `python manage.py makemigrations`  to prepare the changes that will happen in database 
-`python manage.py migrate` tp apply changes that happend in the database . 
- register the models in thee admin app in admin.py  


# Django Delights

This is a project developed in Python to build an API that will help keep track of how much food they have throughout the day in a restaurant.

## Requirements

- Python 3.8 (or higher)
- MariaDB 10.4 (or higher)
- Django 4.2 (or higher)
- mysqlclient package for Python
- python-dotenv package for Python

## How to run

1. Enter the [repository URL](https://github.com/juanmacivico87/djangodelights). Surely, if you are reading this, you are already there.
2. Open a terminal and run the command ```git clone https://github.com/juanmacivico87/djangodelights.git```.
3. Enter the directory you have just cloned with the command ```cd djangodelights```.
4. Create an .env file with the following information:

```
DB_NAME=YourDBName
DB_USER=YourDBUser
DB_PASSWORD=YourDBPassword
DB_HOST=YourDBHost
DB_PORT=YourDBPort
```
5. Run ```python3 manage.py migrate``` to create the tables of the database.
6. Run ```python3 manage.py createsuperuser``` command to create an admin user and follow the instructions on the console.
7. Run ```python3 manage.py runserver``` command to start the project.
8. Go to http://127.0.0.1:8000 from your favorite browser (if the port from which your application was launched is different, substitute that value in the URL).

## Informative note

This is an Open Source project, so feel free to download, use and extend it as you wish.

Did you like it? If so, add a star to the repository to encourage me to continue doing projects like this and help me to give it more visibility.

## Changelog

- 1.0.0
    - Initial version of the project
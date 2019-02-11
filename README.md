# Attendance-List

This is a simple terminal-based app for checking the attendance. 
The project was created for presentation on Pylight: Python-oriented meetup for begginers.
The main goal is to show how to establish a connection with PostgreSQL database using Psycopg2. 

## What is needed
1. Python3.7 (if not you will have to create a virtualenv using desired python version)
2. Pipenv
3. PostgreSQL + new clean database

## How to run 
1. Clone this repository
2. Navigate in terminal to directory containing Pipfile
3. Run 
```
gedit .env
```
  and edit your database connection variables. If you're using other editor than Gedit then type name of this editor instead.
 
4. Run 
```
pipenv install
```
  to install dependencies (Psycopg2 in this case).

5. Run 
```
pipenv shell
```
  to enter virtual enviroment. At this point you should see (Attendance-List) prefix preceding your directory path.

6. Run
```
python logic.py
```
to run the app. You should see a welcome message and menu. 
Type 'd' to create a required database structure. This button is also used for resetting your database. 
**Keep in mind that it will drop existing table and create a new one.**

7. Keep exploring the source code. On branch 'with-decorator' you will find different implementation od the database connection using decorator. 
This implementation creates a new connection, executes a query and closes the connection every time you run the desired function. There is also
a 'bad-example' which contains a function that uses simple string interpolation for passing arguments to SQL query. This is an anti-pattern 
and makes your app vulnerable to SQL injection.

## Worth watching/checking:

Pycon talk from the creator of Pipenv: [link](https://www.youtube.com/watch?v=GBQAKldqgZs)

Pipenv tutorial by Corey Schafer: [link](https://www.youtube.com/watch?v=zDYL22QNiWk&t=982s)

PostreSQL installation & configuration guide on Ubuntu: [link](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)

Psycopg2 docs: [link](http://initd.org/psycopg/docs/usage.html)

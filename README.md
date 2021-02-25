# CRUD Project

This project implements a simple CRUD REST API using flask as web server and SQLAlchemy and Marshmallow as ORM and serializer, repectively. 

## Requirements 

- ODBC Driver 17 for SQL Server installed in your machine

## Setup
1. Create a python virtualenv, and with its activated install the requirements from requirements.txt file:
    
    ```console
        pip install -r requirements.txt
    ```

2. Then set your environment variables in .env configuration file:
    
    ```.env
        server=<your_server_name>
        database=<your_database_name>
        username=<admin>
        password=<pwd>
        driver=<your_driver>
    ```

    obs: This project was implemented using SQL Server as db.


## How to run

Just run api.py file, and your web server is running :two_hearts:

## References

- [SQLAlchemy Oficial documentation](https://docs.sqlalchemy.org/en/14/)
- [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/)
- [Marshmallow documentation](https://marshmallow.readthedocs.io/)
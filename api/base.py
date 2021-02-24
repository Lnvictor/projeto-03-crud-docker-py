from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import urllib

server = config("server")
database = config("database")
username = config("username")
password = config("password")
driver = config("driver")


conn = (
    "DRIVER="
    + driver
    + ";SERVER="
    + server
    + ";PORT=1433;DATABASE="
    + database
    + ";UID="
    + username
    + ";PWD="
    + password
)
params = urllib.parse.quote_plus(conn)
conn_str = "mssql+pyodbc:///?autocommit=true&odbc_connect={}".format(params)
Base = declarative_base()
engine = create_engine(conn_str, echo=False)
Session = sessionmaker(bind=engine)
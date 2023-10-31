from sqlalchemy import create_engine, text
import os
import mysql.connector


db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string, 
  echo=True)

# PyMySQL




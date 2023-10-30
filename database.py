from sqlalchemy import create_engine, text
import os
import mysql.connector


db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string, 
  echo=True)

# PyMySQL
with engine.connect() as conn:
  result = conn.execute(text("SELECT * FROM case22.Vare"))
  print(result.fetchall())
    



from sqlalchemy import create_engine, text

db_connection_string = "mysql+mysqlconnector://kc151xibbj1yblvw8953:pscale_pw_6UvqeRN9wyOtjXX3lELZXGZzUCikKUmFcavYvSssZus@aws.connect.psdb.cloud/case22"

engine = create_engine(
  db_connection_string, 
  echo=True)

# PyMySQL
def load_vare_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM case22.Vare"))
    print(result.fetchall())
    vare = []
    for row in result.all():
      vare.append(dict(row))
    return vare



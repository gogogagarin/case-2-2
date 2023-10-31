from flask import Flask, render_template, url_for
from database import db_connection_string

app = Flask(__name__)


@app.route("/")
def index():
  return render_template('home.html')

@app.route('/vare')
def vare():
  cur = mysql.cursor(dictionary=True)
  cur.execute("SELECT * FROM Vare WHERE Varetype = 'Cykel'")
  data = cur.fetchall()
  cur.close()
  return render_template('var.html', cykler=data)
  


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  
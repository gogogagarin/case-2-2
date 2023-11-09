from flask import Flask, render_template, url_for
import mysql.connector
import database

app = Flask(__name__)


@app.route("/")
def index():
  return render_template('home.html')


@app.route("/vare")
def vare():
  data = database.execute_query('SELECT * FROM gruppe3_nemlig.Vare')
  return render_template('vare.html', data=data)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

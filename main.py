from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route("/")
def hello_jovian():
  return render_template('home.html')

@app.route("/vare")
def vare():
  return render_template('vare.html')
  
@app.route("/ordre")
def ordre():
  return render_template('ordre.html')
  
@app.route("/faktura")
def faktura():
  return render_template('faktura.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  
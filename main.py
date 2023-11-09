# Import the necessary modules
from flask import Flask, render_template, url_for
import database

# Create a new Flask web server
app = Flask(__name__)

# Define the route for the URL '/'
@app.route("/")
def index():
  # When the route is accessed, render the 'home.html' template
  return render_template('home.html')

# Define the route for the URL '/vare'
@app.route("/vare")
def vare():
  # Execute the SQL query 'SELECT * FROM gruppe3_nemlig.Vare' and store the result in 'data'
  data = database.execute_query('SELECT * FROM gruppe3_nemlig.Vare')
  # Print the data to the console
  print(data)
  # When the route is accessed, render the 'vare.html' template and pass the 'data' variable to it
  return render_template('vare.html', data=data)

# If this script is run directly (instead of being imported), start the web server
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

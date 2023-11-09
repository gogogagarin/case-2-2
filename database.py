# Import the necessary modules
import mysql.connector
import os

# Define a function to execute a query
def execute_query(text):
  # Connect to the database
  db = mysql.connector.connect(host='gateway01.us-west-2.prod.aws.tidbcloud.com',
                               port='4000',
                               user='3aHUY11sUPdpx1P.root',
                               password=os.environ['PW'],
                               database='gruppe3_nemlig')
  # Create a cursor
  cur = db.cursor()
  # Execute the query
  cur.execute(text)
  # Fetch all the results
  data = cur.fetchall()
  # Close the cursor
  cur.close()
  # Return the data
  return data
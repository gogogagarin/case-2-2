import mysql.connector
import os


def execute_query(text):
  db = mysql.connector.connect(host='gateway01.us-west-2.prod.aws.tidbcloud.com',
                               port='4000',
                               user='3aHUY11sUPdpx1P.root',
                               password=os.environ['PW'],
                               database='gruppe3_nemlig')
  cur = db.cursor()
  cur.execute(text)
  data = cur.fetchall()
  cur.close()
  return data

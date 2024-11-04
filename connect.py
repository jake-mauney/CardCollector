from dotenv import load_dotenv
import os
#import csv <-- needed if I want to use CSV to import
import mysql.connector

#load env vars
load_dotenv()

#connect to DB
cnx = mysql.connector.connect(user = os.getenv('database_user'), password = os.getenv('pwd'), host=os.getenv('host'))
cursor = cnx.cursor()


#verifieds that we are connected to DB
if cnx and cnx.is_connected():
    result = cursor.execute("SELECT * FROM CardCollector.Card;")
    rows = cursor.fetchall()
    for rows in rows:
        print (rows)
    cnx.close()
else:
    print("could not connect")
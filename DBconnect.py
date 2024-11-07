from dotenv import load_dotenv
import os
#import csv <-- needed if I want to use CSV to import
import mysql.connector

# Load env vars
load_dotenv()

class DBConnect():
    def __init__(self):
        self.cnx = mysql.connector.connect(user = os.getenv('database_user'), password = os.getenv('pwd'), host=os.getenv('host'))

    def query(self, sql):
        cursor = self.cnx.cursor(dictionary=True)
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows
    
    def cursor(self):
        return self.cnx.cursor()
    
    def commit(self):
        return self.cnx.commit()
        


#verifieds that we are connected to DB
#if cnx and cnx.is_connected():
#    result = cursor.execute("SELECT * FROM CardCollector.Card;")
#    rows = cursor.fetchall()
#    for rows in rows:
#        print (rows)
#    cnx.close()
#else:
#    print("cannot connect")
from DBconnect import *

class cardview():
    #create connection to DB
    Database = DBConnect()

    #does the SQL query and grabs the records
    result = Database.query("SELECT Name,SetCode,SetNum FROM CardCollector.Card;")
    resultdic = {}

    #Go through the results and print them out
    rows = result.fetchall()
    for rows in rows:
        print (rows)

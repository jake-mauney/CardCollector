from DBconnect import *

#create connection to DB
Database = DBConnect()

#does the SQL query and grabs the records
result = Database.query("SELECT * FROM CardCollector.Card;")

#Go through the results and print them out
rows = result.fetchall()
for rows in rows:
    print (rows)

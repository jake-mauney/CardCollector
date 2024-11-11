import tkinter as tk
import DBconnect
import requests
from datetime import datetime

def updateprice(setcode, setnum, idCard, foil):
    if foil == 'false':
        c = DBconnect.DBConnect()
        cursor = c.cursor()
        reqeust_url = "https://api.scryfall.com/cards/"+setcode.lower()+"/"+setnum
        response = requests.get(reqeust_url)
        data = response.json()
        values = [data['prices']['usd'],datetime.today().strftime('%Y-%m-%d'),idCard]
        cursor.execute("INSERT INTO CardCollector.Price (price,date,RelCard_Id) VALUES (%s, %s, %s)",(values))
        c.commit()
        cursor.execute("UPDATE CardCollector.Card INNER JOIN CardCollector.Price ON CardCollector.Price.RelCard_Id = CardCollector.Card.idCards SET CardCollector.Card.Price = CardCollector.Price.price WHERE CardCollector.Price.idPrice = %s",(cursor.lastrowid,))
        c.commit()
        
        
    else:
        reqeust_url = "https://api.scryfall.com/cards/"+setcode+"/"+setnum
        response = requests.get(reqeust_url)
        data = response.json()
        print(data['prices']['usd_foil'])
        print("You did it wrong")

if __name__ == "__main__":
    updateprice()

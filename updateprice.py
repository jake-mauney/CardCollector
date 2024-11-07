import tkinter as tk
import DBconnect
import requests
from datetime import datetime

def updateprice(setcode, setnum, idCard, foil):
    if foil == 'false':
        reqeust_url = "https://api.scryfall.com/cards/"+setcode.lower()+"/"+setnum
        response = requests.get(reqeust_url)
        data = response.json()
        print(data['prices']['usd'])
        
        c = DBconnect.DBConnect()
        cursor = c.cursor()
        values = [data['prices']['usd'],datetime.today().strftime('%Y-%m-%d'),idCard]
        cursor.execute("INSERT INTO Price (price,date,RelCard_Id) VALUES (%s, %s, %s)",(values))
        c.commit
    else:
        reqeust_url = "https://api.scryfall.com/cards/"+setcode+"/"+setnum
        response = requests.get(reqeust_url)
        data = response.json()
        print(data['prices']['usd_foil'])

if __name__ == "__main__":
    updateprice()

import tkinter as tk
import DBconnect
from DeckViewUI import openDeck

def deckCollection():
    connect = DBconnect.DBConnect()

    listOfDecks = connect.query("SELECT Name, idDeck FROM CardCollector.Deck;")

    root = tk.Tk()
    root.title("Your Decks")
    for i in range(len(listOfDecks)):
        newButton = tk.Button(root, text=str(listOfDecks[i]["Name"]), command=lambda i=i : openDeck(listOfDecks[i]["idDeck"])) #i=i freezes the i value for the button
        newButton.grid(row=i,column=1)
    root.mainloop()

#This is needed in order for the button to call the window. IDK why
if __name__ == "__main__":
    deckCollection()
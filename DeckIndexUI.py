import tkinter as tk
import DBconnect

def deckCollection():
    connect = DBconnect.DBConnect()

    listOfDecks = connect.query("SELECT Name FROM CardCollector.Deck;")
    print(len(listOfDecks))

    root = tk.Tk()
    root.title("Your Decks")
    for i in range(len(listOfDecks)):
        newButton = tk.Button(root, text=str(listOfDecks[i]["Name"]))
        newButton.grid(row=i,column=1)
    root.mainloop()

#This is needed in order for the button to call the window. IDK why
if __name__ == "__main__":
    deckCollection()
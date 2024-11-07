import tkinter as tk
import DBconnect

def openDeck(deckId):

    root = tk.Tk()
    root.title("Deck List")

    #Grab the deck list entries from DB
    c = DBconnect.DBConnect()
    result = c.query("SELECT Card_Id, Location FROM CardCollector.DeckCard WHERE Deck_Id = %s", (deckId,))
    print(deckId)

    #sets hight of crad based on how many results
    height = len(result)
    #manually set the number of fields you are returning
    width = 4
    colbheader = tk.Label(root, text="Card Id")
    #actually puts the headers in the UI
    colbheader.grid(row=1, column=1)
    #sets the first row of data to be under the headers
    rowcounter = 2
    #actually builds each "Data cell" 
    for i in range(height): #Rows
        for j in range(width): #Columns
            b = tk.Label(root, text=result[i]["Card_Id"])
            #b = tk.Label(root, text="Text in Cell" + str(i) + str(j) )
            b.grid(row=rowcounter, column=1)
            #print(rowcounter)
        rowcounter += 1

    root.mainloop()
    

#This is needed in order for the button to call the window. IDK why
if __name__ == "__main__":
    openDeck()

import tkinter as tk
from CardCollectionUI import openCollection
from importcsv import fileimport
from DeckIndex import deckCollection


#Creates Window
root = tk.Tk()
root.title("Card Collector Home")
#Header stuff
HeaderTxt = 'Welcome to the Card Collector backend!'
headerLabel = tk.Label(text=HeaderTxt)

#Buttons
CardViewButton = tk.Button(root, text="View Collection", command=openCollection)
DeckViewButton = tk.Button(root, text="Decks" ,command=deckCollection)
PriceUpdateButton = tk.Button(root, text="Price Update")

#Top Menu
menubar = tk.Menu(root)
#Creates "File" var for the menu
filemenu = tk.Menu(menubar, tearoff=0)
#Creates the "Import Cards option"
filemenu.add_command(label="Import Cards", command=fileimport)
filemenu.add_command(label="Quit" ,command=root.quit)
#Sets the file option in the menu
menubar.add_cascade(label="File", menu=filemenu)
#puts the menu on the screen
root.config(menu=menubar)


#Pack header
headerLabel.pack()

#Pack buttons
CardViewButton.pack()
DeckViewButton.pack()
PriceUpdateButton.pack()

#wait on something
root.mainloop()


import tkinter as tk
root = tk.Tk()
root.title("Card Collector")
#Header stuff
HeaderTxt = 'Welcome to the Card Collector backend!'
headerLabel = tk.Label(text=HeaderTxt)

#Buttons
CardViewButton = tk.Button(root, text="View Collection")
DeckViewButton = tk.Button(root, text="Decks")
PriceUpdateButton = tk.Button(root, text="Price Update")

#Top Menu
menubar = tk.Menu(root)
#Creates "File" var for the menu
filemenu = tk.Menu(menubar, tearoff=0)
#Creates the "Import Cards option"
filemenu.add_command(label="Import Cards")
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


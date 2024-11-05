import tkinter as tk
root = tk.Tk()
root.title("Card Collector")
#Header stuff
HeaderTxt = 'Welcome to the Card Collector backend!'
headerLabel = tk.Label(text=HeaderTxt)

#Buttons
CardViewButton = tk.Button(root, text="View Collection")


headerLabel.pack()
CardViewButton.pack()
root.mainloop()


import tkinter as tk

def openCollection():


    #Main window
    root = tk.Tk()
    root.title("Card Collection")


    #Header Text
    #HeaderTxt = 'View your collection!'
    #headerLabel = tk.Label(text=HeaderTxt)


    #Table
    height = 5
    width = 5
    for i in range(height): #Rows
        for j in range(width): #Columns
            b = tk.Label(root, text="Text in Cell" + str(i) + str(j) )
            b.grid(row=i, column=j)




    root.mainloop()


#This is needed in order for the button to call the window. IDK why
if __name__ == "__main__":
    openCollection()
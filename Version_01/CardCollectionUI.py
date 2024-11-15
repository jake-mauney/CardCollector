import tkinter as tk
import DBconnect
from updateprice import updateprice
def openCollection():


    #Main window
    root = tk.Tk()
    root.title("Collection of Cards")


    #Header Text
    #HeaderTxt = 'View your collection!'
    #headerLabel = tk.Label(text=HeaderTxt)

    #Connect to DB
    c = DBconnect.DBConnect()
    result = c.query("SELECT Name, SetCode, SetNum, Price, Foil, idCards FROM CardCollector.Card;")
    #print(result)
    #print("The first card is " + result[0]["Name"])
    
    
    #Table

    #height is based on the length of what sql returns
    height = len(result)
    #manually set the number of fields you are returning
    width = 4
    #sets the column headers
    colbheader = tk.Label(root, text="Name")
    colcheader = tk.Label(root, text="Set Code")
    coldheader = tk.Label(root, text="Set Number")
    coleheader = tk.Label(root, text="Price")
    colfheader = tk.Label(root, text="Update Price")
    #actually puts the headers in the UI
    colbheader.grid(row=1, column=1)
    colcheader.grid(row=1, column=2)
    coldheader.grid(row=1, column=3)
    coleheader.grid(row=1, column=4)
    colfheader.grid(row=1, column=5)

    #sets the first row of data to be under the headers
    rowcounter = 2
    #actually builds each "Data cell" 
    for i in range(height): #Rows
        for j in range(width): #Columns
            b = tk.Label(root, text=result[i]["Name"])
            c = tk.Label(root, text=result[i]["SetCode"])
            d = tk.Label(root, text=result[i]["SetNum"])
            e = tk.Label(root, text=result[i]["Price"])
            f = tk.Button(root, text="Update Price" , command=lambda i = i : updateprice(result[i]["SetCode"], result[i]["SetNum"], result[i]["idCards"],result[i]["Foil"]))
            #b = tk.Label(root, text="Text in Cell" + str(i) + str(j) )
            b.grid(row=rowcounter, column=1)
            c.grid(row=rowcounter, column=2)
            d.grid(row=rowcounter, column=3)
            e.grid(row=rowcounter, column=4)
            f.grid(row=rowcounter, column=5)
            #print(rowcounter)
        rowcounter += 1





    root.mainloop()


#This is needed in order for the button to call the window. IDK why
if __name__ == "__main__":
    openCollection()
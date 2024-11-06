import tkinter as tk
import DBconnect
def openCollection():


    #Main window
    root = tk.Tk()
    root.title("Card Collection")


    #Header Text
    #HeaderTxt = 'View your collection!'
    #headerLabel = tk.Label(text=HeaderTxt)

    #Connect to DB
    c = DBconnect.DBConnect()
    result = c.query("SELECT Name, SetCode, SetNum, Price FROM CardCollector.Card;")
    print(result)
    #print("The first card is " + result[0]["Name"])
    
    
    #Table
    height = len(result)
    width = 4
    colbheader = tk.Label(root, text="Name")
    colcheader = tk.Label(root, text="Set Code")
    coldheader = tk.Label(root, text="Set Number")
    coleheader = tk.Label(root, text="Price")
    colbheader.grid(row=1, column=1)
    colcheader.grid(row=1, column=2)
    coldheader.grid(row=1, column=3)
    coleheader.grid(row=1, column=4)
    rowcounter = 2
    for i in range(height): #Rows
        for j in range(width): #Columns
            b = tk.Label(root, text=result[0]["Name"])
            c = tk.Label(root, text=result[0]["SetCode"])
            d = tk.Label(root, text=result[0]["SetNum"])
            e = tk.Label(root, text=result[0]["Price"])
            #b = tk.Label(root, text="Text in Cell" + str(i) + str(j) )
            b.grid(row=rowcounter, column=1)
            c.grid(row=rowcounter, column=2)
            d.grid(row=rowcounter, column=3)
            e.grid(row=rowcounter, column=4)
            print(rowcounter)
        rowcounter += 1





    root.mainloop()


#This is needed in order for the button to call the window. IDK why
if __name__ == "__main__":
    openCollection()
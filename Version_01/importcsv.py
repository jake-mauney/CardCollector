import csv
from tkinter import Tk
import tkinter as tk
from tkinter.filedialog import askopenfilename
import DBconnect
def fileimport():

    #asks for the file to be imported
    file_path = askopenfilename()

    #calls the dbconnect class and creates a cursor
    c = DBconnect.DBConnect()
    cursor = c.cursor()

    #reads the csv file, goes through each row and creates a call for each individual row. This is not scaleable. 
    try:
        with open(file_path, mode='r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                cursor.execute("INSERT INTO `CardCollector`.`Card` (Name,SetCode,SetNum) VALUES (%s,%s,%s)",row)
            c.commit()
    except:
        print("Something went wrong I guess")

if __name__ == "__main__":
    fileimport()

        


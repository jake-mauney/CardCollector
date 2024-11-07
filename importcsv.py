import csv
from tkinter import Tk
import tkinter as tk
from tkinter.filedialog import askopenfilename
import DBconnect



file_path = askopenfilename()

c = DBconnect.DBConnect()
cursor = c.cursor()


try:
    with open(file_path, mode='r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            cursor.execute("INSERT INTO `CardCollector`.`Card` (Name,SetCode,SetNum) VALUES (%s,%s,%s)",row)
        c.commit()
except:
    print("Something went wrong I guess")


        


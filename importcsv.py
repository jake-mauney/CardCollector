import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import DBconnect



file_path = askopenfilename()

c = DBconnect.DBConnect()
cursor = c.cursor()

with open(file_path, mode='r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        cursor.execute("INSERT INTO `CardCollector`.`Card` (Name,SetCode,SetNum) VALUES (%s,%s,%s)",row)
c.commit()

        


from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import sqlite3
import os                      
import time                     



class CCalculator:
    def __init__(self, root):
        self.root=root
        self.root.geometry("490x460+200+100")
        self.root.title("Calculator")
        #self.root.state('zoomed')                    
        self.root.configure(bg='grey') 
        #self.root.overrideredirect(1) #remove close and maximise icons 

        self.con=sqlite3.connect(database=r'CAMP.db')
        self.cur=self.con.cursor()


        self.Incperiod = "December2022_RTGS_Income"

        self.cur.execute(f"Select * from {self.Incperiod} ")
        rows=self.cur.fetchall()

        itotal=0
        for row in rows :
            itotal += float(row[4])
            print(itotal)



if __name__== "__main__":
    root=Tk()
    obj=CCalculator(root)
    root.mainloop()

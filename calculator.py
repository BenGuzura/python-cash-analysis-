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

        title=Label(self.root, text="Munyaradzi Primary School", font=("Times New Roman", 18, "bold"), bg="blue", fg="white").pack(side=TOP, fill=BOTH)
        
                #=====Calculator function
        def get_Input(num):
            xnum=calcuInput.get()+str(num)
            calcuInput.set(xnum)

        def ClearCalculator():
            calcuInput.set('')

        def CalResults():
            Results=calcuInput.get()
            try:
                calcuInput.set(eval(Results))
            
            except Exception as ex:
                messagebox.showerror("error","Invalid Input",parent=root)

                
        #==Calculator===========
        Calculator = Frame(self.root, bd=9, relief=RIDGE, bg="#3B3131")
        Calculator.place(x=0,y=0,  height=500, width=490)

        calcuInput=StringVar()


        TextCalculcInput= Entry(Calculator, font=("Bradley Hand ITC", 32),textvariable=calcuInput, width=20,bd=10,relief=GROOVE,justify=RIGHT ,state="readonly" )
        TextCalculcInput.grid(row=0,columnspan=5)

        btn7=Button(Calculator, text='7',font=("Bradley Hand ITC", 15, "bold"), command=lambda:get_Input(7) , width=8,bd=5,pady=13,cursor="hand2").grid(row=1,column=0)
        btn8=Button(Calculator, text='8',font=("Bradley Hand ITC", 15, "bold"),command=lambda:get_Input(8) , width=8,bd=5,pady=13,cursor="hand2").grid(row=1,column=1)
        btn9=Button(Calculator, text='9',font=("Bradley Hand ITC", 15, "bold"),command=lambda:get_Input(9) , width=8,bd=5,pady=13,cursor="hand2").grid(row=1,column=2)
        btnSum=Button(Calculator, text='+',font=("Bradley Hand ITC", 15, "bold"),command=lambda:get_Input('+') , width=8,bd=5,pady=13,cursor="hand2").grid(row=1,column=3)

        btn4=Button(Calculator, text='4',font=("Bradley Hand ITC", 15, "bold"),command=lambda:get_Input(4) , width=8,bd=5,pady=14,cursor="hand2").grid(row=2,column=0)
        btn5=Button(Calculator, text='5',font=("Bradley Hand ITC", 15, "bold"), command=lambda:get_Input(5) ,width=8,bd=5,pady=14,cursor="hand2").grid(row=2,column=1)
        btn6=Button(Calculator, text='6',font=("Bradley Hand ITC", 15, "bold"), command=lambda:get_Input(6) ,width=8,bd=5,pady=14,cursor="hand2").grid(row=2,column=2)
        btnSub=Button(Calculator, text='-',font=("Bradley Hand ITC", 15, "bold"), command=lambda:get_Input('-') , width=8,bd=5,pady=14,cursor="hand2").grid(row=2,column=3)

        btn1=Button(Calculator, text='1',font=("Bradley Hand ITC", 15, "bold"), command=lambda:get_Input(1) ,width=8,bd=5,pady=15,cursor="hand2").grid(row=3,column=0)
        btn2=Button(Calculator, text='2',font=("Bradley Hand ITC", 15, "bold"), command=lambda:get_Input(2) ,width=8,bd=5,pady=15,cursor="hand2").grid(row=3,column=1)
        btn3=Button(Calculator, text='3',font=("Bradley Hand ITC", 15, "bold"),command=lambda:get_Input(3) , width=8,bd=5,pady=15,cursor="hand2").grid(row=3,column=2)
        btnDvd=Button(Calculator, text='/',font=("Bradley Hand ITC", 15, "bold"),command=lambda:get_Input('/') , width=8,bd=5,pady=15,cursor="hand2").grid(row=3,column=3)

        btn0=Button(Calculator, text='0',font=("Bradley Hand ITC", 15, "bold"),command=lambda:get_Input(0) , width=8,bd=5,pady=15,cursor="hand2").grid(row=4,column=0)
        btnC=Button(Calculator, text='C',font=("Bradley Hand ITC", 15, "bold"),command=ClearCalculator , width=8,bd=5,pady=15,cursor="hand2").grid(row=4,column=1)
        btnFT=Button(Calculator, text='.',font=("Bradley Hand ITC", 15, "bold"),command=lambda:get_Input('.'), width=8,bd=5,pady=15,cursor="hand2").grid(row=4,column=2)
        btnMl=Button(Calculator, text='*',font=("Bradley Hand ITC", 15, "bold"), command=lambda:get_Input('*') ,width=8,bd=5,pady=15,cursor="hand2").grid(row=4,column=3)

        btnBrL=Button(Calculator, text='(',font=("Bradley Hand ITC", 15, "bold"),command=lambda:get_Input('(') , width=8,bd=5,pady=15,cursor="hand2").grid(row=5,column=0)
        btnBrR=Button(Calculator, text=')',font=("Bradley Hand ITC", 15, "bold"),command=lambda:get_Input(')') , width=8,bd=5,pady=15,cursor="hand2").grid(row=5,column=1)
        btnEq=Button(Calculator, text='=',font=("Bradley Hand ITC", 15, "bold"),command=CalResults, width=8,bd=5,pady=15,cursor="hand2").grid(row=5,column=2)



if __name__== "__main__":
    root=Tk()
    obj=CCalculator(root)
    root.mainloop()

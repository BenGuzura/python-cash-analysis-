from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from calculator import CCalculator
from UpdateIn import CupdateINC
from updateExp import CupdateEXP
import sqlite3
import os                      
import time                     



class RTGS:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Cash Analysis")
        self.root.state('zoomed')                    
        self.root.configure(bg='grey')
        self.root.focus_force() 
        #self.root.overrideredirect(1) #remove close and maximise icons



        #===========All Variables============
        self.PeriodYear=StringVar()
        self.PeriodMonth=StringVar()
        self.ReceptNo=StringVar()
        self.Details=StringVar()
        self.Date=StringVar()
        self.Total=StringVar() 
        self.BF=StringVar()
        self.SPORTS=StringVar() 
        self.GPF=StringVar()
        self.EWP=StringVar()
        self.ZMSEC=StringVar()
        self.G7Vac=StringVar() 
        self.BHole=StringVar()
        self.ExamTrans=StringVar() 
        self.FeedingP=StringVar()

        self.IncT_Total=StringVar() 
        self.IncT_BF=StringVar()
        self.IncT_SPORTS=StringVar() 
        self.IncT_GPF=StringVar()
        self.IncT_EWP=StringVar()
        self.IncT_ZMSEC=StringVar()
        self.IncT_G7Vac=StringVar() 
        self.IncT_BHole=StringVar()
        self.IncT_ExamTrans=StringVar() 
        self.IncT_FeedingP=StringVar()


        self.ExT_Total=StringVar() 
        self.ExT_BF=StringVar()
        self.ExT_SPORTS=StringVar() 
        self.ExT_GPF=StringVar()
        self.ExT_EWP=StringVar()
        self.ExT_ZMSEC=StringVar()
        self.ExT_G7Vac=StringVar() 
        self.ExT_BHole=StringVar()
        self.ExT_ExamTrans=StringVar() 
        self.ExT_FeedingP=StringVar()

        self.PLT_Total=StringVar() 
        self.PLT_BF=StringVar()
        self.PLT_SPORTS=StringVar() 
        self.PLT_GPF=StringVar()
        self.PLT_EWP=StringVar()
        self.PLT_ZMSEC=StringVar()
        self.PLT_G7Vac=StringVar() 
        self.PLT_BHole=StringVar()
        self.PLT_ExamTrans=StringVar() 
        self.PLT_FeedingP=StringVar()


        title=Label(self.root, text="RTGS Cash Analysis ", font=("Times New Roman", 18, "bold"), bg="blue", fg="white").pack(side=TOP, fill=BOTH)
        
        #====Headings=============
        MReceiptno=Label(self.root, text="ReceiptNo", font=("Times New Roman", 10), bg="grey", fg="white").place(x=150, y=30)
        MDetails=Label(self.root, text="Details", font=("Times New Roman", 10), bg="grey", fg="white").place(x=235, y=30)
        MDate=Label(self.root, text="Date", font=("Times New Roman", 10), bg="grey", fg="white").place(x=340, y=30)
        MTotalsL=Label(self.root, text="Total", font=("Times New Roman", 10), bg="grey", fg="white").place(x=430, y=30)
        MTBFL=Label(self.root, text="BF", font=("Times New Roman", 10), bg="grey", fg="white").place(x=535, y=30)
        MTSportsL=Label(self.root, text="Sports", font=("Times New Roman", 10), bg="grey", fg="white").place(x=620, y=30)
        MTGPFL=Label(self.root, text="GPF", font=("Times New Roman", 10), bg="grey", fg="white").place(x=735, y=30)
        MTEWPL=Label(self.root, text="EWP", font=("Times New Roman", 10), bg="grey", fg="white").place(x=835, y=30)
        MTZIMSECL=Label(self.root, text="ZIMSEC", font=("Times New Roman", 10), bg="grey", fg="white").place(x=935, y=30)
        MTG7VacL=Label(self.root, text="G7Vac", font=("Times New Roman", 10), bg="grey", fg="white").place(x=1035, y=30)
        MTBHL=Label(self.root, text="B/HOLE", font=("Times New Roman", 10), bg="grey", fg="white").place(x=1120, y=30)
        MTExamTL=Label(self.root, text="Exam/Tra", font=("Times New Roman", 10), bg="grey", fg="white").place(x=1220, y=30)
        MTFPROL=Label(self.root, text="F/PRO", font=("Times New Roman", 10), bg="grey", fg="white").place(x=1320, y=30)

        MReceiptno=Entry(self.root,textvariable=self.ReceptNo,  font=("Times New Roman", 10)).place(x=150, y=45)
        MDetails=Entry(self.root,textvariable= self.Details, font=("Times New Roman", 10)).place(x=235, y=45)
        MDate=Entry(self.root,textvariable=self.Date,  font=("Times New Roman", 10)).place(x=335, y=45)
        MTotalsL=Entry(self.root,textvariable=self.Total,  font=("Times New Roman", 10)).place(x=435, y=45)
        MTBFL=Entry(self.root, textvariable=self.BF, font=("Times New Roman", 10)).place(x=535, y=45)
        MTSportsL=Entry(self.root,textvariable=self.SPORTS,  font=("Times New Roman",10)).place(x=620, y=45)
        MTGPFL=Entry(self.root,textvariable=self.GPF,  font=("Times New Roman", 10)).place(x=735, y=45)
        MTEWPL=Entry(self.root, textvariable=self.EWP, font=("Times New Roman", 10)).place(x=835, y=45)
        MTZIMSECL=Entry(self.root,textvariable=self.ZMSEC,  font=("Times New Roman", 10)).place(x=935, y=45)
        MTG7VacL=Entry(self.root, textvariable=self.G7Vac, font=("Times New Roman", 10)).place(x=1035, y=45)
        MTBHL=Entry(self.root,textvariable=self.BHole,  font=("Times New Roman", 10)).place(x=1120, y=45)
        MTExamTL=Entry(self.root,textvariable=self.ExamTrans,  font=("Times New Roman", 10)).place(x=1220, y=45)
        MTFPROL=Entry(self.root,textvariable=self.FeedingP,  font=("Times New Roman", 10)).place(x=1310, y=45)

        #LeftMenu=Frame(self.root,bg="white", width=150, height=700)
        #LeftMenu.place(x=0, y=50)

        LeftMenu=Frame(root, bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0, y=30, width=150,height=700)

        Menutitle=Label(LeftMenu, text="MUNYARADZI \n PRIMARY \n SCHOOL", font=("Times New Roman", 15, "bold"), bg="white", fg="blue").place(x=0, y=10)
        DateT=Label(LeftMenu, text="Period Date ",  font=("Times New Roman", 12), bg="#00008B", fg="white").place(x=0, y=100, relwidth=1)
        PYear=ttk.Combobox( LeftMenu, textvariable=self.PeriodYear ,values=["2022", "2023", "2024", "2025","2026"],state="readonly", justify=CENTER ,font=("Times New Roman", 15)).place(x=0, y=125,relwidth=1)
        self.PeriodYear.set("2023")
        PMonth=ttk.Combobox( LeftMenu, textvariable=self.PeriodMonth ,values=["January", "February", "March", "April", "May","June", "July", "August", "September", "October","Novermber","December"],state="readonly", justify=CENTER ,font=("Times New Roman", 15)).place(x=0, y=165,relwidth=1)
        self.PeriodMonth.set("January")
        ViewRec=Button(LeftMenu, text="View cash \n analysis for\n the period", command=self.Database,  font=("Times New Roman", 10), bg="green", fg="white").place(x=0, y=200,relwidth=1)

       
        #===========Left Menu Buttons===========
        MainMenu=Button(LeftMenu, text="Re-Fresh", command=self.Database, font=("Times New Roman", 15), bg="green", fg="white").place(x=0, y=250, relwidth=1, height=70)
        Calculator=Button(LeftMenu, text="Calculator", command=self.students,  font=("Times New Roman", 13), bg="#3B3131", fg="white").place(x=0, y=460, relwidth=1,height=70)
        NewIncome=Button(LeftMenu, text="Update \nIncome", command=self.UpdaInc, font=("Times New Roman", 13), bg="#2B60DE", fg="white").place(x=0, y=320, relwidth=1,height=70)
        NewExpent=Button(LeftMenu, text="Update \n Expentiture",command=self.UpdateExp, font=("Times New Roman", 13), bg="orange", fg="white").place(x=0, y=390, relwidth=1,height=70)
        #UpdateIncome=Button(LeftMenu, text="Update Income \n Values", command=self.UpdaInc, font=("Times New Roman", 12), bg="#00008B", fg="white").place(x=0, y=530, relwidth=1,height=60)
        #UpdateExpnt=Button(LeftMenu, text="Update Epentiture \n Values",command=self.UpdateExp, font=("Times New Roman", 12), bg="#00008B", fg="white").place(x=0, y=580, relwidth=1,height=50)
        Exit=Button(LeftMenu, text="Exit ", command=self.Close, font=("Times New Roman", 15), bg="red", fg="white").place(x=0, y=630, relwidth=1,height=70)




        #==========Main Menu==============
 
        #=========Income records========== 
        self.IncomeFrame=Frame(root, bd=2,relief=RIDGE,bg="white")
        self.IncomeFrame.place(x=150, y=65, width=1220,height=280)

        self.Inctitle=Label(self.IncomeFrame, text="RTGS Income for the period January 2023 ", font=("Times New Roman", 12), bg="#000080", fg="white").pack(side=TOP, fill=BOTH)
            
        scrolly=Scrollbar(self.IncomeFrame,orient=VERTICAL)
        scrollx=Scrollbar(self.IncomeFrame,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        self.IncomeTable=ttk.Treeview(self.IncomeFrame,columns=("ID","ReceptNo","Details","Date","Total", "BF","SPORTS", "GPF","EWP","ZMSEC","G7Vac", "BHole","ExamTrans", "FeedingP" ), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        self.IncomeTable.pack(fill=BOTH, expand=1)
    
        scrollx.configure(command=self.IncomeTable.xview)
        scrolly.configure(command=self.IncomeTable.yview)

        self.IncomeTable.heading("ID",text="ID")
        self.IncomeTable.heading("ReceptNo",text="ReceptNo")
        self.IncomeTable.heading("Details",text="Details")
        self.IncomeTable.heading("Date",text="Date")
        self.IncomeTable.heading("Total",text="Total")
        self.IncomeTable.heading("BF",text="BF")
        self.IncomeTable.heading("SPORTS",text="SPORTS")
        self.IncomeTable.heading("GPF",text="GPF")
        self.IncomeTable.heading("EWP",text="EWP")
        self.IncomeTable.heading("ZMSEC",text="ZMSEC")
        self.IncomeTable.heading("G7Vac",text="G7Vac")
        self.IncomeTable.heading("BHole",text="B/Hole")
        self.IncomeTable.heading("ExamTrans",text="Exam/Trans")
        self.IncomeTable.heading("FeedingP",text="Feeding/P")

        self.IncomeTable.column("ID",width=30)
        self.IncomeTable.column("ReceptNo",width=80)
        self.IncomeTable.column("Details",width=100)
        self.IncomeTable.column("Date",width=100)
        self.IncomeTable.column("Total",width=100)
        self.IncomeTable.column("BF",width=100)
        self.IncomeTable.column("SPORTS",width=100)
        self.IncomeTable.column("GPF",width=100)
        self.IncomeTable.column("EWP",width=100)
        self.IncomeTable.column("ZMSEC",width=100)
        self.IncomeTable.column("G7Vac",width=100)
        self.IncomeTable.column("BHole",width=100)
        self.IncomeTable.column("ExamTrans",width=100)
        self.IncomeTable.column("FeedingP",width=100)
        self.IncomeTable["show"]="headings"
        self.IncomeTable.bind("<ButtonRelease-1>", self.get_data)


        #=========Expentiture records========== 
        self.ExpFrame=Frame(root, bd=2,relief=RIDGE,bg="white")
        self.ExpFrame.place(x=150, y=345, width=1220,height=270)

        self.Exptitle=Label(self.ExpFrame, text="RTGS Expentiture for the period January 2023 ", font=("Times New Roman", 12), bg="orange", fg="white").pack(side=TOP, fill=BOTH)
        scrolly=Scrollbar(self.ExpFrame,orient=VERTICAL)
        scrollx=Scrollbar(self.ExpFrame,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        self.ExpTable=ttk.Treeview(self.ExpFrame,columns=("ID","ReceptNo","Details","Date","Total", "BF","SPORTS", "GPF", "EWP","ZMSEC","G7Vac", "BHole","ExamTrans", "FeedingP"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        self.ExpTable.pack(fill=BOTH, expand=1)
    
        scrollx.configure(command=self.ExpTable.xview)
        scrolly.configure(command=self.ExpTable.yview)

        self.ExpTable.heading("ID",text="ID")
        self.ExpTable.heading("ReceptNo",text="ReceptNo")
        self.ExpTable.heading("Details",text="Details")
        self.ExpTable.heading("Date",text="Date")
        self.ExpTable.heading("Total",text="Total")
        self.ExpTable.heading("BF",text="BF")
        self.ExpTable.heading("SPORTS",text="SPORTS")
        self.ExpTable.heading("GPF",text="GPF")
        self.ExpTable.heading("EWP",text="EWP")
        self.ExpTable.heading("ZMSEC",text="ZMSEC")
        self.ExpTable.heading("G7Vac",text="G7Vac")
        self.ExpTable.heading("BHole",text="B/Hole")
        self.ExpTable.heading("ExamTrans",text="Exam/Trans")
        self.ExpTable.heading("FeedingP",text="Feeding/P")

        self.ExpTable.column("ID",width=30)
        self.ExpTable.column("ReceptNo",width=80)
        self.ExpTable.column("Details",width=100)
        self.ExpTable.column("Date",width=100)
        self.ExpTable.column("Total",width=100)
        self.ExpTable.column("BF",width=100)
        self.ExpTable.column("SPORTS",width=100)
        self.ExpTable.column("GPF",width=100)
        self.ExpTable.column("EWP",width=100)
        self.ExpTable.column("ZMSEC",width=100)
        self.ExpTable.column("G7Vac",width=100)
        self.ExpTable.column("BHole",width=100)
        self.ExpTable.column("ExamTrans",width=100)
        self.ExpTable.column("FeedingP",width=100)
        self.ExpTable["show"]="headings"
        self.ExpTable.bind("<ButtonRelease-1>", self.get_data2)


        #====Profit or loss=====
        self.PLFrame=Frame(root, bd=2,relief=RIDGE,bg="grey")
        self.PLFrame.place(x=150, y=615, width=1220,height=200)

        TotalInL=Label(self.PLFrame, text="Total Income", font=("Times New Roman", 10), bg="grey", fg="white").place(x=0, y=25)
        TotalExL=Label(self.PLFrame, text="Total Expent", font=("Times New Roman", 10), bg="grey", fg="white").place(x=0, y=55)
        PLL=Label(self.PLFrame, text="Profite/loss", font=("Times New Roman", 10), bg="grey", fg="white").place(x=0, y=85)

        #====Headings=============
        TotalsL=Label(self.PLFrame, text="Total", font=("Times New Roman", 10), bg="grey", fg="white").place(x=80, y=5)
        TBFL=Label(self.PLFrame, text="BF", font=("Times New Roman", 10), bg="grey", fg="white").place(x=180, y=5)
        TSportsL=Label(self.PLFrame, text="Sports", font=("Times New Roman", 10), bg="grey", fg="white").place(x=280, y=5)
        TGPFL=Label(self.PLFrame, text="GPF", font=("Times New Roman", 10), bg="grey", fg="white").place(x=380, y=5)
        TEWPL=Label(self.PLFrame, text="EWP", font=("Times New Roman", 10), bg="grey", fg="white").place(x=480, y=5)
        TZIMSECL=Label(self.PLFrame, text="ZIMSEC", font=("Times New Roman", 10), bg="grey", fg="white").place(x=580, y=5)
        TG7VacL=Label(self.PLFrame, text="G7Vac", font=("Times New Roman", 10), bg="grey", fg="white").place(x=680, y=5)
        TBHL=Label(self.PLFrame, text="B/HOLE", font=("Times New Roman", 10), bg="grey", fg="white").place(x=780, y=5)
        TExamTL=Label(self.PLFrame, text="Exam/Tra", font=("Times New Roman", 10), bg="grey", fg="white").place(x=880, y=5)
        TFPROL=Label(self.PLFrame, text="F/PRO", font=("Times New Roman", 10), bg="grey", fg="white").place(x=980, y=5)

       #====Income Eentries=============
        TotalsIE=Entry(self.PLFrame, textvariable=self.IncT_Total,state="readonly", font=("Times New Roman", 10)).place(x=80, y=25)
        TBFIE=Entry(self.PLFrame,textvariable=self.IncT_BF, state="readonly" ,font=("Times New Roman", 10)).place(x=180, y=25)
        TSportsIE=Entry(self.PLFrame,textvariable=self.IncT_SPORTS, state="readonly" ,  font=("Times New Roman", 10)).place(x=280, y=25)
        TGPFIE=Entry(self.PLFrame,textvariable=self.IncT_GPF ,state="readonly",  font=("Times New Roman", 10)).place(x=380, y=25)
        TEWPIE=Entry(self.PLFrame, textvariable=self.IncT_EWP , state="readonly",font=("Times New Roman", 10)).place(x=480, y=25)
        TZIMSECIE=Entry(self.PLFrame,textvariable=self.IncT_ZMSEC ,state="readonly",  font=("Times New Roman", 10)).place(x=580, y=25)
        TG7VacIE=Entry(self.PLFrame, textvariable=self.IncT_G7Vac,state="readonly", font=("Times New Roman", 10)).place(x=680, y=25)
        TBHIE=Entry(self.PLFrame, textvariable=self.IncT_BHole ,state="readonly", font=("Times New Roman", 10)).place(x=780, y=25)
        TExamTIE=Entry(self.PLFrame,textvariable=self.IncT_ExamTrans , state="readonly", font=("Times New Roman", 10)).place(x=880, y=25)
        TFPROIE=Entry(self.PLFrame, textvariable=self.IncT_FeedingP , state="readonly",font=("Times New Roman", 10)).place(x=980, y=25)

        #====Expentiture Eentries=============
        TotalsEE=Entry(self.PLFrame,textvariable=self.ExT_Total ,state="readonly",  font=("Times New Roman", 10)).place(x=80, y=55)
        TBFEE=Entry(self.PLFrame, textvariable=self.ExT_BF ,state="readonly",font=("Times New Roman", 10)).place(x=180, y=55)
        TSportsEE=Entry(self.PLFrame, textvariable=self.ExT_SPORTS ,state="readonly", font=("Times New Roman", 10)).place(x=280, y=55)
        TGPFEE=Entry(self.PLFrame, textvariable=self.ExT_GPF , state="readonly",font=("Times New Roman", 10)).place(x=380, y=55)
        TEWPEE=Entry(self.PLFrame, textvariable=self.ExT_EWP , state="readonly",font=("Times New Roman", 10)).place(x=480, y=55)
        TZIMSECEE=Entry(self.PLFrame, textvariable=self.ExT_ZMSEC ,state="readonly", font=("Times New Roman", 10)).place(x=580, y=55)
        TG7VacEE=Entry(self.PLFrame,textvariable=self.ExT_G7Vac , state="readonly", font=("Times New Roman", 10)).place(x=680, y=55)
        TBHEE=Entry(self.PLFrame, textvariable=self.ExT_BHole ,state="readonly", font=("Times New Roman", 10)).place(x=780, y=55)
        TExamTEE=Entry(self.PLFrame, textvariable=self.ExT_ExamTrans , state="readonly",font=("Times New Roman", 10)).place(x=880, y=55)
        TFPROEE=Entry(self.PLFrame, textvariable=self.ExT_FeedingP , state="readonly",font=("Times New Roman", 10)).place(x=980, y=55)

        #====P/L Eentries=============
        TotalsPLE=Entry(self.PLFrame,textvariable=self.PLT_Total,  font=("Times New Roman", 10), state="readonly").place(x=80, y=85)
        TBFPLE=Entry(self.PLFrame, textvariable=self.PLT_BF,font=("Times New Roman", 10), state="readonly").place(x=180, y=85)
        TSportsPLE=Entry(self.PLFrame,textvariable=self.PLT_SPORTS,  font=("Times New Roman", 10), state="readonly").place(x=280, y=85)
        TGPFPLE=Entry(self.PLFrame, textvariable=self.PLT_GPF, font=("Times New Roman", 10), state="readonly").place(x=380, y=85)
        TEWPPLE=Entry(self.PLFrame, textvariable=self.PLT_EWP, font=("Times New Roman", 10), state="readonly").place(x=480, y=85)
        TZIMSECPLE=Entry(self.PLFrame, textvariable=self.PLT_ZMSEC, font=("Times New Roman", 10), state="readonly").place(x=580, y=85)
        TG7VacPLE=Entry(self.PLFrame,textvariable=self.PLT_G7Vac,  font=("Times New Roman", 10), state="readonly").place(x=680, y=85)
        TBHPLE=Entry(self.PLFrame, textvariable=self.PLT_BHole, font=("Times New Roman", 10), state="readonly").place(x=780, y=85)
        TExamTPLE=Entry(self.PLFrame, textvariable=self.PLT_ExamTrans, font=("Times New Roman", 10), state="readonly").place(x=880, y=85)
        TFPROPLE=Entry(self.PLFrame, textvariable=self.PLT_FeedingP, font=("Times New Roman", 10), state="readonly").place(x=980, y=85)

        UpdTotals=Button(self.PLFrame, text="Get Totals\nUpdates\n\n....", command=self.Totals, font=("Times New Roman", 15), bg="green", fg="white").place(x=1110, y=25)


        self.Database()
 



        Ftitle=Label(self.root, text="designed by N.Guzura | naisonguzura@gmail.com @ 2023", font=("Times New Roman", 10, "bold"), bg="blue", fg="white").pack(side=BOTTOM, fill=BOTH)
    #=======All Functions============


    def Close(self):
        exit()
    
    def students(self):
        self.new_Window=Toplevel(self.root)
        self.app=CCalculator(self.new_Window)

    def UpdaInc(self):
        
        if self.PeriodMonth.get() == "Choose Month" or self.PeriodMonth.get()=="Choose Year":
            messagebox.showerror("Warning", "Choose the responsive Month and Year")
        else:
            self.new_Window=Toplevel(self.root)
            year=self.PeriodYear.get()
            month=self.PeriodMonth.get()
            self.app=CupdateINC(self.new_Window, year, month)

    def UpdateExp(self):
        if self.PeriodMonth.get() == "Choose Month" or self.PeriodMonth.get()=="Choose Year":
            messagebox.showerror("Warning", "Choose the responsive Month and Year")
        else:
            self.new_Window=Toplevel(self.root)
            year=self.PeriodYear.get()
            month=self.PeriodMonth.get()
            self.app=CupdateEXP(self.new_Window, year, month)

    def Show1(self):
        try:
           self.cur.execute(f"Select * from {self.Incperiod} ")
           rows=self.cur.fetchall()
           self.IncomeTable.delete(*self.IncomeTable.get_children())
           for row in rows :
               self.IncomeTable.insert('',END, values=row)

        except Exception as ex:
            messagebox.showerror("error",f"Error due to: {str(ex)}",parent=self.root)

    def Show2(self):
        try:
           self.cur.execute(f"Select * from {self.Expperiod} ")
           rows=self.cur.fetchall()
           self.ExpTable.delete(*self.ExpTable.get_children())
           for row in rows :
               self.ExpTable.insert('',END, values=row)

        except Exception as ex:
            messagebox.showerror("error",f"Error due to: {str(ex)}",parent=self.root)

    def Database(self):
        try:
            #======================Database connectivity and tablesconfigurations===========
            self.con=sqlite3.connect(database=r'CAMP.db')
            self.cur=self.con.cursor()


            self.Incperiod = str(self.PeriodMonth.get()+self.PeriodYear.get()+"_RTGS_Income")
            self.Expperiod = str(self.PeriodMonth.get()+self.PeriodYear.get()+"_RTGS_Expentiture")
            self.PLperiod = str(self.PeriodMonth.get()+self.PeriodYear.get()+"_RTGS_PL")



            self.cur.execute(f"CREATE TABLE IF NOT EXISTS {self.Incperiod}(id INTEGER PRIMARY KEY AUTOINCREMENT, ReceptNo text, Details text, Date text, Total text, BF text, SPORTS text, GPF text, EWP text, ZMSEC text, G7Vac text, BHole text, ExamTrans text, FeedingP text)")
            self.con.commit()

            self.cur.execute(f"CREATE TABLE IF NOT EXISTS {self.Expperiod}(id INTEGER PRIMARY KEY AUTOINCREMENT, ReceptNo text, Details text, Date text, Total text, BF text, SPORTS text, GPF text, EWP text, ZMSEC text, G7Vac text, BHole text, ExamTrans text, FeedingP text)")
            self.con.commit()

            self.cur.execute(f"CREATE TABLE IF NOT EXISTS {self.PLperiod}(id INTEGER PRIMARY KEY AUTOINCREMENT, Total text, BF text, SPORTS text, GPF text, EWP text, ZMSEC text, G7Vac text, BHole text, ExamTrans text, FeedingP text)")
            self.con.commit()

            self.cur.execute(f"Select * from {self.PLperiod}")
            row = self.cur.fetchone()

            if row == None :
                self.cur.execute(f"Insert into {self.PLperiod} ( id , Total , BF , SPORTS , GPF , EWP , ZMSEC , G7Vac , BHole , ExamTrans , FeedingP  ) values(?,?,?,?,?,?,?,?,?,?,?)", (1, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00))
                self.con.commit()
                self.cur.execute(f"Insert into {self.PLperiod} ( id , Total , BF , SPORTS , GPF , EWP , ZMSEC , G7Vac , BHole , ExamTrans , FeedingP  ) values(?,?,?,?,?,?,?,?,?,?,?)", (2, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00))
                self.con.commit()
                self.cur.execute(f"Insert into {self.PLperiod} ( id , Total , BF , SPORTS , GPF , EWP , ZMSEC , G7Vac , BHole , ExamTrans , FeedingP  ) values(?,?,?,?,?,?,?,?,?,?,?)", (3, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00))
                self.con.commit()
           
        except Exception as ex:
            messagebox.showerror("error",f"Error due to: {str(ex)}",parent=self.root)
        
        self.Show1()
        self.Show2()

    def get_data(self, ev):
        f=self.IncomeTable.focus()
        content = (self.IncomeTable.item(f))
        row=content['values']
        #print(row)

        self.ReceptNo.set(row[1])
        self.Details.set(row[2])
        self.Date.set(row[3])
        self.Total.set(row[4]) 
        self.BF.set(row[5])
        self.SPORTS.set(row[6]) 
        self.GPF.set(row[7])
        self.EWP.set(row[8])
        self.ZMSEC.set(row[9])
        self.G7Vac.set(row[10]) 
        self.BHole.set(row[11])
        self.ExamTrans.set(row[12]) 
        self.FeedingP.set(row[13])

    def get_data2(self, ev):
        f=self.ExpTable.focus()
        content = (self.ExpTable.item(f))
        row=content['values']
        #print(row)

        self.ReceptNo.set(row[1])
        self.Details.set(row[2])
        self.Date.set(row[3])
        self.Total.set(row[4]) 
        self.BF.set(row[5])
        self.SPORTS.set(row[6]) 
        self.GPF.set(row[7])
        self.EWP.set(row[8])
        self.ZMSEC.set(row[9])
        self.G7Vac.set(row[10]) 
        self.BHole.set(row[11])
        self.ExamTrans.set(row[12]) 
        self.FeedingP.set(row[13])

    def Totals(self):
        ITotal=0 
        IBF=0
        ISPORTS=0 
        IGPF=0
        IEWP=0
        IZMSEC=0
        IG7Vac=0 
        IBHole=0
        IExamTrans=0 
        IFeedingP=0

        ETotal=0 
        EBF=0
        ESPORTS=0 
        EGPF=0
        EEWP=0
        EZMSEC=0
        EG7Vac=0 
        EBHole=0
        EExamTrans=0 
        EFeedingP=0

        PLTotal=0 
        PLBF=0
        PLSPORTS=0 
        PLGPF=0
        PLEWP=0
        PLZMSEC=0
        PLG7Vac=0 
        PLBHole=0
        PLExamTrans=0 
        PLFeedingP=0
       

        self.cur.execute(f"Select * from {self.Incperiod} ")
        rows1=self.cur.fetchall()

        for row in rows1 :

            ITotal += float(row[4])
            IBF += float(row[5])
            ISPORTS += float(row[6])
            IGPF+= float(row[7])
            IEWP+= float(row[8])
            IZMSEC+= float(row[9])
            IG7Vac+= float(row[10])
            IBHole+= float(row[11])
            IExamTrans+= float(row[12])
            IFeedingP+= float(row[13])
        
        self.cur.execute(f"Select * from {self.Expperiod} ")
        rows2=self.cur.fetchall()

        for row in rows2 :

            ETotal += float(row[4])
            EBF += float(row[5])
            ESPORTS += float(row[6])
            EGPF+= float(row[7])
            EEWP+= float(row[8])
            EZMSEC+= float(row[9])
            EG7Vac+= float(row[10])
            EBHole+= float(row[11])
            EExamTrans+= float(row[12])
            EFeedingP+= float(row[13])

        PLTotal=ITotal-ETotal 
        PLBF=IBF-EBF
        PLSPORTS=ISPORTS-ESPORTS
        PLGPF=IGPF-EGPF
        PLEWP=IEWP-EEWP
        PLZMSEC=IZMSEC-EZMSEC
        PLG7Vac=IG7Vac-EG7Vac 
        PLBHole=IBHole-EBHole
        PLExamTrans=IExamTrans-EExamTrans
        PLFeedingP=IFeedingP-EFeedingP


        self.IncT_Total.set(ITotal) 
        self.IncT_BF.set(IBF)
        self.IncT_SPORTS.set(ISPORTS) 
        self.IncT_GPF.set(IGPF)
        self.IncT_EWP.set(IEWP)
        self.IncT_ZMSEC.set(IZMSEC)
        self.IncT_G7Vac.set(IG7Vac) 
        self.IncT_BHole.set(IBHole)
        self.IncT_ExamTrans.set(IExamTrans) 
        self.IncT_FeedingP.set(IFeedingP)

        self.ExT_Total.set(ETotal) 
        self.ExT_BF.set(EBF)
        self.ExT_SPORTS.set(ESPORTS) 
        self.ExT_GPF.set(EGPF)
        self.ExT_EWP.set(EEWP)
        self.ExT_ZMSEC.set(EZMSEC)
        self.ExT_G7Vac.set(EG7Vac) 
        self.ExT_BHole.set(EBF)
        self.ExT_ExamTrans.set(EExamTrans) 
        self.ExT_FeedingP.set(EFeedingP)

        self.PLT_Total.set(PLTotal) 
        self.PLT_BF.set(PLBF)
        self.PLT_SPORTS.set(PLSPORTS) 
        self.PLT_GPF.set(PLGPF)
        self.PLT_EWP.set(PLEWP)
        self.PLT_ZMSEC.set(PLZMSEC)
        self.PLT_G7Vac.set(PLG7Vac) 
        self.PLT_BHole.set(PLBHole)
        self.PLT_ExamTrans.set(PLExamTrans) 
        self.PLT_FeedingP.set(PLFeedingP)
        


if __name__== "__main__":
    root=Tk()
    obj=RTGS(root)
    root.mainloop()




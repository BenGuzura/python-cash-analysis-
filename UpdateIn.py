from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import sqlite3
import os                      
import time                     



class CupdateINC:
    def __init__(self, root, year, month):
        self.root=root
        self.root.geometry("1220x700+150+30")
        self.root.title("Cash Analysis")
        #self.root.state('zoomed')                    
        self.root.configure(bg='grey') 
        self.root.focus_force()
        #self.root.overrideredirect(1) #remove close and maximise icons 
        #RTGS Cash Analysis (UPDATE EXPENTITURE RECORDS FOR THE MONTH


        try:
            #======================Database connectivity and tablesconfigurations===========
            self.con=sqlite3.connect(database=r'CAMP.db')
            self.cur=self.con.cursor()

            self.year=year
            self.month=month

            self.Incperiod = str(self.month + self.year+"_RTGS_Income")
            self.Expperiod = str(self.month + self.year+"_RTGS_Expentiture")
            self.PLperiod = str(self.month + self.year+"_RTGS_PL")
            
            #print(self.year)
            #print(self.month)
            #print(self.Incperiod)

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
        self.Clear() 

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



        title=Label(self.root, text=f"RTGS Cash Analysis (UPDATE INCOME RECORDS FOR THE MONTH {self.month}-{self.year})", font=("Times New Roman", 18, "bold"), bg="blue", fg="white").pack(side=TOP, fill=BOTH)

         #====Headings=============
        MReceiptno=Label(self.root, text="ReceiptNo", font=("Times New Roman", 16), bg="grey", fg="white").place(x=20, y=35)
        MDetails=Label(self.root, text="Details", font=("Times New Roman", 16), bg="grey", fg="white").place(x=280, y=35)
        MDate=Label(self.root, text="Date", font=("Times New Roman", 16), bg="grey", fg="white").place(x=480, y=35)
        MTotalsL=Label(self.root, text="Total", font=("Times New Roman", 16), bg="grey", fg="white").place(x=680, y=35)
        MTBFL=Label(self.root, text="BF", font=("Times New Roman", 16), bg="grey", fg="white").place(x=880, y=35)

        MTSportsL=Label(self.root, text="Sports", font=("Times New Roman", 16), bg="grey", fg="white").place(x=20, y=130)
        MTGPFL=Label(self.root, text="GPF", font=("Times New Roman", 16), bg="grey", fg="white").place(x=280, y=130)
        MTEWPL=Label(self.root, text="EWP", font=("Times New Roman", 16), bg="grey", fg="white").place(x=480, y=130)
        MTZIMSECL=Label(self.root, text="ZIMSEC", font=("Times New Roman", 16), bg="grey", fg="white").place(x=680, y=130)
        MTG7VacL=Label(self.root, text="G7Vac", font=("Times New Roman", 16), bg="grey", fg="white").place(x=880, y=130)

        MTBHL=Label(self.root, text="B/HOLE", font=("Times New Roman", 16), bg="grey", fg="white").place(x=20, y=230)
        MTExamTL=Label(self.root, text="Exam/Tra", font=("Times New Roman", 16), bg="grey", fg="white").place(x=280, y=230)
        MTFPROL=Label(self.root, text="F/PRO", font=("Times New Roman", 16), bg="grey", fg="white").place(x=480, y=230)

        MReceiptno=Entry(self.root, textvariable=self.ReceptNo ,  font=("Times New Roman", 16)).place(x=20, y=65,width=160)
        MDetails=Entry(self.root,textvariable=self.Details , font=("Times New Roman", 16)).place(x=280, y=65,width=160)
        MDate=Entry(self.root, textvariable=self.Date , font=("Times New Roman", 16)).place(x=480, y=65,width=160)
        MTotalsL=Entry(self.root,textvariable=self.Total , state="readonly",  font=("Times New Roman", 16)).place(x=680, y=65,width=160)
        MTBFL=Entry(self.root,textvariable=self.BF ,  font=("Times New Roman", 16)).place(x=880, y=65,width=160)

        MTSportsL=Entry(self.root,textvariable=self.SPORTS ,  font=("Times New Roman",16)).place(x=20, y=160,width=160)
        MTGPFL=Entry(self.root,textvariable=self.GPF ,  font=("Times New Roman", 16)).place(x=280, y=160,width=160)
        MTEWPL=Entry(self.root,textvariable=self.EWP ,  font=("Times New Roman", 16)).place(x=480, y=160,width=160)
        MTZIMSECL=Entry(self.root, textvariable=self.ZMSEC , font=("Times New Roman", 16)).place(x=680, y=160,width=160)
        MTG7VacL=Entry(self.root, textvariable=self.G7Vac , font=("Times New Roman", 16)).place(x=880, y=160,width=160)

        MTBHL=Entry(self.root, textvariable=self.BHole , font=("Times New Roman", 16)).place(x=20, y=260,width=160)
        MTExamTL=Entry(self.root, textvariable=self.ExamTrans , font=("Times New Roman", 16)).place(x=280, y=260,width=160)
        MTFPROL=Entry(self.root, textvariable=self.FeedingP , font=("Times New Roman", 16)).place(x=480, y=260,width=160)

        BtnUpdate=Button(self.root, text="Save Record", command=self.AddIncome,  font=("Times New Roman", 13), bg="green", fg="white").place(x=680, y=260, width=120)
        BtnUpdate=Button(self.root, text="Update Record", command=self.UpdateInc, font=("Times New Roman", 13), bg="blue", fg="white").place(x=800, y=260, width=120)
        BTNDELETE=Button(self.root, text="Delete Record", command=self.DeleteRecord, font=("Times New Roman", 13), bg="red", fg="white").place(x=920, y=260,width=120)
        BTNClear=Button(self.root, text="Resert Ground", command=self.Clear,   font=("Times New Roman", 13), bg="orange", fg="white").place(x=1040, y=260,width=120)





        #=========Income records========== 
        self.IncomeFrame=Frame(root, bd=2,relief=RIDGE,bg="white")
        self.IncomeFrame.place(x=0, y=300, width=1220,height=400)
        
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

        self.Show()




    #========All Functions===============
    def AddIncome(self):

        try:
            if self.ReceptNo.get() =="" or self.Details.get() =="" or self.Date.get() =="":
                messagebox.showerror("error","Check your receipt No or record details or record date",parent=self.root)

            else :
                #messagebox.showinfo("Employee","Employee ID is"+ EmpID.get(),parent=MainFrame)
                self.cur.execute(f"Select * from {self.Incperiod} where ReceptNo=?", (self.ReceptNo.get(), ))
                row = self.cur.fetchone()
                

                if row != None :
                    messagebox.showerror("error","Record Already entered!!! do you want to update record??",parent=self.root)
                else :

                    #=============Find Total for the entered income===================
                    Total_Inc= float(self.BF.get() )+ float(self.SPORTS.get())+ float(self.GPF.get())+ float(self.EWP.get())+ float(self.ZMSEC.get())+ float(self.G7Vac.get())+ float(self.BHole.get())+ float(self.ExamTrans.get())+ float(self.FeedingP.get())
                    self.Total.set(Total_Inc) 

                    #=============Add income into Database===================
                    self.cur.execute(f"Insert into {self.Incperiod} ( ReceptNo , Details , Date , Total , BF , SPORTS , GPF , EWP , ZMSEC , G7Vac , BHole , ExamTrans , FeedingP) values(?,?,?,?,?,?,?,?,?,?,?,?,?)", (
                                
                                    self.ReceptNo.get(),
                                    self.Details.get(),
                                    self.Date.get(),
                                    Total_Inc, 
                                    self.BF.get(),
                                    self.SPORTS.get(), 
                                    self.GPF.get(),
                                    self.EWP.get(),
                                    self.ZMSEC.get(),
                                    self.G7Vac.get(), 
                                    self.BHole.get(),
                                    self.ExamTrans.get(), 
                                    self.FeedingP.get(),
                    ))
                    self.con.commit()


                    #=================Update Total Income ==================================
                    """
                        self.cur.execute(f"Select * from {self.PLperiod} where id=1")
                        PL = self.cur.fetchall()

                        for PLI in PL:
                            self.IncT_Total.set(float(PLI[1])+Total_Inc) 
                            self.IncT_BF.set(float(PLI[2])+float(self.BF.get()))
                            self.IncT_SPORTS.set(float(PLI[3])+float(self.SPORTS.get())) 
                            self.IncT_GPF.set(float(PLI[4])+float(self.GPF.get()))
                            self.IncT_EWP.set(float(PLI[5])+float(self.EWP.get()))
                            self.IncT_ZMSEC.set(float(PLI[6])+float(self.ZMSEC.get()))
                            self.IncT_G7Vac.set(float(PLI[7])+float(self.G7Vac.get())) 
                            self.IncT_BHole.set(float(PLI[8])+float(self.BHole.get()))
                            self.IncT_ExamTrans.set(float(PLI[9])+float(self.ExamTrans.get())) 
                            self.IncT_FeedingP.set(float(PLI[10])+float(self.FeedingP.get()))

                        print(Total_Inc)
                        print(self.IncT_Total.get())
                        print(self.IncT_BF.get())
                        print(self.IncT_SPORTS.get())
                        print(self.IncT_GPF.get())
                        print(self.IncT_EWP.get())



                        
                        self.cur.execute(f"Update  {self.PLperiod} set Total=? , BF=? , SPORTS=? , GPF=? , EWP=? , ZMSEC=? , G7Vac=? , BHole=? , ExamTrans=? , FeedingP=?  where id=1", (
                                    
                            self.IncT_Total.get() ,
                            self.IncT_BF.get(),
                            self.IncT_SPORTS.get() ,
                            self.IncT_GPF.get(),
                            self.IncT_EWP.get(),
                            self.IncT_ZMSEC.get(),
                            self.IncT_G7Vac.get() ,
                            self.IncT_BHole.get(),
                            self.IncT_ExamTrans.get(),
                            self.IncT_FeedingP.get(),

                        ))
                        self.con.commit()


                        #=================Update PL Update ==================================
                        self.cur.execute(f"Select * from {self.PLperiod} where id=2")
                        PL = self.cur.fetchall()
                        

                        for PLI in PL:
                            self.PLT_Total.set(float(self.IncT_Total.get())-float(PLI[1])) 
                            self.PLT_BF.set(float(self.IncT_BF.get())-float(PLI[2]))
                            self.PLT_SPORTS.set(float(self.IncT_SPORTS.get())-float(PLI[3])) 
                            self.PLT_GPF.set(float(self.IncT_GPF.get())-float(PLI[4]))
                            self.PLT_EWP.set(float(self.IncT_EWP.get())-float(PLI[5]))
                            self.PLT_ZMSEC.set(float(self.IncT_ZMSEC.get())-float(PLI[6]))
                            self.PLT_G7Vac.set(float(self.IncT_G7Vac.get())-float(PLI[7])) 
                            self.PLT_BHole.set(float(self.IncT_BHole.get())-float(PLI[8]))
                            self.PLT_ExamTrans.set(float(self.IncT_ExamTrans.get())-float(PLI[9])) 
                            self.PLT_FeedingP.set(float(self.IncT_FeedingP.get())-float(PLI[10]))

                        print("---------------")
                        print(self.PLT_Total.get())
                        print(self.PLT_BF.get())
                        print(self.PLT_SPORTS.get())
                        print(self.PLT_GPF.get())
                        print(self.PLT_EWP.get())



                        
                        
                        self.cur.execute(f"Update  {self.PLperiod} set Total=? , BF=? , SPORTS=? , GPF=? , EWP=? , ZMSEC=? , G7Vac=? , BHole=? , ExamTrans=? , FeedingP=?  where id=3", (
                                    
                            self.PLT_Total.get() ,
                            self.PLT_BF.get(),
                            self.PLT_SPORTS.get() ,
                            self.PLT_GPF.get(),
                            self.PLT_EWP.get(),
                            self.PLT_ZMSEC.get(),
                            self.PLT_G7Vac.get() ,
                            self.PLT_BHole.get(),
                            self.PLT_ExamTrans.get(),
                            self.PLT_FeedingP.get(),

                        ))
                        self.con.commit()
                    """


                    messagebox.showinfo("Success","Recod Added Successfully",parent=self.root)
                    self.Clear()
                    self.Show()


        except Exception as ex:
            messagebox.showerror("error",f"Error due to: {str(ex)}",parent=self.root)

    def Clear(self):
        self.ReceptNo.set("")
        self.Details.set("")
        self.Date.set("")
        self.Total.set("") 
        self.BF.set("0.00")
        self.SPORTS.set("0.00") 
        self.GPF.set("0.00")
        self.EWP.set("0.00")
        self.ZMSEC.set("0.00")
        self.G7Vac.set("0.00") 
        self.BHole.set("0.00")
        self.ExamTrans.set("0.00") 
        self.FeedingP.set("0.00")

    def Show(self):
       
        try:
           self.cur.execute(f"Select * from {self.Incperiod} ")
           rows=self.cur.fetchall()
           self.IncomeTable.delete(*self.IncomeTable.get_children())
           for row in rows :
               self.IncomeTable.insert('',END, values=row)

        except Exception as ex:
            messagebox.showerror("error",f"Error due to: {str(ex)}",parent=self.root)

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

    def UpdateInc(self):

        try:
            if self.ReceptNo.get() =="" or self.Details.get() =="" or self.Date.get() =="":
                messagebox.showerror("error","Choose Record and Update",parent=self.root)

            else :
                #messagebox.showinfo("Employee","Employee ID is"+ EmpID.get(),parent=MainFrame)
                self.cur.execute(f"Select * from {self.Incperiod} where ReceptNo=?", (self.ReceptNo.get(), ))
                row = self.cur.fetchone()
                if row == None :
                    messagebox.showerror("error","Record not Found!!! check-Again Recipt Number",parent=self.root)
                else :

                    Total_Inc= float(self.BF.get() )+ float(self.SPORTS.get())+ float(self.GPF.get())+ float(self.EWP.get())+ float(self.ZMSEC.get())+ float(self.G7Vac.get())+ float(self.BHole.get())+ float(self.ExamTrans.get())+ float(self.FeedingP.get())
                    self.Total.set(Total_Inc) 
                    self.cur.execute(f"Update  {self.Incperiod} set Details=?, Date=? , Total=? , BF=? , SPORTS=? , GPF=? , EWP=? , ZMSEC=? , G7Vac=? , BHole=? , ExamTrans=? , FeedingP=?  where ReceptNo=?", (
                                    
                                    
                                    self.Details.get(),
                                    self.Date.get(),
                                    Total_Inc, 
                                    self.BF.get(),
                                    self.SPORTS.get(), 
                                    self.GPF.get(),
                                    self.EWP.get(),
                                    self.ZMSEC.get(),
                                    self.G7Vac.get(), 
                                    self.BHole.get(),
                                    self.ExamTrans.get(), 
                                    self.FeedingP.get(),
                                    self.ReceptNo.get(),

                        ))
                    self.con.commit()
                    messagebox.showinfo("Record Update","Record Updated Successfully",parent=self.root)
                    self.Show()


        except Exception as ex:
            messagebox.showerror("error",f"Errordue to: {str(ex)}",parent=self.root)

    def DeleteRecord(self):

        try:
            if self.ReceptNo.get() =="" or self.Details.get() =="" or self.Date.get() =="":
                messagebox.showerror("error","Choose Record to Delete",parent=self.root)

            else :
                self.cur.execute(f"Select * from {self.Incperiod} where ReceptNo=?", (self.ReceptNo.get(), ))
                row = self.cur.fetchone()
                if row == None :
                    messagebox.showerror("error","Record not Found!!! check-Again Recipt Number",parent=self.root)

                else :
                    option=messagebox.askyesno("Confirm", "Are you sure you want to Delete this Record",parent=self.root)
                    if option==True:    
                        self.cur.execute(f" Delete from {self.Incperiod} where ReceptNo=?", (self.ReceptNo.get(), ))
                        self.con.commit()
                        messagebox.showinfo("Delete Record","Record Deleted Successfully",parent=self.root)
                        self.Clear()
                        self.Show()

        except Exception as ex:
            messagebox.showerror("error",f"Errordue to: {str(ex)}",parent=self.root)




if __name__== "__main__":
    root=Tk()
    obj=CupdateINC(root)
    root.mainloop()

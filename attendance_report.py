# import re
import re
from sys import path
from tkinter import*
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import threading
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog
import tkinter as tk
from tktimepicker import AnalogPicker, AnalogThemes, SpinTimePickerModern, constants
import openpyxl
import pyodbc
# create a new workbook and select the active worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active
#Global variable for importCsv Function 
mydata=[]
mydata2=[]
class Attendance:
    alive=False
    def destroy(self):
        # Restore the attribute on close.
        self.__class__.alive = False
        return super().destroy()
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Attendance Pannel")
        self.__class__.alive = True

        #-----------Variables-------------------
        self.var_select_filename=StringVar()
        self.var_select_data=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()
        self.var_dep=StringVar()

# first header image  
        img=Image.open(r"C:\Users\Mubashir\Downloads\back.jpg")
        img=img.resize((1920,1080),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1920,height=1080)

        # backgorund image 
        bg1=Image.open(r"C:\Users\Mubashir\Downloads\back.jpg")
        bg1=bg1.resize((1920,1080),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1920,height=1080)


        #title section
              #========================Section Creating==================================

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=0,y=0,width=1920,height=1080)

        title_lb1 = Label(main_frame,text="Welcome to Attendance Pannel",font=("verdana",50,"bold"),bg="white",fg="#002B53")
        title_lb1.place(x=-180,y=0,width=1920,height=100)


        # Left Label Frame 
        #left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Details",font=("verdana",12,"bold"),fg="#002B53")
        #left_frame.place(x=0,y=85,width=1980,height=80)

        

        # ==================================Text boxes and Combo Boxes====================

        #Student id
        #studentId_label = Label(left_frame,text="Emp-ID:",font=("verdana",12,"bold"),fg="#002B53",bg="white")
        #studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        #def id_validation():
        #    name=self.var_id.get()
        
        #    regex="^(?:-(?:[1-9](?:\\d{0,2}(?:,\\d{3})+|\\d*))|(?:0|(?:[1-9](?:\\d{0,2}(?:,\\d{3})+|\\d*))))(?:.\\d+|)$"
        #    if len(name) == 0:
        #        msg = 'name can\'t be empty'
        #    else:
        #        try:
        #            if name.isnumeric():
        #                print("done") 
        #            else:
        #                msg = 'Employee Id can\'t be Alphanumeric '
        #                messagebox.showerror('Incorrect ID', msg,parent=self.root)
        #                studentId_entry.delete(0,END)
        #                print("Gazab")
        #        except Exception as ep:
        #            messagebox.showerror('error', ep,parent=self.root)
             
        #    return True
        #studentId_entry = ttk.Entry(left_frame,textvariable=self.var_id,width=15,font=("verdana",12,"bold"),validate='focusout',validatecommand=id_validation)
        ##studentId_entry.configure(state='normal')
        #studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Department
        #dep_label = Label(left_frame,text="Department:",font=("verdana",12,"bold"),fg="#002B53",bg="white")
        #dep_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        #dep_combo=ttk.Combobox(left_frame,textvariable=self.var_dep,width=13,font=("verdana",12,"bold"),state="readonly")
        #dep_combo["values"]=("CS","Software","IT","Cyber")
        #dep_combo.current(0)
        #dep_combo.grid(row=0,column=3,padx=5,pady=5,sticky=W)
        #Student Roll
        #student_roll_label = Label(left_frame,text="Department:",font=("verdana",12,"bold"),fg="#002B53",bg="white")
        #student_roll_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        #student_roll_entry = ttk.Entry(left_frame,textvariable=self.var_dep,width=15,font=("verdana",12,"bold"))
        #student_roll_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #Studnet Name
        #student_name_label = Label(left_frame,text="Emp-Name:",font=("verdana",12,"bold"),fg="#002B53",bg="white")
        #student_name_label.grid(row=0,column=4,padx=5,pady=5,sticky=W)

        #def name_validation():
        #    name=self.var_name.get()
        #    print("najndjnjsn",name)
        #    msg = ''

        #    if len(name) == 0:
        #        msg = 'name can\'t be empty'
        #    else:
        #        try:
        #            if any(ch.isdigit() for ch in name):
        #                msg = 'Name can\'t have numbers'
        #                messagebox.showerror('Incorrect Employee Name', msg,parent=self.root)
        #                student_name_entry.delete(0,END)
        #            elif len(name) <= 2:
        #                msg = 'name is too short.'
        #                messagebox.showerror('Incorrect Employee Name', msg,parent=self.root)
        #                student_name_entry.delete(0,END)
        #            elif len(name) > 100:
        #                msg = 'name is too long.'
        #               messagebox.showerror('Incorrect Employee Name', msg,parent=self.root)
        #                student_name_entry.delete(0,END)
        #            else:
        #                msg = ''
        #        except Exception as ep:
        #            messagebox.showerror('error', ep,parent=self.root)
        #    return True


        #student_name_entry = ttk.Entry(left_frame,textvariable=self.var_name,width=15,font=("verdana",12,"bold"),validate='focusout',validatecommand=name_validation)
        #student_name_entry.grid(row=0,column=5,padx=5,pady=5,sticky=W)

        #Department
        # dep_label = Label(left_frame,text="Department:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        # dep_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        # dep_entry = ttk.Entry(left_frame,textvariable=self.var_dep,width=15,font=("verdana",12,"bold"))
        # dep_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #time
        #time_label = Label(left_frame,text="Time:",font=("verdana",12,"bold"),fg="#002B53",bg="white")
        #time_label.grid(row=0,column=6,padx=5,pady=5,sticky=W)

       
        #def set_time():  
        #    now=datetime.now()
        #    current_time = now.strftime("%H:%M:%S")
        #    time_entry.insert(0,current_time)

        #    time=self.var_time.get()
        #    format= '%H:%M:%S'
        #    try:
        #        datetime.strptime(time, format)
        #    except ValueError:
        #        messagebox.showerror('Incorrect Time Format', 'Use Correct Time Format H:M:S',parent=self.root)
        #        time_entry.delete(0,END)
        #        now=datetime.now()
        #        current_time = now.strftime("%H:%M:%S")
        #        time_entry.insert(0,current_time)
        

        #    return True



        
        #time_entry = ttk.Entry(left_frame,textvariable=self.var_time,width=15,font=("verdana",12,"bold"),validate='focusout',validatecommand=set_time)
        #time_entry.grid(row=0,column=7,padx=5,pady=5,sticky=W)

        #Date 
        #date_label = Label(left_frame,text="Date:",font=("verdana",12,"bold"),fg="#002B53",bg="white")
        #date_label.grid(row=0,column=8,padx=5,pady=5,sticky=W)
        


        #def strftime_format():
        #    date=self.var_date.get()
        #    format= '%d/%m/%Y'
        #    try:
        #        datetime.strptime(date, format)
        #    except ValueError:
        #        messagebox.showerror('Incorrect Date Format', 'Use Correct Date Format dd/mm/yyyy',parent=self.root)
        #        date_entry.delete(0,END)
        

        #    return True

        #date_entry = ttk.Entry(left_frame,textvariable=self.var_date,width=15,font=("verdana",12,"bold"),validate='focusout',validatecommand=strftime_format)
        #date_entry.grid(row=0,column=9,padx=5,pady=5,sticky=W)

        #Attendance
        #student_attend_label = Label(left_frame,text="Attend-status:",font=("verdana",12,"bold"),fg="#002B53",bg="white")
        #student_attend_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        #attend_combo=ttk.Combobox(left_frame,textvariable=self.var_attend,width=13,font=("verdana",12,"bold"),state="readonly")
        #attend_combo["values"]=("Status","Present","Absent")
        #attend_combo.current(0)
        #attend_combo.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        

        


        # Right section=======================================================

        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Attendance Details",font=("verdana",12,"bold"),fg="#002B53")
        right_frame.place(x=0,y=100,width=1920,height=750)


        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=20,width=1500,height=600)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport = ttk.Treeview(table_frame,column=("ID","Dep","Name","Time","Date","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        self.attendanceReport.heading("ID",text="Emp-ID")
        self.attendanceReport.heading("Dep",text="Department")
        self.attendanceReport.heading("Name",text="Emp-Name")
        self.attendanceReport.heading("Time",text="Time")
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.heading("Attend",text="Attend-status")
        

        self.attendanceReport["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport.column("ID",width=100)
        self.attendanceReport.column("Dep",width=100)
        self.attendanceReport.column("Name",width=100)
        self.attendanceReport.column("Time",width=100)
        self.attendanceReport.column("Date",width=100)
        self.attendanceReport.column("Attend",width=100)
        
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor_right)
        self.fetch_data()
    # =================================update for mysql button================
        #right_btn_frame = Frame(main_frame,bd=2,bg="white",relief=RIDGE)
        #right_btn_frame.place(x=0,y=680,width=1920,height=90)
    #Update button
        del_btn=Button(main_frame,command=self.export_csv,text="Export CSV",width=12,font=("verdana",12,"bold"),fg="white",bg="#002B53")
        del_btn.place(x=700,y=740,height=30,width=110)
    #Update button
        #del_btn=Button(main_frame,command=self.delete_data,text="Delete",width=12,font=("verdana",12,"bold"),fg="white",bg="#002B53")
        #del_btn.place(x=770,y=740,height=30,width=100)
    
    # ===============================update function for mysql database=================
    def export_csv(self):
                        self.root2=Toplevel()
                        self.root2.title("Export Attendance")
                        self.root2.geometry("400x400+570+220")
                        l=Label(self.root2,text="Export Attendance Report",font=("times new roman",20,"bold"),fg="#002B53",bg="#fff")
                        l.place(x=0,y=15,relwidth=1)
                        # -------------------fields-------------------
                        #label1 
                        ssq =lb1= Label(self.root2,text="Enter File Name",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                        ssq.place(x=70,y=90)
                        
                        def validate_file():
                            email = self.var_select_data.get()
                            regx=" "
                            print("helloo",email)
                            msg = ''

                            if len(email) == 0:
                                msg = 'Email can\'t be empty'
                            else:
                                try:
                                    if(re.fullmatch(regx, email)):

                                        msg=''
                                    else:
                                        messagebox.showerror('Incorrect Date Format', 'Write Date in Correct Format dd/mm/yyyy',parent=self.root2)
                                        self.txtpwd.delete(0,END)
                                except Exception as ep:
                                    messagebox.showerror('error', ep,parent=self.root2)
                                
                            
                            return True
                        self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_select_filename,font=("times new roman",15,"bold"))
                        self.txtpwd.place(x=70,y=120,width=270)


                        #label2 
                        sa =lb1= Label(self.root2,text="Select Date",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                        sa.place(x=70,y=170)
                        def validate_email():
                            email = self.var_select_data.get()
                            regx="^(0[1-9]|[12][0-9]|3[01])[/](0[1-9]|1[012])[/](19|20)\d\d$"
                            print("helloo",email)
                            msg = ''

                            if len(email) == 0:
                                msg = 'Email can\'t be empty'
                            else:
                                try:
                                    if(re.fullmatch(regx, email)):

                                        msg=''
                                    else:
                                        messagebox.showerror('Incorrect Date Format', 'Write Date in Correct Format dd/mm/yyyy',parent=self.root2)
                                        self.txtpwd_2.delete(0,END)
                                except Exception as ep:
                                    messagebox.showerror('error', ep,parent=self.root2)
                                
                            
                            return True
                        def delete_date(e):
                            self.txtpwd_2.delete(0,END)
                        self.txtpwd_2=DateEntry(self.root2,textvariable=self.var_select_data,font=("times new roman",15,"bold"),date_pattern="dd/mm/yyyy")
                        #self.txtpwd_2.insert(0,"dd/mm/yyyy")
                        #self.txtpwd_2.bind("<FocusIn>",delete_date)
                        self.txtpwd_2.place(x=70,y=210,width=270)
                        

                        loginbtn=Button(self.root2,command=self.submit,text="Submit",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#002B53",borderwidth=1)
                        loginbtn.place(x=160,y=270,width=80,height=30)

                        #entry2 
                        
       # if self.var_id.get()=="" or self.var_name.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
        #    messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        #else:
         #   try:
                        #Update=messagebox.askyesno("Update","Do you want to Update this Student Attendance!",parent=self.root)
                        
          #  except Exception as es:
           #     messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    def submit(self):  
                    if self.var_select_data.get()=='' or self.var_select_filename.get()=='':
                            messagebox.showerror("Error","Enter Filename and Date",parent=self.root2)
                            
                    else:        
                            

                            conn = mysql.connector.connect(username='root', password='root',host='localhost',database='employee_management')
                            mycursor = conn.cursor()
                            mycursor.execute("select * from employee_attendance where emp_date='" +self.var_select_data.get()+ "'")
                            df=mycursor.fetchall()
                            if len(df)==0:
                                 messagebox.showerror("Record Not Found","Attendance Not Found!",parent=self.root2)
        
                            else:
                                print("data",df)
                                for row, record in enumerate(df, start=1):
                                    for col, value in enumerate(record, start=1):
                                        cell = worksheet.cell(row=row, column=col)
                                        cell.value = value
            # save the Excel file
                                extension='.xlsx'
                                search=str(self.var_select_filename.get())
                                name='D:\\Bushi\\Employees Face Recognition System\\attendance\\'+search
                                file=name+extension
                                workbook.save(file)
                                
                            #df.to_excel('ds.xls')
                                messagebox.showinfo("Success","Successfully Exported Attendance!",parent=self.root2)
                            
                                print("here")
                                conn.commit()
                            
                                conn.close()
                                self.fetch_data()
                                self.root2.destroy()
                                self.root.destroy()
                                
    def update_data(self):
        if self.var_id.get()=="" or self.var_name.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Attendance!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='root',host='localhost',database='employee_management')
                    mycursor = conn.cursor()
                    mycursor.execute("update employee_attendance set emp_dep=%s,emp_name=%s,emp_time=%s,emp_date=%s,emp_status=%s where emp_id=%s", (
                                                                                                                                                                              
                                                                                                                                                                    
                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                            self.var_time.get(),
                                                                                                                                                                            
                                                                                                                                                                            self.var_attend.get(),
                                                                                                                                                                            self.var_date.get(),
                                                                                                                                                                            self.var_id.get() 
                                                                                                                                                                              ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    # =============================Delete Attendance form my sql============================
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='root',host='localhost',database='employee_management')
                    mycursor = conn.cursor() 
                    sql="delete from employee_attendance where emp_id=%s"
                    val=(self.var_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)  
    # ===========================fatch data form mysql attendance===========

    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='root',host='localhost',database='employee_management')
        mycursor = conn.cursor()

        mycursor.execute("select * from employee_attendance")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.attendanceReport.delete(*self.attendanceReport.get_children())
            for i in data:
                self.attendanceReport.insert("",END,values=i)
            conn.commit()
        conn.close()

    #============================Reset Data======================
    def reset_data(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_dep.set("")
        self.var_attend.set("Status")

    # =========================Fetch Data Import data ===============

    def fetchData(self,rows):
        global mydata
        mydata = rows
        self.attendanceReport_left.delete(*self.attendanceReport_left.get_children())
        for i in rows:
            self.attendanceReport_left.insert("",END,values=i)
            print(i)

    def fetchData2(self,rows):
        global mydata2
        mydata2 = rows
        self.attendanceReport.delete(*self.attendanceReport.get_children())
        for i in rows:
            self.attendanceReport.insert("",END,values=i)
            print(i)    

    def importCsv(self):
        global mydata
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            

    #==================Experot CSV=============
    def exportCsv(self):
        try:
            print("my data values",mydata)
            if len(mydata2)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata2:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Export Data Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

    #=============Cursur Function for CSV========================

    def get_cursor_left(self,event=""):
        cursor_focus = self.attendanceReport_left.focus()
        content = self.attendanceReport_left.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_dep.set(data[1]),
        self.var_name.set(data[2]),
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_attend.set(data[5]) 

     #=============Cursur Function for mysql========================

    def get_cursor_right(self,event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_dep.set(data[1]),
        self.var_name.set(data[2]),
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_attend.set(data[5])   
    #=========================================Update CSV============================

    # export upadte
    def action(self):
        if self.var_id.get()=="" or self.var_name.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='root',host='localhost',database='employee_management')
                mycursor = conn.cursor()
                mycursor.execute("insert into employee_attendance values(%s,%s,%s,%s,%s,%s)",(
                self.var_id.get(),
                self.var_dep.get(),
                self.var_name.get(),
                self.var_time.get(),
                self.var_date.get(),
                self.var_attend.get()
                
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved in Database!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)






    #     conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
    #     mycursor = conn.cursor()
    #     if messagebox.askyesno("Confirmation","Are you sure you want to save attendance on database?"):
    #         for i in mydata:
    #             uid = i[0]
    #             uroll = i[1]
    #             uname = i[2]
    #             utime = i[3]
    #             udate = i[4]
    #             uattend = i[5]
    #             qury = "INSERT INTO stdattendance(std_id, std_roll_no, std_name, std_time, std_date, std_attendance) VALUES(%s,%s,%s,%s,%s,%s)"
    #             mycursor.execute(qury,(uid,uroll,uname,utime,udate,uattend))
    #         conn.commit()
    #         conn.close()
    #         messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
    #     else:
    #         return False




        # 









if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
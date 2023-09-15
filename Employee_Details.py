from tkinter import*# create gui in pythom
from tkinter import ttk# stylish toolkit
from PIL import Image,ImageTk# to import images in python
from tkinter import messagebox
#import customtkinter
import mysql.connector 
import pandas as pd
from tqdm import tqdm
from tkcalendar import Calendar, DateEntry
import re
import os
import cv2 as cv
import tkinter as tk

class employee_details:
    alive=False
    def destroy(self):
        # Restore the attribute on close.
        self.__class__.alive = False
        return super().destroy()
    def __init__(self,root ):#constructor #root name of window
        self.root=root
        self.root.geometry("1920x1080+0+0")#0+0Position of window on x and y axis
        self.root.title('Employee Details') 
        self.__class__.alive = True
        #title_label=Label(text="Employee Management System",font=("time new roman",50,'italic','bold'),bg='black',fg='white')
        #title_label.place(x=-200,y=0,width=1920,height=100)
        
        ## variables to store data
        self.var_empid=StringVar()
        self.var_cnic=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_phone_no=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_martial_status=StringVar()
        self.var_job_title=StringVar()
        self.var_dob=StringVar()
        self.var_department=StringVar()
        self.var_hire_date=StringVar()
        self.var_salary=StringVar()
        self.var_address=StringVar()
        self.var_manager_id=StringVar()
        self.var_radiobtn1=StringVar()
        self.var_radiobtn2=StringVar()

        #img=Image.open(r"C:\Users\Mubashir\Downloads\back.jpg")
        #img=img.resize((1920,1080),Image.LANCZOS)
        #self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        #f_lb1 = Label(self.root,image=self.photoimg)
        #f_lb1.place(x=0,y=0,width=1920,height=1080)

        # backgorund image 
        #bg1=Image.open(r"C:\Users\Mubashir\Downloads\back.jpg")
        #bg1=bg1.resize((1920,1080),Image.LANCZOS)
        #self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root)
        bg_img.place(x=0,y=0,width=1920,height=1080)

        #main frame
        main_frame=Frame(bg_img,bd=2)#bd=2 2 boders
        main_frame.place(x=0,y=0,width=1920,height=1080)

        title_label=Label(main_frame,text="Employee Management System",font=("time new roman",50,'italic'),bg="#002B53", fg='white')
        title_label.place(x=-180,y=0,width=1920,height=100)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Employee Details',font=("time new roman",10,'italic','bold'),fg="#002B53")
        left_frame.place(x=0,y=100,width=780,height=660)
        root.option_add('*TCombobox*Listbox.foreground' % left_frame,"#002B53")
            

        
        #Employee Id label
        employee_id_label=Label(left_frame,text="Employee ID:*",font=("time new roman",10,'italic','bold'),bg='white',fg="#002B53")
        employee_id_label.grid(row=0,column=0,padx=2,pady=10)
       
        def id_validation():
            name=self.var_empid.get()
            

        
            regex="^(?:-(?:[1-9](?:\\d{0,2}(?:,\\d{3})+|\\d*))|(?:0|(?:[1-9](?:\\d{0,2}(?:,\\d{3})+|\\d*))))(?:.\\d+|)$"
            if len(name) == 0:
                msg = 'name can\'t be empty'
            else:
                try:
                    if name.isnumeric():
                        print("done") 
                    
                    else:
                        msg = 'Employee Id can\'t be Alphanumeric '
                        messagebox.showerror('Incorrect ID', msg,parent=self.root)
                        employee_id_entry.delete(0,END)
                        print("Gazab")
                except Exception as ep:
                    messagebox.showerror('error', ep,parent=self.root)
             
            return True
        #Employee Id Entry
        employee_id_entry=Entry(left_frame,textvariable=self.var_empid,width=20,font=("time new roman",10,'italic','bold'),validate='focusout',validatecommand=id_validation)
        employee_id_entry.grid(row=0,column=1,padx=2,pady=10)
        #Employee CNIC label
        employee_cnic_label=Label(left_frame,text="CNIC:*",font=("time new roman",10,'italic','bold'),bg='white',fg="#002B53")
        employee_cnic_label.grid(row=0,column=2,padx=2,pady=10)

        def cnic_validation():
            name=self.var_cnic.get()
        
            regex="^[0-9]{5}-[0-9]{7}-[0-9]$"
            if len(name) == 0:
                msg = 'name can\'t be empty'
            else:
                try:
                    if re.match(regex,name):
               
                        print("done") 
                    else:
                        msg = 'Correct Format xxxxx-xxxxxxx-x'
                        
                        messagebox.showerror('Incorrect CNIC Format', msg,parent=self.root)
                        employee_cnic_entry.delete(0,END)
                    
                        
                        print("Gazab")
                except Exception as ep:
                    messagebox.showerror('error', ep,parent=self.root)
             
            return True
       
        #Employee CNIC Entry
        def delete_cnic(e):
            employee_cnic_entry.delete(0,END)
        employee_cnic_entry=Entry(left_frame,textvariable=self.var_cnic,width=20,font=("time new roman",10,'italic','bold'),validate='focusout',validatecommand=cnic_validation)
        employee_cnic_entry.insert(0,"32102-1010248-4")
        employee_cnic_entry.bind("<FocusIn>",delete_cnic)
        employee_cnic_entry.grid(row=0,column=3,padx=2,pady=10)


        #Employee Name label
        employee_name_label=Label(left_frame,text="Employee Name:*",font=("time new roman",10,'italic','bold'),bg='white',fg="#002B53")
        employee_name_label.grid(row=1,column=0,padx=2,pady=10)
        def name_validation():
            name=self.var_name.get()
            print("najndjnjsn",name)
            msg = ''

            if len(name) == 0:
                msg = 'name can\'t be empty'
            else:
                try:
                    if any(ch.isdigit() for ch in name):
                        msg = 'Name can\'t have numbers'
                        messagebox.showerror('Incorrect Employee Name', msg,parent=self.root)
                        self.employee_name_entry.delete(0,END)
                    elif len(name) <= 2:
                        msg = 'name is too short.'
                        messagebox.showerror('Incorrect Employee Name', msg,parent=self.root)
                        self.employee_name_entry.delete(0,END)
                    elif len(name) > 100:
                        msg = 'name is too long.'
                        messagebox.showerror('Incorrect Employee Name', msg,parent=self.root)
                        self.employee_name_entry.delete(0,END)
                    else:
                        msg = ''
                except Exception as ep:
                    messagebox.showerror('error', ep,parent=self.root)
            return True
        
        #Employee Name Entry
        self.employee_name_entry=Entry(left_frame,textvariable=self.var_name,width=20,font=("time new roman",10,'italic','bold'),validate='focusout',validatecommand=name_validation)
        self.employee_name_entry.grid(row=1,column=1,padx=2,pady=10)
        #Employee dob label
        employee_dob_label=Label(left_frame,text="DOB:*",font=("time new roman",10,'italic','bold'),bg='white',fg="#002B53")
        employee_dob_label.grid(row=1,column=2,padx=2,pady=10)
        #Employee dob Entry
       


        employee_dob_entry=DateEntry(left_frame,textvariable=self.var_dob,width=17,font=("time new roman",10,'italic','bold'),date_pattern="dd/mm/yyyy")
        employee_dob_entry.grid(row=1,column=3,padx=2,pady=10)
        
        #Employee phone_no label
        employee_phone_no_label=Label(left_frame,text="Phone No:*",font=("time new roman",10,'italic','bold'),bg='white',fg="#002B53")
        employee_phone_no_label.grid(row=2,column=0,padx=2,pady=10)
        #Employee phone_no Entry
        def validate_contact():
            passwd = self.var_phone_no.get()
            regex = "^((\+92)?(0092)?(92)?(0)?)(3)([0-9]{9})$"

            pat = re.compile(regex)
            mat = re.search(pat, passwd)
            
            # validating conditions
            if self.var_phone_no.get() == '':
                print('')
            else:
                if mat:
                    print("")
                else:
                    messagebox.showerror('Incorrect Contact', 'Write Correct Phone Number like 03157784521',parent=self.root)
                    employee_phone_no_entry.delete(0,END)
                
            return True
        def delete_num(e):
            employee_phone_no_entry.delete(0,END)
        employee_phone_no_entry=Entry(left_frame,textvariable=self.var_phone_no,width=20,font=("time new roman",10,'italic','bold'),validate='focusout',validatecommand=validate_contact)
        employee_phone_no_entry.insert(0,"03495412154")
        employee_phone_no_entry.bind("<FocusIn>",delete_num)
        employee_phone_no_entry.grid(row=2,column=1,padx=2,pady=10)
        #Employee email label
        employee_email_label=Label(left_frame,text="Email:*",font=("time new roman",10,'italic','bold'),bg='white',fg="#002B53")
        employee_email_label.grid(row=2,column=2,padx=2,pady=10)
        #Employee email Entry
        def validate_email():
            email = self.var_email.get()
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            print("helloo",email)
            msg = ''

            if len(email) == 0:
                msg = 'Email can\'t be empty'
            else:
                try:
                    if(re.fullmatch(regex, email)):

                        msg=''
                    else:
                        messagebox.showerror('Incorrect Email Format', 'Write Email in Correct Format ',parent=self.root)
                        employee_email_entry.delete(0,END)
                except Exception as ep:
                    messagebox.showerror('error', ep,parent=self.root)
                
            
            return True
        employee_email_entry=Entry(left_frame,textvariable=self.var_email,width=20,font=("time new roman",10,'italic','bold'),validate='focusout',validatecommand=validate_email)
        employee_email_entry.grid(row=2,column=3,padx=2,pady=10)

        #gender label
        gender_label=Label(left_frame,text="Gender:*",font=("time new roman",10,'italic','bold'),bg='white',fg="#002B53")
        gender_label.grid(row=3,column=0,padx=2,pady=10)
        #gender combobox
        gender_combo=ttk.Combobox(left_frame,textvariable=self.var_gender,font=("time new roman",10,'italic','bold'),width=17,state='readonly')
        gender_combo['values']=('Male','Female','Other')
        gender_combo.current(0) 
        gender_combo.grid(row=3,column=1,padx=2,pady=10)
        #martial_status label
        martial_status_label=Label(left_frame,text="Martial Status:*",font=("time new roman",10,'italic','bold'),bg='white',fg="#002B53")
        martial_status_label.grid(row=3,column=2,padx=2,pady=10)
        #martial_status combobox
        martial_status_combo=ttk.Combobox(left_frame,textvariable=self.var_martial_status,font=("time new roman",10,'italic','bold'),width=17,state="readonly")
        martial_status_combo['values']=('Single','Married')
        martial_status_combo.current(0) 
        martial_status_combo.grid(row=3,column=3,padx=2,pady=10)
        #job_title label
        job_title_label=Label(left_frame,text="Job Title:*",font=("time new roman",10,'italic','bold'),bg='white',fg="#002B53")
        job_title_label.grid(row=4,column=0,padx=2,pady=10)
        #job_title combobox
        job_title_combo=ttk.Combobox(left_frame,textvariable=self.var_job_title,font=("time new roman",10,'italic','bold'),width=17,state='readonly')
        job_title_combo['values']=('Business Analyst','Data Scientist/Analyst','Machine Learning Engineer','AIDeveloper')
        job_title_combo.current(0) 
        job_title_combo.grid(row=4,column=1,padx=2,pady=10)
        #department label
        department_label=Label(left_frame,text="Department:*",font=("time new roman",10,'italic','bold'),bg='white',fg="#002B53")
        department_label.grid(row=4,column=2,padx=2,pady=10)
        #department combobox
        department_combo=ttk.Combobox(left_frame,textvariable=self.var_department,font=("time new roman",10,'italic','bold'),width=17,state='readonly')
        department_combo['values']=('Computer Science','Software Engineering','Information Technology','Cyber Technology')
        department_combo.current(0) 
        department_combo.grid(row=4,column=3,padx=2,pady=10)

        #hire_date label
        #hire_date_label=Label(left_frame,text="Hire Date:",font=("time new roman",10,'italic','bold'),bg='white',fg="#002B53")
        #hire_date_label.grid(row=5,column=0,padx=2,pady=10)
        #hire_date Entry
        #hire_date_entry=Entry(left_frame,textvariable=self.var_hire_date,width=20,font=("time new roman",10,'italic','bold'))
        #hire_date_entry.grid(row=5,column=1,padx=2,pady=10)
        #salary label
        salary_label=Label(left_frame,text="Salary:*",font=("time new roman",10,'italic','bold'),bg='white',fg="#002B53")
        salary_label.grid(row=5,column=2,padx=2,pady=10)
        #salary Entry
        def validate_salary():
            sal = self.var_salary.get()
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            print("helloo",sal)
            msg = ''

            if len(sal) == 0:
                msg = 'Salary can\'t be empty'
            else:
                try:
                    
                    
                    if all(ch.isdigit() for ch in sal):
                        print("hey")
                        msg="Salary can\'t have digits"
                        #messagebox.showerror('Incorrect Salary', msg,parent=self.root)
                        #salary_entry.delete(0,END)
                    else:
                  
                                msg="Incorrect Salary"
                                messagebox.showerror('Incorrect Salary', msg,parent=self.root)
                                salary_entry.delete(0,END)
                       
                            
                except Exception as ep:
                    messagebox.showerror('error', ep,parent=self.root)
                
            
            return True
        salary_entry=Entry(left_frame,textvariable=self.var_salary,width=20,font=("time new roman",10,'italic','bold'),validate='focusout',validatecommand=validate_salary)
        salary_entry.grid(row=5,column=3,padx=2,pady=10)

        #address label
        address_label=Label(left_frame,text="Address:*",font=("time new roman",10,'italic','bold'),bg='white',fg="#002B53")
        
        #row=6,column=0,padx=2,pady=10
        address_label.grid(row=5,column=0,padx=2,pady=10)
        #address Entry
        #row=6,column=1,padx=2,pady=10
        address_entry=Entry(left_frame,textvariable=self.var_address,width=20,font=("time new roman",10,'italic','bold'))
        address_entry.grid(row=5,column=1,padx=2,pady=10)
        #manager_id label
        #manager_id_label=Label(left_frame,text="Manager Id:",font=("time new roman",10,'italic','bold'),bg='white',fg="#002B53")
        #manager_id_label.grid(row=6,column=2,padx=2,pady=10)
        #manager_id Entry
        #manager_id_entry=Entry(left_frame,textvariable=self.var_manager_id,width=20,font=("time new roman",10,'italic','bold'))
        #manager_id_entry.grid(row=6,column=3,padx=2,pady=10)

        #Radio Buttons
        #radiobtn1=ttk.Radiobutton(left_frame,variable=self.var_radiobtn1,text='take photo sample',value='yes')
        #radiobtn1.grid(row=7,column=0,padx=2,pady=10)
        #radiobtn2=ttk.Radiobutton(left_frame,variable=self.var_radiobtn1,text='not photo sample',value='no')
        #radiobtn2.grid(row=7,column=1,padx=2,pady=10)

        #Save Button 
        savebtn=Button(left_frame,width=20,command=self.add_data,text="Save",font=("time new roman",10,'italic','bold'),fg='white',bg="#002B53")
        savebtn.grid(row=8,column=0,padx=2,pady=10)
        #Update Button 
        updatebtn=Button(left_frame,command=self.update_data,width=20,text="Update",font=("time new roman",10,'italic','bold'),fg='white',bg="#002B53")
        updatebtn.grid(row=8,column=1,padx=2,pady=10)
        # Delete Button 
        deletebtn=Button(left_frame,command=self.delete_data,width=20,text="Delete",font=("time new roman",10,'italic','bold'),fg='white',bg="#002B53")
        deletebtn.grid(row=8,column=2,padx=2,pady=10)
        #Reset Button 
        resetbtn=Button(left_frame,command=self.reset,width=18,text="Reset",font=("time new roman",10,'italic','bold'),fg='white',bg="#002B53")
        resetbtn.grid(row=8,column=3,padx=2,pady=10)

        # #photo frame
        # photo_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,font=("time new roman",10,'italic','bold'))
        # photo_frame.place(x=3,y=390,width=677,height=30)
        #take photo sample Button 
        take_photo_samplebtn=Button(left_frame,command=self.generate_dataset,width=20, text="Take Photo Sample",font=("time new roman",10,'italic','bold'),fg='white',bg="#002B53")
        take_photo_samplebtn.place(x=260,y=300,width=180,height=30)
        #update photo sample Button
        #update_photo_samplebtn=Button(left_frame,text="Update Photo Sample",width=20,font=("time new roman",10,'italic','bold'),fg='white',bg="#002B53")
        #update_photo_samplebtn.grid(row=9,column=2,padx=2,pady=10)



        #right frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Employee Details',font=("time new roman",10,'italic','bold'),fg="#002B53")
        right_frame.place(x=780,y=100,width=780,height=660)

        #Search label
        self.var_search=StringVar()
        search_label=Label(right_frame,text="Search By",font=("time new roman",10,'italic','bold'),bg="#002B53",fg='white')
        search_label.grid(row=0,column=0,padx=2,pady=10)
        #Search combobox
        self.var_searchTX=StringVar()
        search_combo=ttk.Combobox(right_frame,textvariable=self.var_searchTX,font=("time new roman",10,'italic','bold'),width=17,state='readonly')
        search_combo['values']=('Select','Employee ID')
        search_combo.current(0) 
        search_combo.grid(row=0,column=1,padx=2,pady=10)
        #Search EntryFill
        search_entry=Entry(right_frame,textvariable=self.var_search,width=20,font=("time new roman",10,'italic','bold'))
        search_entry.grid(row=0,column=2,padx=2,pady=10)
        #Searach Button
        searchbtn=Button(right_frame,text="Search",command=self.search_data,font=("time new roman",10,'italic','bold'),fg='white',bg="#002B53")
        searchbtn.grid(row=0,column=3,padx=2,pady=10)
        #Showall Button
        showallbtn=Button(right_frame,text="Show All",command=self.fetch_data,font=("time new roman",10,'italic','bold'),fg='white',bg="#002B53")
        showallbtn.grid(row=0,column=4,padx=2,pady=10)

        #Table frame
        table_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,font=("time new roman",10,'italic','bold'))
        table_frame.place(x=3,y=40,width=720,height=600)
        
        #Scrollbars for table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,columns=('employee id','cnic','name','dob','phone no','email','gender',
        'martial_status','job_title','department','salary','address')
        ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('employee id',text="Employee Id") 
        self.employee_table.heading('name',text="CNIC") 
        self.employee_table.heading('cnic',text="Name") 
        self.employee_table.heading('dob',text="DOB") 
        self.employee_table.heading('phone no',text="Phone No") 
        self.employee_table.heading('email',text="Email") 
        self.employee_table.heading('gender',text="Gender") 
        self.employee_table.heading('martial_status',text="Martial Status") 
        self.employee_table.heading('job_title',text="Job title") 
        self.employee_table.heading('department',text="Department") 
        #self.employee_table.heading('hire_date',text="Hire Date")
        self.employee_table.heading('salary',text="Salary") 
        self.employee_table.heading('address',text="Address") 
       # self.employee_table.heading('manager_id',text="Manager Id") 
        #self.employee_table.heading('photo_sample',text="Photo Sample") 
    

        self.employee_table['show']="headings"

        self.employee_table.column('employee id',width=150) 
        self.employee_table.column('name',width=150) 
        self.employee_table.column('cnic',width=150) 
        self.employee_table.column('email',width=150) 
        self.employee_table.column('dob',width=150) 
        self.employee_table.column('phone no',width=150) 
        self.employee_table.column('email',width=100) 
        self.employee_table.column('gender',width=100) 
        self.employee_table.column('martial_status',width=100) 
        self.employee_table.column('job_title',width=100) 
        self.employee_table.column('department',width=100) 
        #elf.employee_table.column('hire_date',width=100)
        self.employee_table.column('salary',width=100) 
        self.employee_table.column('address',width=100) 
        #self.employee_table.column('manager_id',width=100) 
        #self.employee_table.column('photo_sample',width=100) 
        # self.employee_table['show']="column"

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)#by clicking on data to update data will be place in all entry fills
        self.fetch_data()

    def add_data(self):
        if self.var_empid.get()=="" or self.var_name.get()=="" or self.var_cnic.get()=="" or self.var_dob.get()=="" or self.var_phone_no.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="" or self.var_martial_status.get()=="" or self.var_job_title.get()=="" or self.var_department.get()=="" or self.var_salary.get()==0.0 or self.var_address.get()=="":
            messagebox.showerror("ERROR",'All Fields are required')
        else:
            try:
                conn = mysql.connector.connect(username='root', password='root',host='localhost',database='employee_management')
                my_cursor = conn.cursor()
                        
                sql = "SELECT employee_id,Name,CNIC,DOB,Phone_no,Email,Gender,Martial_Status,Department,Salary,Address,Job_Title FROM employee_data where employee_id='" +self.var_empid.get() + "'" 
                my_cursor.execute(sql)
                        
                        
                #my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    messagebox.showerror('Repeat Record', "Employee ID Already Exist",parent=self.root)
                    self.reset()
                else:
                    con=mysql.connector.connect(host="localhost",username="root",password="root",database="employee_management")
                    my_cursor=con.cursor()
                    my_cursor.execute("insert  into employee_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                        self.var_empid.get(),
                                                                                                                        self.var_name.get(),
                                                                                                                        self.var_cnic.get(),
                                                                                                                        self.var_dob.get(),
                                                                                                                        self.var_phone_no.get(),
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.var_martial_status.get(),
                                                                                                                    
                                                                                                                        self.var_department.get(),
                                                                                                                    #self.var_hire_date.get(),
                                                                                                                        self.var_salary.get(),
                                                                                                                        self.var_address.get(),
                                                                                                                        #self.var_manager_id.get(),
                                                                                                                        #self.var_radiobtn1.get(),
                                                                                                                        self.var_job_title.get()  ))
                    con.commit()
                    self.fetch_data()
                    con.close()
                    messagebox.showinfo("INFO","Data is Save Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    
    #Fetch Data
    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",username="root",password="root",database="employee_management")
        my_cursor=con.cursor()
        my_cursor.execute("select * from employee_data")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)

            con.commit()
        con.close()

    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Enter Select Type and Employee ID",parent=self.root)
        else:
            try:
                if all(ch.isdigit() for ch in self.var_search.get()):
                    conn = mysql.connector.connect(username='root', password='root',host='localhost',database='employee_management')
                    my_cursor = conn.cursor()
                    
                    sql = "SELECT employee_id,Name,CNIC,DOB,Phone_no,Email,Gender,Martial_Status,Department,Salary,Address,Job_Title FROM employee_data where employee_id='" +self.var_search.get() + "'" 
                    my_cursor.execute(sql)
                    
                    
                    # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                    rows=my_cursor.fetchall()       
                    print("rows",len(rows))

                    if len(rows)!=0:
                        self.employee_table.delete(*self.employee_table.get_children())
                        
                        for i in rows:
                            self.employee_table.insert("",END,values=i)
                            conn.commit()

                    if len(rows)==0:
                        self.employee_table.delete(*self.employee_table.get_children())
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        
                        
                    conn.close()
                else:
                    self.employee_table.delete(*self.employee_table.get_children())
                    messagebox.showerror("Error","Data Not Found",parent=self.root)
                
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #Get Cousor to update data
    def get_cursor(self,event=""):
        cursor_focus=self.employee_table.focus()# take focus from table
        content=self.employee_table.item(cursor_focus)
        data=content['values']
        print("valuesssssssss are",data[0])

        self.var_empid.set(data[0])
        id=data[0]
        self.var_name.set(data[1]) 
        name=data[1]    
        self.var_cnic.set(data[2])
        self.var_dob.set(data[3])
        self.var_phone_no.set(data[4])
        self.var_email.set(data[5])
        self.var_gender.set(data[6])
        self.var_martial_status.set(data[7])
        self.var_department.set(data[8])
        
        #self.var_hire_date.set(data[9])
        self.var_salary.set(data[9])
        self.var_address.set(data[10])
        #self.var_manager_id.set(data[12])
        #self.var_radiobtn1.set(data[13])
        
        self.var_job_title.set(data[11])
        print("valuesssssssss are",name)
        return name,id
    def get_cursor_for_update(self,event=""):
        cursor_focus=self.employee_table.focus()# take focus from table
        content=self.employee_table.item(cursor_focus)
        data=content['values']
        id=data[0]
        return id

    
    #update data function 
    def update_data(self):
        check=int(self.var_empid.get())
        id=self.get_cursor_for_update()
        
        
        if self.var_empid.get()=='' or self.var_name.get()=='' or self.var_cnic.get()=='' or self.var_dob.get()=='' or self.var_phone_no.get()=='' or self.var_email.get()=='' or self.var_gender.get()=='' or self.var_martial_status.get()=='' or self.var_job_title.get()=='' or self.var_department.get()=='' or self.var_salary.get()==0.0 or self.var_address.get()=='':
            messagebox.showerror("ERROR",'All Fields are required',parent=self.root)
        else:
            try:
                
      
                
                print("value of id",type(id))
                
                print("second value",type(check))
               
                #print(entry)
                #print(id)
                if(check==id):
                    check=str(check)
                    update=messagebox.askyesno("update","Do you want to Update This employee details",parent=self.root)
                    if update >0:
                
                        con=mysql.connector.connect(host="localhost",username="root",password="root",database="employee_management")
                        my_cursor=con.cursor()       
                        print("values of empid",self.var_empid.get())                                                                                                                                                                                                                                                                                                                                                 
                        my_cursor.execute("update employee_data set Name=%s,CNIC=%s,DOB=%s,Phone_no=%s,Email=%s,Gender=%s,Martial_Status=%s,Job_Title=%s,Department=%s,Salary=%s,Address=%s where employee_id=%s",(
                                                                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                                                                            self.var_cnic.get(),
                                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                                            self.var_phone_no.get(),
                                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                                            self.var_martial_status.get(),
                                                                                                                                                                                                                            self.var_job_title.get(),
                                                                                                                                                                                                                            self.var_department.get(),
                                                                                                                                                                                                                            #self.var_hire_date.get(),
                                                                                                                                                                                                                            self.var_salary.get(),
                                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                                            #self.var_manager_id.get(),
                                                                                                                                                                                                                            #self.var_radiobtn1.get(),
                                                                                                                                                                                                                            self.var_empid.get()
                                                                                                                                                                                                                            ))                                                        
                    else:
                        if not update:
                            return#remain in same window
                    messagebox.showinfo("Success","Employee Data is updated Successfully")
                    con.commit()
                    self.fetch_data()
                    con.close()
                    self.reset()
                        
                                                                              
                       
                        #remain in same window
                        
                                
                        
                                    

                              
                        
                    
                else:
                    messagebox.showerror("ERROR",'Cannot Change Employee ID',parent=self.root)
                    self.reset()
                                                                                                                                                                                                                                                                                                                                                                      
                    
            except Exception as es:
                messagebox.showerror("error",f"Due to:{str(es)}",parent=self.root)


    def delete_data(self):
        if self.var_empid.get()=="":
            messagebox.showerror("Error","Employee_id is must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete Data","Do You really want to delete this data",parent=self.root)
                if delete>0:
                    con=mysql.connector.connect(host="localhost",username="root",password="root",database="employee_management")
                    my_cursor=con.cursor()
                    sql="delete from employee_data where employee_id=%s"
                    val=(self.var_empid.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                con.commit()
                
                con.close()
                self.fetch_data()
                self.reset()
                messagebox.showinfo('Delete','Successfully Deleated Employee Detail',parent=self.root)
            except Exception as es:
                messagebox.showerror("error",f"Due to:{str(es)}",parent=self.root)


    #Reset function
    def reset(self):
        self.var_empid.set("")
        self.var_name.set("")
        self.var_cnic.set("")
        self.var_dob.set("")
        self.var_phone_no.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_martial_status.set("")
        self.var_job_title.set("")
        self.var_department.set("")
        #self.var_hire_date.set("")
        self.var_salary.set("")
        self.var_address.set("")
        #self.var_manager_id.set("")
        #self.var_radiobtn1.set("")

    #######Generate dataset to take photo samples
    
    def generate_dataset(self):
        name,id=self.get_cursor()
        print("name sss",name)
        if self.var_empid.get()=="" or self.var_name.get()=="" or self.var_cnic.get()=="" or self.var_dob.get()=="" or self.var_phone_no.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="" or self.var_martial_status.get()=="" or self.var_job_title.get()=="" or self.var_department.get()=="" or  self.var_salary.get()==0.0 or self.var_address.get()=="":
            messagebox.showerror("ERROR",'All Fields are required')
        else:
            try:
                con=mysql.connector.connect(host="localhost",username="root",password="root",database="employee_management")
                my_cursor=con.cursor()
                my_cursor.execute("select * from employee_data")
                result=my_cursor.fetchall()
                id=0
                for x in result:
                    id+=1
                my_cursor.execute("UPDATE employee_data SET Name=%s,CNIC=%s,DOB=%s,Phone_no=%s,Email=%s,Gender=%s,Martial_Status=%s,Job_Title=%s,Department=%s,Salary=%s,Address=%s WHERE employee_id=%s",(
                                                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                                                            self.var_cnic.get(),
                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                            self.var_phone_no.get(),
                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                            self.var_martial_status.get(),
                                                                                                                                                                                                            self.var_job_title.get(),
                                                                                                                                                                                                            self.var_department.get(),
                                                                                                                                                                                                                        #self.var_hire_date.get(),
                                                                                                                                                                                                            self.var_salary.get(),
                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                            #self.var_manager_id.get(),
                                                                                                                                                                                                                        #self.var_radiobtn1.get(),
                                                                                                                                                                                                            self.var_empid.get()==id+1
                                                                                                                                                                                                            ))
                con.commit()
                self.fetch_data()
                self.reset()
                con.close()
            

                

                def Crete_Folder_Images(name,id, tn,directory):
                    # Creating directory in the file
                    if not os.path.exists(directory):
                    
                        os.makedirs(directory)
                        
                        
                        faceDetect=cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml") #cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
                        
                        cam=cv.VideoCapture(0)
                        desired_frame_rate = 5
                        cam.set(cv.CAP_PROP_FPS, desired_frame_rate)
                        size =(224, 224)

                    
                        for i in tqdm(range(1, 1+ tn)):
                            
                            ret,img=cam.read()
                            gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)  #for GRAY SCALE IMAGES
                            faces=faceDetect.detectMultiScale(gray,1.3,5)
                            # faces=faceDetect.detectMultiScale(img,1.3,5)    # FOR COLOR IMAGES
                            for(x,y,w,h) in faces:
                                res = cv.resize(gray[y:y+h,x:x+w], size, interpolation = cv.INTER_AREA)
                                #cv.imwrite('Datasets/'+str(name) +'/'+str(name)+'.'+ str(id) + '.' + str(i) + ".jpg",res )  #for GRAY SCALE IMAGES
                                cv.imwrite('dataset/'+str(name)+'/'+str(name)+str(i)+'.jpg', res)
                                # cv2.imwrite(directory+'/'+str(name)+'-'+str(sn)+'.jpg'
                                #             ,img[y:y+h,x:x+w])  # FOR COLOR IMAGES
                                cv.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
                                cv.waitKey(400)
                            cv.imshow('Dataset Creator',img)
                            cv.waitKey(1)
                        cam.release()
                        cv.destroyAllWindows()
                        messagebox.showinfo('Successful','Images Successfully Taken')

                    else:
                        messagebox.showerror('Error','Directory Already Exist')


                # Taking inputs
                def tkinput(text) -> str:
                    import tkinter as tk
                    root2 = tk.Tk()
                    question = tk.StringVar()
                    question='mubbashar'
                    print("Value",question)

                    tk.Label(root2, text=text).pack()
                    e = tk.Entry(root2, textvariable=question)
                    e.pack()
                    e.focus()
                    # question.set("prova")
                    
                    e.bind("<Return>", lambda event: root2.destroy())
                    root.mainloop()
                    
                    return question
                #name = tkinput("What is your name?")
                #print(f"{name=}")
                #name=self.get_cursor_generate()
                #name='Adnan'
                #id=input('\nEnter your ID: ')

                #directory='Datasets/'+name
                tn=100
                #tn= int(input('Enter no.of images to be taken: '),parent=self.root)
                directory='dataset/'+name
                Crete_Folder_Images(name,id, tn,directory)
            except Exception as es:
                messagebox.showerror("error",f"Due to:{str(es)}",parent=self.root)


                ### load predefine data on face frontals from opencv
                




if __name__=='__main__':
    root=Tk()
    obj=employee_details(root)#creating object of class
    root.mainloop()#close the lop


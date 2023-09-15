from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import re
class Register:
    alive=False
    def destroy(self):
        # Restore the attribute on close.
        self.__class__.alive = False
        return super().destroy()
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry('1530x790+0+0')
        self.__class__.alive = True
       

        # ============ Variables =================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_cnum=StringVar()
        self.var_email=StringVar()
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()
        self.var_cpwd=StringVar()
        self.var_check=IntVar()

        img1=Image.open(r'D:\Bushi\Employees Face Recognition System\icons\bg2.jpg')
        img1=img1.resize((1920,1080),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lb1_bg=Label(self.root,image=self.photoimg1)
        lb1_bg.place(x=0,y=0,width=1920,height=1080)


        frame= Frame(self.root,bg="#F2F2F2",highlightbackground="#002B53", highlightthickness=5)
        frame.place(x=310,y=100,width=900,height=580)
        

        # img1=Image.open(r"C:\Users\Muhammad Waseem\Documents\Python_Test_Projects\Images_GUI\reg1.png")
        # img1=img1.resize((450,100),Image.ANTIALIAS)
        # self.photoimage1=ImageTk.PhotoImage(img1)
        # lb1img1 = Label(image=self.photoimage1,bg="#F2F2F2")
        # lb1img1.place(x=300,y=100, width=500,height=100)
        

        get_str = Label(frame,text="Registration",font=("times new roman",30,"bold"),fg="#002B53",bg="#F2F2F2")
        get_str.place(x=320,y=50)
        #Label 1
       

        def f_name_validation():
            name=self.var_fname.get()
            print("najndjnjsn",name)
            msg = ''

            if len(name) == 0:
                msg = 'name can\'t be empty'
            else:
                try:
                    if any(ch.isdigit() for ch in name):
                        msg = 'Name can\'t have numbers'
                        messagebox.showerror('Incorrect First Name', msg,parent=self.root)
                        self.var_fname.set('')
                    elif len(name) <= 2:
                        msg = 'name is too short.'
                        messagebox.showerror('Incorrect First Name', msg,parent=self.root)
                        self.var_fname.set('')
                    elif len(name) > 100:
                        msg = 'name is too long.'
                        messagebox.showerror('Incorrect First Name', msg,parent=self.root)
                        self.var_fname.set('')
                    else:
                        msg = ''
                except Exception as ep:
                    messagebox.showerror('error', ep,parent=self.root)
            return True
        #label1 
        fname =lb1= Label(frame,text="First Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        fname.place(x=100,y=150)
        

        #entry1 
        self.f_name=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"),validate='focusout',validatecommand=f_name_validation)
        self.f_name.place(x=103,y=175,width=270)

        def l_name_validation():
            name=self.var_lname.get()
            msg = ''

            if len(name) == 0:
                msg = 'name can\'t be empty'
            else:
                try:
                    if any(ch.isdigit() for ch in name):
                        msg = 'Name can\'t have numbers'
                        messagebox.showerror('Incorrect Last Name', msg,parent=self.root)
                        self.var_lname.set('')
                    elif len(name) <= 2:
                        msg = 'name is too short.'
                        messagebox.showerror('Incorrect Last Name', msg,parent=self.root)
                        self.var_lname.set('')
                    elif len(name) > 100:
                        msg = 'name is too long.'
                        messagebox.showerror('Incorrect Last Name', msg,parent=self.root)
                        self.var_lname.set('')
                    else:
                        msg = ''
                except Exception as ep:
                    messagebox.showerror('error', ep,parent=self.root)
            return True


        #label2 
        lname =lb2= Label(frame,text="Last Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        lname.place(x=100,y=220)

        #entry2 
        self.l_name=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"),validate='focusout',validatecommand=l_name_validation)
        self.l_name.place(x=103,y=245,width=270)

        # ==================== section 2 -------- 2nd Columan===================

        #label1 
        def validate_contact():
            passwd = self.var_cnum.get()
            regex = "^((\+92)|(051))-{0,1}\d{3}-{0,1}\d{7}$|^\d{11}$|^\d{4}-\d{7}$"

            pat = re.compile(regex)
            mat = re.search(pat, passwd)
            
            # validating conditions
            if(self.var_cnum.get()==''):
                print('')

            else:
                if mat:
                    print("")
                else:
                    messagebox.showerror('Incorrect Contact', 'Write Correct Phone Number like 03157784521',parent=self.root)
                    self.var_cnum.set('')
                
            return True
        
        
       
        
        cnum =lb1= Label(frame,text="Contact Number:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cnum.place(x=530,y=150)

        #entry1 
        def delete_num(e):
           txtuser.delete(0,END)
        txtuser=ttk.Entry(frame,textvariable=self.var_cnum,font=("times new roman",15,"bold"),validate='focusout',validatecommand=validate_contact)
        txtuser.insert(5,"03495454687")
        txtuser.bind('<FocusIn>',delete_num)
        #txtuser.configure(state='disabled')
        txtuser.place(x=533,y=175,width=270)


        #label2 
        email =lb1= Label(frame,text="Email:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        email.place(x=530,y=220)

        #entry2
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
                        self.var_email.set('')
                except Exception as ep:
                    messagebox.showerror('error', ep,parent=self.root)
                
            
            return True 
        
        
        def delete_emai(e):
           txtemail.delete(0,END)
        
        
        txtemail=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"),validate='focusout',validatecommand=validate_email)
        txtemail.insert(5,"xyz@gmail.com")
        txtemail.bind("<FocusIn>",delete_emai)
        #self.txtemail.configure(state='disabled')
        txtemail.place(x=533,y=245,width=270)

        # ========================= Section 3 --- 1 Columan=================

        #label1 
        ssq =lb1= Label(frame,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        ssq.place(x=100,y=300)

        #Combo Box1
        self.combo_security = ttk.Combobox(frame,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
        self.combo_security.current(0)
        self.combo_security.place(x=103,y=335,width=270)


        #label2 
        sa =lb1= Label(frame,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        sa.place(x=100,y=370)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_sa,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=103,y=395,width=270)

        # ========================= Section 4-----Column 2=============================
        
        def validate_password():
            passwd = self.var_pwd.get()
            regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&+-])[A-Za-z\d@$!#%*-?&+]{6,20}$"
            pat = re.compile(regex)
     
            # searching regex                
            mat = re.search(pat, passwd)
            
            # validating conditions
            if self.var_pwd.get()=='':
                print('')
            else:
                if mat:
                    print("")
                else:
                    messagebox.showerror('Passowrd Error', 'Pssword must be Alphanumeric',parent=self.root)
                    self.var_pwd.set('')
                
            return True
        #label1 
        pwd =lb1= Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        pwd.place(x=530,y=300)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_pwd,font=("times new roman",15,"bold"),show="*",validate='focusout',validatecommand=validate_password)
        #self.txtuser.insert(5,"Pass must be AlphaNumeric")
        #self.txtuser.configure(state='disabled')
        self.txtuser.place(x=533,y=325,width=270)

        def validate_confirm_password():
            passwd = self.var_cpwd.get()
            regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&+-])[A-Za-z\d@$!#%*-?&+]{6,20}$"
            pat = re.compile(regex)
     
            # searching regex                
            mat = re.search(pat, passwd)
            
             # validating conditions
            if self.var_cpwd.get()=='':
                print('')
            else:
                if mat:
                    print("")
                else:
                    messagebox.showerror('Password Error', 'Pssword must be Alphanumeric',parent=self.root)
                    self.var_cpwd.set('')
                
            return True
        #label2 
        cpwd =lb1= Label(frame,text="Confirm Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cpwd.place(x=530,y=370)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_cpwd,font=("times new roman",15,"bold"),show="*",validate='focusout',validatecommand=validate_confirm_password)
        #self.txtpwd.insert(5,"Pass must be AlphaNumeric")
        #self.txtpwd.configure(state='disabled')
        self.txtpwd.place(x=533,y=395,width=270)

        # Checkbutton
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",13,"bold"),fg="#002B53",bg="#F2F2F2")
        checkbtn.place(x=100,y=450,width=270)


        # Creating Button Register
        loginbtn=Button(frame,command=self.reg,text="Register",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=300,y=510,width=250,height=35)

        # Creating Button Login
      



    def reg(self):
        if (self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_cnum.get()=="" or self.var_email.get()=="" or self.var_ssq.get()=="Select" or self.var_sa.get()=="" or self.var_pwd.get()=="" or self.var_cpwd.get()==""):
            messagebox.showerror("Error","All Field Required!",parent=self.root)
        elif(self.var_pwd.get() != self.var_cpwd.get()):
            messagebox.showerror("Error","Please Enter Same Password & Confirm Password!",parent=self.root)
        elif(self.var_check.get()==0):
            messagebox.showerror("Error","Please Check the Agree Terms and Conditons!",parent=self.root)
        else:
            # messagebox.showinfo("Successfully","Successfully Register!")
            try:
                conn = mysql.connector.connect(username='root', password='root',host='localhost',database='employee_management')
                mycursor = conn.cursor()
                query=("select * from employee_record where email=%s")
                value=(self.var_email.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist,please try another email")
                else:
                    mycursor.execute("insert into employee_record values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_cnum.get(),
                    self.var_email.get(),
                    self.var_ssq.get(),
                    self.var_sa.get(),
                    self.var_pwd.get()
                    ))

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Successfully Registerd!",parent=self.root)
                    
                    root.destroy()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


        
if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
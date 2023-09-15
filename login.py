from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
import os
import re
from main import Face_Recognition

#from pre_trained_model import training


class Login():
    alive = False
    def destroy(self):
        # Restore the attribute on close.
        self.__class__.alive = False
        return super().destroy()
    def __init__(self,root):
        self.main_root=root
        self.main_root.title("Login-Employee Management System")
        self.main_root.geometry('1530x790+0+0')

        # variables 
        self.email=StringVar()
        self.password=StringVar()
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()
        
        img1=Image.open(r'D:\Bushi\Employees Face Recognition System\icons\loginBg.jpg')
        img1=img1.resize((1920,1080),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lb1_bg=Label(self.main_root,image=self.photoimg1)
        lb1_bg.place(x=0,y=0,width=1920,height=1080)
        
        frame1= Frame(self.main_root,bg="white",highlightbackground="#002B53", highlightthickness=5)
        frame1.place(x=600,y=180,width=340,height=450)

        #img_1=Image.open(r'C:\Users\Mubashir\Downloads\icon.png')
        #img_1=img_1.resize((150,150),Image.LANCZOS)
        #self.photoimg_1=ImageTk.PhotoImage(img_1)
        #lb1img1 = Label(image=self.photoimg_1,bg="#002B53")
        #lb1img1.place(x=680,y=175, width=150,height=150)

        get_str = Label(frame1,text="Login",font=("times new roman",30,"bold"),fg="#002B53",bg="white")
        get_str.place(x=110,y=50)

        #label1 
        username =lb1= Label(frame1,text="Email:",font=("times new roman",15,"bold"),fg="#002B53",bg="white")
        username.place(x=30,y=160)
        check=0
        def validate_email():
            email = self.email.get()
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
                        messagebox.showerror('Incorrect Email Format', 'Write Email in Correct Format ',parent=self.main_root)
                        self.email.set('')
                except Exception as ep:
                    messagebox.showerror('error', ep,parent=self.main_root)
                
            
            return True
        #entry1 
            
        self.txtuser=ttk.Entry(frame1,textvariable=self.email,font=("times new roman",15,"bold"),validate='focusout',validatecommand=validate_email)
        self.txtuser.place(x=33,y=190,width=270)
 
            #label2 
        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="white")
        pwd.place(x=30,y=230)

            

       
        


        

        #entry2 
        self.txtpwd=ttk.Entry(frame1,textvariable=self.password,font=("times new roman",15,"bold"),show='*')
        self.txtpwd.place(x=33,y=260,width=270)


        # Creating Button Login
       
        loginbtn=Button(frame1,command=self.login,text="Login",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#002B53",borderwidth=1)
        loginbtn.place(x=120,y=330,width=80,height=30)
        #font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC"
        

        # Creating Button Registration
        loginbtn=Button(frame1,command=self.reg,text="Sign Up",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="white",activebackground="#002B53",borderwidth=1)
        loginbtn.place(x=30,y=330,width=80,height=30)


        # Creating Button Forget
        loginbtn=Button(frame1,command=self.forget_pwd,text="Forget",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="white",activebackground="#002B53",borderwidth=1)
        loginbtn.place(x=210,y=330,width=80,height=30)

        
   
    #  THis function is for open register window
    def chek_pass_window(self):
        if not Login.alive:
            self.forget_pwd()

      
    def forget_pwd(self):
        #if not Login.alive:
            self.__class__.alive = True
            if self.txtuser.get=="":
                    messagebox.showerror("Error","Please Enter the Email ID to reset Password!",parent=self.main_root)
            else:
                
                    conn = mysql.connector.connect(username='root', password='root',host='localhost',database='employee_management')
                    mycursor = conn.cursor()
                    query=("select * from employee_record where email=%s")
                    value=(self.txtuser.get(),)
                    mycursor.execute(query,value)
                    row=mycursor.fetchone()
                    # print(row)

                    if row==None:
                        messagebox.showerror("Error","Please Enter the Valid Email ID!",parent=self.main_root)
                    else:
                        conn.close()
                        self.main_root.withdraw()
                        self.root2=Toplevel()
                        self.root2.title("Forget Password")
                        self.root2.geometry("400x400+570+220")
                        l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                        l.place(x=0,y=10,relwidth=1)
                        # -------------------fields-------------------
                        #label1 
                        ssq =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                        ssq.place(x=70,y=80)

                        #Combo Box1
                        self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
                        self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                        self.combo_security.current(0)
                        self.combo_security.place(x=70,y=110,width=270)


                        #label2 
                        sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                        sa.place(x=70,y=150)

                        #entry2 
                        self.txt_pwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("times new roman",15,"bold"))
                        self.txt_pwd.place(x=70,y=180,width=270)

                        #label2 
                        new_pwd =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                        new_pwd.place(x=70,y=220)

                        #entry2 
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
                                    #self.txtpwd=ttk.Entry(self.main_root,textvariable=self.var_pwd)
                                
                                else:
                                    messagebox.showerror('Passowrd Error', 'Pssword must be Alphanumeric',parent=self.root2)
                                    self.var_pwd.set('')
                                
                            return True
                        self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("times new roman",15,"bold"),show='*',validate='focusout',validatecommand=validate_password)
                        self.new_pwd.place(x=70,y=250,width=270)

                        # Creating Button New Password
                        loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                        loginbtn.place(x=70,y=300,width=270,height=35)
                        



    def reset_pass(self):
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(username='root', password='root',host='localhost',database='employee_management')
            mycursor = conn.cursor()
            query=("select * from employee_record where email=%s and ssq=%s and sa=%s")
            value=(self.txtuser.get(),self.var_ssq.get(),self.var_sa.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                query=("update employee_record set pwd=%s where email=%s")
                value=(self.var_pwd.get(),self.txtuser.get())
                mycursor.execute(query,value)
                #self.txtpwd=self.var_pwd.get()

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root2)
                self.main_root.deiconify()
                print("value before destroy",self.var_pwd,self.txtuser.get(),self.txtpwd)
                self.root2.destroy()
                

            


    def reg(self):
        #if not Register.alive:
            self.new_window=Toplevel(self.main_root)
            self.app=Register(self.new_window)
    def login(self):
        if  self.txtuser.get()=="" or self.txtpwd.get()=="":
            messagebox.showerror("Error","All Field Required!",parent=self.main_root)
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            conn = mysql.connector.connect(username='root', password='root',host='localhost',database='employee_management')
            mycursor = conn.cursor()
            mycursor.execute("select * from employee_record where email=%s and pwd=%s",(
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row=mycursor.fetchone()
            conn.commit()
            conn.close()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!",parent=self.main_root)
                self.email.set('')
                self.password.set('')
            else:
                #if not Face_Recognition.alive:  
                    self.main_root.withdraw()  
                    self.new_window=Toplevel(self.main_root)
                    self.app=Face_Recognition(self.new_window)

                
        return
            
    
    

#=======================Reset Passowrd Function=============================


if __name__ == "__main__":
    root=Tk()
    app=Login(root)
    root.mainloop()
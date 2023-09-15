from tkinter import * # create gui in pythom
from tkinter import ttk
from tkinter import messagebox# stylish toolkit
from PIL import Image,ImageTk# to import images in python
from Employee_Details import employee_details
import os
import sys
from recognize import face_varification
from pre_trained_model import training
#from face_recognition_page import Recognition
from train_images import Train
from face_finalized import Recognition
from attendance_report import Attendance
class Face_Recognition:
    alive = False

    def __init__(self,root ):#constructor #root name of window
        
        self.root=root
        self.root.geometry('1530x790+0+0')#0+0Position of window on x and y axis
        self.root.title('Face Recognition System')


        img1=Image.open(r'D:\Bushi\Employees Face Recognition System\icons\bg2.jpg')
        img1=img1.resize((1920,1080),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_label=Label(self.root,image=self.photoimg1)
        f_label.place(x=0,y=0,width=1920,height=1080)

        title_label=Label(f_label,text="Face Recognotion Attendence System",font=("time new roman",30,'italic'),bg="white", fg='#002B53')
        title_label.place(x=-200,y=100,width=1920,height=45)

        #Employee detail button
        img2=Image.open(r'D:\Bushi\Employees Face Recognition System\icons\em.png')
        img2=img2.resize((150,150),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        employee_btn=Button(f_label,image=self.photoimg2,command=self.employee_details_funcall)
        employee_btn.place(x=270,y=200,width=150,height=150)

        employee_btn1_1=Button(f_label,text="Employee Details",command=self.employee_details_funcall,font=("time new roman",10,'italic'),bg="white",fg='#002B53')
        employee_btn1_1.place(x=270,y=350,width=150,height=30)

        # employee_btn=Button(f_label,image=self.photoimg2,command=self.employee_details_funcall)
        # employee_btn.place(x=200,y=100,width=150,height=150)

        # employee_btn1_1=Button(f_label,text="Employee Details",command=self.employee_details_funcall,font=("time new roman",10,'italic'),bg='black',fg='white')
        # employee_btn1_1.place(x=200,y=100,width=150,height=30)


        # face Recognition button
        img3=Image.open(r'D:\Bushi\Employees Face Recognition System\icons\f_det.jpg')
        img3=img3.resize((150,150),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        face_rec_btn=Button(f_label,image=self.photoimg3,command=self.test_funcall)
        face_rec_btn.place(x=670,y=200,width=150,height=150)

        face_rec_btn1_1=Button(f_label,text="Face Recognition",command=self.test_funcall,font=("time new roman",10,'italic'),bg="white",fg='#002B53')
        face_rec_btn1_1.place(x=670,y=350,width=150,height=30)


        #Attendence button
        img4=Image.open(r'D:\Bushi\Employees Face Recognition System\icons\att.jpg')
        img4=img4.resize((150,150),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        attendence_btn=Button(f_label,image=self.photoimg4,command=self.attendance_funcall)
        attendence_btn.place(x=1070,y=200,width=150,height=150)

        attendence_btn1_1=Button(f_label,text="Attendence",command=self.attendance_funcall,font=("time new roman",10,'italic'),bg="white",fg='#002B53')
        attendence_btn1_1.place(x=1070,y=350,width=150,height=30)

        #Train Data Button
        img5=Image.open(r'D:\Bushi\Employees Face Recognition System\icons\tra1.jpg')
        img5=img5.resize((150,150),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        train_data_btn=Button(f_label,image=self.photoimg5,command=self.train_funcall)
        train_data_btn.place(x=270,y=450,width=150,height=150)

        train_data_btn1_1=Button(f_label,text="Train Data",command=self.train_funcall,font=("time new roman",10,'italic'),bg="white",fg='#002B53')
        train_data_btn1_1.place(x=270,y=600,width=150,height=30)

        #photos Button
        img6=Image.open(r'D:\Bushi\Employees Face Recognition System\icons\cam.jpg')
        img6=img6.resize((150,150),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        photo_btn=Button(f_label,image=self.photoimg6,command=self.open_img)
        photo_btn.place(x=670,y=450,width=150,height=150)

        photo_btn1_1=Button(f_label,text="Photos",font=("time new roman",10,'italic'),bg="white",fg='#002B53',command=self.open_img)
        photo_btn1_1.place(x=670,y=600,width=150,height=30)

        #exit Button
        img7=Image.open(r'D:\Bushi\Employees Face Recognition System\icons\exit.jpg')
        img7=img7.resize((150,150),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        exit_btn=Button(f_label,image=self.photoimg7,command=self.employee_exit)
        exit_btn.place(x=1070,y=450,width=150,height=150)

        exit_btn1_1=Button(f_label,text="Exit",font=("time new roman",10,'italic'),bg="white",fg='#002B53',command=self.employee_exit)
        exit_btn1_1.place(x=1070,y=600,width=150,height=30)

        self.__class__.alive = True

    #Functioncall Set on Employee Detail Button
    def employee_details_funcall(self):
            
        #if not employee_details.alive and not Attendance.alive and not Recognition.alive and not Train.alive:
            self.employee_details_window=Toplevel(self.root)
            self.app=employee_details(self.employee_details_window)
    
    def attendance_funcall(self):
        
        #if not Attendance.alive and not employee_details.alive and not Recognition.alive and not Train.alive:
            self.attendance_window=Toplevel(self.root)
            self.app=Attendance(self.attendance_window)

    def train_funcall(self):
            
        #if not Train.alive :
            self.train_window=Toplevel(self.root)
            self.app=Train(self.train_window)


    def test_funcall(self):
    
        #if not employee_details.alive and not Attendance.alive and not Recognition.alive and not Train.alive:
            self.recognition_window=Toplevel(self.root)
            self.app=Recognition(self.recognition_window)

    def employee_exit(self):
        if messagebox.askyesno('Exit', 'Exit the Applicaton'):
            sys.exit()

    def open_img(self):
        os.startfile("D:\Bushi\Employees Face Recognition System\dataset")

if __name__ == "__main__":
    root=Tk()
    app=Face_Recognition(root)
    root.mainloop()
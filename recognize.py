from tkinter import messagebox
from PIL import Image
import numpy as np
import cv2
import pickle
from keras.models import load_model
import mysql.connector
from datetime import datetime
import sqlite3

# for face detection


# load the trained model


class face_varification:
    alive=False
    def destroy(self):
        # Restore the attribute on close.
        self.__class__.alive = False
        return super().destroy()
    def __init__(self):
      
        self.start()
        self.__class__.alive = True
    #labels for the trained model

    def database(self,name,id,dep):
        print("database")
        if name=="" or id=="" or dep=="":
            messagebox.showerror("ERROR",'Data for Employee Not Found')
        else:
            try:
                    con=mysql.connector.connect(host="localhost",username="root",password="root",database="employee_management")
                    my_cursor=con.cursor()
                    print("database ma agaya")
                    condition="select emp_id from employee_attendance where emp_name=%s"
                    apply=(name,)
                    my_cursor.execute(condition,apply)
                    id=my_cursor.fetchone()
                    if id=='':

                     

                        now=datetime.now()
                        d1=now.strftime("%d/%m/%Y")
                        dtString=now.strftime("%H:%M:%S") 
                        status='Present'                                                                                                                                                                                                                                                                                                                                                     
                        my_cursor.execute("insert into employee_attendance values (%s,%s,%s,%s,%s,%s)",(
                                                                                                                                                                    id,
                                                                                                                                                                    dep,
                                                                                                                                                                    name,
                                                                                                                                                                    dtString,
                                                                                                                                                                    d1,
                                                                                                                                                                    status
                                                                                                                                                                ))                                                        
            
                                    #remain in same window
                        messagebox.showinfo("Success","Employee Data is updated Successfully")
                        con.commit()
                            
                        con.close()

                    else:
                        messagebox.showerror("Record","Employee Attendance Already Exists")
                        
            except Exception as es:
                messagebox.showerror("error",f"Due to:{str(es)}")


    def mark_attendance(self,r,name,n):
            with open("attendance.csv","r+",newline="\n") as f:
                print("attendance")
                myDatalist=f.readlines()
                print("ahsudhushauhd",myDatalist)
                name_list=[]
                for line in myDatalist:
                    entry=line.split((","))
                    name_list.append(entry[0])

                print("alllllllllllllllllll",name_list)
                print("type of n",type(n))
                print("type of name",type(name))
                print("type of r",type(r))
                print("type of namelist",type(name_list))
                if ((r not in name_list)) and ((name not in name_list)) and ((n not in name_list)):
                    print("ab kia hogya ha")
                if ((r not in name_list)) and ((name not in name_list)) and ((n not in name_list)):
                    now=datetime.now()
                    d1=now.strftime("%d/%m/%Y")
                    dtString=now.strftime("%H:%M:%S")
                    f.writelines(f"\n{r},{name},{n},{dtString},{d1},Present")

    def start(self):
        cascPath = "C:\\Users\\Mubashir\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\cv2\data\\haarcascade_frontalface_default.xml"
        face_cascade =  cv2.CascadeClassifier(cascPath)

        # resolution of the webcam
        screen_width = 1280       # try 640 if code fails
        screen_height = 720

        # size of the image to predict
        image_width = 224
        image_height = 224
        # default webcam
        model = load_model('transfer_learning_trained_face_cnn_model.h5')
        with open("face-labels.pickle", 'rb') as f:
            og_labels = pickle.load(f)
            labels = {key:value for key,value in og_labels.items()}
        print(labels)

        stream = cv2.VideoCapture(0)

        while(True):
            # Capture frame-by-frame
            (grabbed, frame) = stream.read()
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # try to detect faces in the webcam
            faces = face_cascade.detectMultiScale(rgb, scaleFactor=1.3, minNeighbors=5)

            # for each faces found
            for (x, y, w, h) in faces:
                try:
                    roi_rgb = rgb[y:y+h, x:x+w]
                    cv2.rectangle(frame, (x, y), (x + w, y + h),(255,0,255),2)

                    # resize the image
                    size = (image_width, image_height)
                    resized_image = cv2.resize(roi_rgb, size)
                    image_array = np.array(resized_image, "uint8")
                    img = image_array.reshape(1,image_width,image_height,3) 
                    img = img.astype('float32')
                    img /= 255

                    # predict the image
                    predicted_prob = model.predict(img)
                    print("Prediction score",predicted_prob)
                    print("hello")
                    name = labels[predicted_prob[0].argmax()]
                    confidence=int((100*(1-predicted_prob[0].argmax()/300)))
                    print("what is confidence",confidence)
                    print("name iss",name)
                    print("type of name",type(name))
                    print("length of name",len(name))
                    conn2 = mysql.connector.connect(username='root', password='root',host='localhost',database='employee_management')
                    cursor2 = conn2.cursor()
                    print("first")        
                    #cursor.execute("select emp_id from employee_attendance where emp_name="+name)
                    condition="select Department from employee_data where Name=%s"
                    apply=(name,)
                    cursor2.execute(condition,apply)
                    dep=cursor2.fetchone()
                    dep="+".join(dep)

                    condition="select employee_id from employee_data where Name=%s"
                    apply=(name,)
                    cursor2.execute(condition,apply)
                    id=cursor2.fetchone()
                    id=str(id[0])
                    print("This data fetches from employee data database",dep,id,name)

                    #con = mysql.connector.connect(username='root', password='root',host='localhost',database='employee_management')
                    #cursor = con.cursor()
                    #print("first")        
                    #cursor.execute("select emp_id from employee_attendance where emp_name="+name)
                    #condition="select emp_dep from employee_attendance where emp_name=%s"
                    #apply=(name,)
                    #cursor.execute(condition,apply)
                    #print("database")
                    #n=cursor.fetchone()

                    #print("value of n",n)
                    #print("type of n",type(n))
                
                    #n="+".join(n)
                    #print("pehla hgayaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",n)
                    #condition="select emp_id from employee_attendance where emp_name=%s"
                    #apply=(name,)
                    #cursor.execute("select emp_dep from employee_attendance where emp_name="+str(name))
                    #cursor.execute(condition,apply)
                    #r=cursor.fetchone()
                    #print("value of r",r)
                    #print("type of r",type(r))
                    #r=str(r[0])
                    #r="+".join(r)
                    #print("dosra hgayaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",r)

                    #cursor.execute("select emp_id from employee_attendance where emp_id="+str(maximum))
                    #i=cursor.fetchone()
                    #i="+".join(i)
                    #print("tesra hgayaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                            
                    if confidence > 77:
                        print("does is comes here 123")
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 100, 0), 2)
                        cv2.putText(frame,f"emp_id:{id}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,100,0),2)
                        cv2.putText(frame,f"emp_name:{name}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,100,0),2)
                        cv2.putText(frame,f"emp_dep:{dep}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,100,0),2)
                        #self.mark_attendance(id,name,name)
                        self.database(name,id,dep)
                    else:
                        
                        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
                        cv2.putText(frame,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)
                    # Display the label
                except:
                    le=2
                # Show the frame
            cv2.imshow("Image", frame)
            c = cv2.waitKey(1)
            if c & 0xFF == ord('q'):
                break     

        stream.release()
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
if __name__ == "__main__":
    face_varification()
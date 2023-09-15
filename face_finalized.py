# import re
from sys import path
from tkinter import messagebox
from PIL import Image
import numpy as np
from keras.applications.mobilenet import preprocess_input
import cv2
import pickle
from keras.models import load_model
import mysql.connector
from datetime import datetime
from sklearn.preprocessing import normalize
import sklearn
import sqlite3
from keras.models import Model
from keras.layers import GlobalAveragePooling2D, Dense

from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from keras_vggface.vggface import VGGFace
import os
import mysql.connector
import cv2
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from tkinter import messagebox
from time import strftime
from datetime import datetime
class Recognition:
    alive=False
    def destroy(self):
        # Restore the attribute on close.
        self.__class__.alive = False
        return super().destroy()
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition Pannel")
        self.__class__.alive = True

        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"D:\Bushi\Employees Face Recognition System\icons\banner.jpg")
        img=img.resize((1920,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1920,height=130)

        # backgorund image 
        bg1=Image.open(r"D:\Bushi\Employees Face Recognition System\icons\bg2.jpg")
        bg1=bg1.resize((1920,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1920,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Face Recognition Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=-200,y=0,width=1920,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"D:\Bushi\Employees Face Recognition System\icons\f_det.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.start,image=self.std_img1,cursor="hand2")
        std_b1.place(x=670,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.start,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=670,y=350,width=180,height=45)
    #=====================Attendance===================
   
    def destroy(self):
        # Restore the attribute on close.
        self.__class__.alive = False
        return super().destroy()
      
   
        
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
                    condition="select emp_id, emp_date from employee_attendance where emp_name=%s"
                    apply=(name,)
                    my_cursor.execute(condition,apply)
                    check=my_cursor.fetchall()
                    print("what is value of check",check)
                    now = datetime.now()
                    d1 = now.strftime("%d/%m/%Y")
                    record_found=False
                    check_id=int(id)
                    check_list=(check_id,d1)
                    print("type of check",len(check))
                    print("type of check",len(check_list))
                    for i in check:
                        print(i)
                        if(i==check_list):
                            record_found=True
                            print
                            print("exisit")
                    print(check_list)
                    if  record_found == True:
                        print("Repeat Record")
                    else:
                        now = datetime.now()
                        d1 = now.strftime("%d/%m/%Y")
                        dtString = now.strftime("%H:%M:%S") 
                        status = 'Present'                                                                                                                                                                                                                                                                                                                                                   
                        my_cursor.execute("insert into employee_attendance values (%s,%s,%s,%s,%s,%s)",(
                                                                                                                                                                    id,
                                                                                                                                                                    dep,
                                                                                                                                                                    name,
                                                                                                                                                                    dtString,
                                                                                                                                                                    d1,
                                                                                                                                                                    status
                                                                                                                                                                ))                                                        

                        
                        #remain in same window
                        messagebox.showinfo("Success",f"{name}  Attendance Successfully Marked",parent=self.root)
                        con.commit()
                        con.close()
                   
                        
                        #messagebox.showerror("Record","Employee Attendance Already Exists",parent=self.root)
                        
                        
            except Exception as es:
                messagebox.showerror("error",f"Due to:{str(es)}")

    def is_marked(self,name):
        con=mysql.connector.connect(host="localhost",username="root",password="root",database="employee_management")
        my_cursor=con.cursor()
        print("database ma agaya")
        condition="select emp_id from employee_attendance where emp_name=%s"
        apply=(name,)
        my_cursor.execute(condition,apply)
        id=my_cursor.fetchone()
        if id=='':
            return 0
        else:
            return 1


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
        #base_model = load_model('transfer_learning_trained_face_cnn_model-testing.h5')
        #model.summary()
        model = VGGFace(include_top=False,
            model='vgg16',
            input_shape=(224, 224, 3))
        #model.summary()
        embeddings_file_path = 'D:\\Bushi\\Employees Face Recognition System\\trained model\\known_embeddings-1.pkl'
        identities_file_path = 'D:\\Bushi\\Employees Face Recognition System\\trained model\\known_identities-1.pkl'
        with open(embeddings_file_path, 'rb') as embeddings_file:
            loaded_known_embeddings = pickle.load(embeddings_file)

        # Load known identities from pickle file
        with open(identities_file_path, 'rb') as identities_file:
            loaded_known_identities = pickle.load(identities_file)
        screen_width = 1280       # try 640 if code fails
        screen_height = 720

        # size of the image to predict
        image_width = 224
        image_height = 224
        def preprocess_image(image):
            image = cv2.resize(image, (224, 224))
            image = preprocess_input(image)
        
            return image

        # Function to calculate the embedding for an image using the loaded model
        def calculate_embedding(image):
            preprocessed_image = preprocess_image(image)
            embedding = model.predict(np.expand_dims(preprocessed_image, axis=0))
            return embedding

        # default webcam
        #model = load_model('transfer_learning_trained_face_cnn_model.h5')
        with open("D:\\Bushi\\Employees Face Recognition System\\trained model\\face-labels-testing.pickle", 'rb') as f:
            og_labels = pickle.load(f)
            labels = {key:value for key,value in og_labels.items()}
        print(labels)

        self.stream = cv2.VideoCapture(0)

        while(True):
            # Capture frame-by-frame
            (grabbed, frame) = self.stream.read()
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # try to detect faces in the webcam
            faces = face_cascade.detectMultiScale(rgb, scaleFactor=1.1, minNeighbors=5)

            # for each faces found
            for (x, y, w, h) in faces:
                try:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    detected_face = frame[y:y+h, x:x+w]
                    detected_face_embedding = calculate_embedding(detected_face)
                   
                    print("Detected Face Embedding Shape:", detected_face_embedding.shape)
                    detected_face_embedding_2d = detected_face_embedding.reshape(1, -1)
                    #print("Detected Face Embedding Shape 2:", detected_face_embedding_2d.shape)
                    #print("known loadeed Embeddings",loaded_known_embeddings)
                    #print("known loadeed Identities",loaded_known_identities)
                    #detected_num_embeddings = detected_face_embedding.shape[0]
                    #detected_embedding_dimension = np.prod(detected_face_embedding.shape[1:])
                    #detected_embedding_array = detected_face_embedding.reshape(detected_num_embeddings, detected_embedding_dimension)
                    detected_known_embeddings_normalized = normalize(detected_face_embedding_2d, axis=1, norm='l2')
                    #detected_known_embeddings_normalized = normalize(detected_face_embedding)
                    
                    print("value of normalizzed",detected_known_embeddings_normalized)
                    print("Detected Face Embedding Shape 3:", detected_known_embeddings_normalized.shape)
                    #detected_face_embeddings = normalize(detected_face_embeddings, axis=1, norm='l2')
                    #print("yaaaaq",detected_known_embeddings_normalized)
                    #print("type of embedding",type(detected_known_embeddings_normalized))
                    #print("len of embedding",len(detected_known_embeddings_normalized))
                    #print("Normalized Detected Face Embedding:", detected_known_embeddings_normalized.shape)

                    # predict the image
                 
                    #embedding = model.predict(np.expand_dims(img, axis=0))
                    
                    print("loaded",loaded_known_embeddings.shape)
                    similarities = cosine_similarity(detected_known_embeddings_normalized, loaded_known_embeddings)

                    #print("before",similarities)
                    print("type",type(similarities))
                    print("shape",similarities.shape)
                    print("len",len(similarities))
                    print("max",similarities.max())
                    similarity_threshold = 0.5
                    

    # Identify the most similar identity
                    most_similar_idx = np.argmax(similarities)
                    print("thershhold",most_similar_idx)
                    print("max value is",similarities.max())
                    #print("max cosine",similarities[most_similar_idx])
                    if similarities.max()  > similarity_threshold:
                        recognized_identity = loaded_known_identities[most_similar_idx]
                      
                        conn2 = mysql.connector.connect(username='root', password='root',host='localhost',database='employee_management')
                        cursor2 = conn2.cursor()
                        print("first")        
                        #cursor.execute("select emp_id from employee_attendance where emp_name="+name)
                        condition="select Department from employee_data where Name=%s"
                        apply=(recognized_identity,)
                        cursor2.execute(condition,apply)
                        dep=cursor2.fetchone()
                        dep="+".join(dep)
                        condition="select employee_id from employee_data where Name=%s"
                        apply=(recognized_identity,)
                        cursor2.execute(condition,apply)
                        id=cursor2.fetchone()
                        id=str(id[0])
                        print("This data fetches from employee data database",dep,id,recognized_identity)

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

                        #if  predicted_prob.max()> 0.77:
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 100, 0), 2)
                        cv2.putText(frame,f"emp_id:{id}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,100,0),2)
                        cv2.putText(frame,f"emp_name:{recognized_identity}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,100,0),2)
                        cv2.putText(frame,f"emp_dep:{dep}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,100,0),2)
                            #self.mark_attendance(id,name,name)
                        #print('value ya return karra',self.is_marked(name))
                        self.database(recognized_identity,id,dep)
                    else:

                        recognized_identity = "Unknown"
                        cv2.rectangle(frame, (x, y) , (x+w, y+h), (139, 0, 0),2)
                        cv2.putText(frame,"Unknown Face",(x,y-50),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),2)
                        #print("hey",similarities[most_similar_idx])
                   # predicted_prob = model.predict(img)
                    #x, y, w, h = [...]  # Coordinates of the detected face
                

                    # Display the frame
                    #cv2.imshow('Face Recognition', frame)
                    #print("Prediction score",predicted_prob)
                    #print("hello",predicted_prob[0])
                    #name = labels[predicted_prob[0].argmax()]

                    #confidence=int((100*(1-predicted_prob[0].argmax()/300)))
                    #print("what is confidence",confidence)
                    #print("name iss",name)
                    #print("type of name",type(name))
                    #print("length of name",len(name)
                        
                        
                    # Display the label
                except:
                    le=2
                # Show the frame
            cv2.imshow("Image", frame)
            c = cv2.waitKey(1)
            
            if (c & 0xFF == ord('q')):
                break     

        self.stream.release()
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        cv2.waitKey(1)

    



if __name__ == "__main__":
    root=Tk()
    obj=Recognition(root)
    root.mainloop()
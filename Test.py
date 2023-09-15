import numpy as np
from tkinter import *
from PIL import ImageTk, Image
import cv2
import os
import h5py
import mysql.connector

import dlib
from imutils import face_utils
from keras.models import load_model
import sys
from PIL import Image
import h5py
import dlib
from imutils import face_utils
from keras.models import load_model
import sys
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D,Dropout,BatchNormalization
from keras.layers import Dense, Activation, Flatten
from keras.utils import to_categorical
from keras import backend as K 
from sklearn.model_selection import train_test_split
from tkinter import messagebox
from time import strftime
from datetime import datetime

cascPath = "C:\\Users\\Mubashir\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\cv2\data\\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
font = cv2.FONT_HERSHEY_SIMPLEX

class test:
    def __init__(self):
        
        self.start()

    def mark_attendance(self,i,r,n):
        with open("attendance.csv","r+",newline="\n") as f:
            print("attendance")
            myDatalist=f.readlines()
            print("ahsudhushauhd",myDatalist)
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")

    def getImagesAndLabels(self,path):
        
        #path = 'D:\Bushi\Dummy of Project\Dummy of Project\Face_Recognition\dataset'
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
        faceSamples=[]
        ids = []
        for imagePath in imagePaths:

            #if there is an error saving any jpegs
            try:
                PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
            except:
                continue  
            img_numpy = np.array(PIL_img,'uint8')

            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faceSamples.append(img_numpy)
            ids.append(id)  
        return faceSamples,ids
    

    def model(self,input_shape,num_classes):
   
        model = Sequential()

        model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=input_shape))
        model.add(BatchNormalization()) #----------------
        model.add(Conv2D(64, kernel_size=3, activation='relu'))
        model.add(BatchNormalization()) #----------------
        model.add(Conv2D(64, kernel_size=5, padding='same', activation='relu'))
        model.add(BatchNormalization()) #----------------
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.2)) #----------------

        model.add(Conv2D(128, kernel_size=3, activation='relu'))
        model.add(BatchNormalization())
        model.add(Conv2D(128, kernel_size=3, activation='relu'))
        model.add(BatchNormalization())
        model.add(Conv2D(128, kernel_size=5, padding='same', activation='relu'))
        model.add(BatchNormalization())
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.2))

        model.add(Conv2D(256, kernel_size=3, activation='relu'))
        model.add(BatchNormalization())
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.2))

        model.add(Flatten())
        model.add(Dense(num_classes))
        model.add(BatchNormalization())
        model.add(Dense(num_classes, activation='softmax'))

        model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

        model.summary()
        return model

    def start(self):
        path = 'D:\Bushi\Dummy of Project\data'
        _,ids = self.getImagesAndLabels(path)
        print("ksndujnsdsd",ids)
        model = self.model((32,32,1),len(set(ids)))
        model.load_weights  ('D:\Bushi\Dummy of Project/transfer_learning_trained_face_cnn_model.h5', by_name = True, skip_mismatch = True)
        model.summary()
        cap = cv2.VideoCapture(0)
        print('here')
        ret = True

        clip = []
        while ret:
            #read frame by frame
            ret, frame = cap.read()
            nframe = frame
            faces = faceCascade.detectMultiScale(frame,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30))

            try:
                (x,y,w,h) = faces[0]
            except:
                continue
            frame = frame[y:y+h,x:x+w]
            frame = cv2.resize(frame, (32,32))
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #cv2.imshow('result small' , frame)
            c= cv2.waitKey(1)
            if c & 0xFF == ord('q'):
                break
            
            gray = gray[np.newaxis,:,:,np.newaxis]
            gray = gray.reshape(-1, 32, 32, 1).astype('float32') / 255.
            #print(gray.shape)
            prediction = model.predict(gray)
            #confidence=int((100*(1-prediction/300)))
            print("prediction:" + str(prediction))
            #print("prediction:" + str(confidence))


            

            print("\n\n\n\n")
            print("----------------------------------------------")
            print('ekdnnfhndhnf',set(ids))
            get_employees = list(ids)

            labels = ['George W Bush' ,'Rishabh','Mubbasher','Adnan']
            prediction = prediction.tolist()
            print("What is prediction 0 ",prediction[0])
            
            listv = prediction[0]
            n = listv.index(max(listv))
            print("\n")
            print("----------------------------------------------")
            #print( "Highest Probability: " + labels[n] + "==>" + str(prediction[0][n]) )
            print( "Highest Probability: " + "User " + str(n) + "==>" + str(prediction[0][n]) )
            prediction = np.argmax(model.predict(gray), 1)
            confidence=int((100*(1-prediction/300)))
            print("Confidence",confidence)
            print("Confidence",prediction)
            maximum=n
            print("----------------------------------------------")
            print("\n")
            for (x, y, w, h) in faces:
                try:
                    print("does is comes here nnnn value",maximum)
                    #cv2.rectangle(nframe, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    #cv2.putText(nframe, str(labels[n]), (x+5,y-5), font, 1, (255,255,255), 2)
                    conn = mysql.connector.connect(username='root', password='root',host='localhost',database='employee_management')
                    cursor = conn.cursor()
                    
                    cursor.execute("select emp_name from employee_attendance where emp_id="+str(maximum))

                    n=cursor.fetchone()
                    print("fuck", n)
                    n="+".join(n)
                    print("type of 9 is",type(n))
                    print("pehla hgayaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",n)

                    cursor.execute("select emp_roll from employee_attendance where emp_id="+str(maximum))
                    r=cursor.fetchone()
                    r="+".join(r)
                    print("dosra hgayaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",r)

                    #cursor.execute("select emp_id from employee_attendance where emp_id="+str(maximum))
                    #i=cursor.fetchone()
                    #i="+".join(i)
                    print("tesra hgayaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                    

                    print("does is comes here last")
                    if confidence > 77:
                        print("does is comes here 123")
                        cv2.rectangle(nframe, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        cv2.putText(nframe,f"emp_id:{maximum}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                        cv2.putText(nframe,f"emp_name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                        cv2.putText(nframe,f"emp_roll:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                        self.mark_attendance(maximum,r,n)
                    else:
                 
                        cv2.rectangle(nframe,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(nframe,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)
                        #cv2.putText(nframe, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
                except:
                    la = 2 
            prediction = np.argmax(model.predict(gray), 1)
            confidence=int((100*(1-prediction/300)))
            print(prediction)
            cv2.imshow('result', nframe)
            c = cv2.waitKey(1)
            if c & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    
    
if __name__ == "__main__":
    test()
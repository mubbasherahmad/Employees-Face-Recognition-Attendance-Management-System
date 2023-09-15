import cv2
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import pandas as pd
import matplotlib as plt
import tensorflow
import os
from imutils import face_utils
from keras.models import load_model
import sys
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D,Dropout,BatchNormalization
from keras.layers import Dense, Activation, Flatten
from keras.utils import to_categorical
from keras import backend as K 
from sklearn.model_selection import train_test_split
import cv2
import os
from tkinter import messagebox
import h5py
import dlib
from tkinter import ttk# 
from imutils import face_utils
from keras.models import load_model
import sys
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D,Dropout
from keras.layers import Dense, Activation, Flatten
from keras.utils import to_categorical
from keras import backend as K 
from sklearn.model_selection import train_test_split
from keras import callbacks

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("C:\\Users\\Mubashir\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\cv2\data\\haarcascade_frontalface_default.xml")

class train:
    def __init__(self):
        df = pd.read_csv('D:\Bushi\Dummy of Project/final_df.csv', index_col=0)
        path = 'D:\Bushi\Dummy of Project\Datasets\data/'
        print("hello")
        print ("\n [INFO] Training faces now.")
        faces,ids = self.getImagesAndLabels(path)
        print("hello",len(ids))

        K.clear_session()
        n_faces = len(set(ids))
        train_model = self.model((100,100,1),n_faces)
        #train_model = self.model()
        

        faces = np.asarray(faces,dtype="object")
        print("hello",type(faces))
        print("hello",len(faces))
        print("hello",faces)
        faces = np.asarray([self.downsample_image(ab) for ab in faces])
        ids = np.asarray(ids)
       
        faces = faces[:,:,:,np.newaxis]
        print("Shape of Data: " + str(faces.shape))
        print("Number of unique faces : " + str(n_faces))


        ids = to_categorical(ids)
        print("iddssss",ids)

        faces = faces.astype('float32')
        faces /= 255.

        x_train, x_test, y_train, y_test = train_test_split(faces,ids, test_size = 0.2, random_state = 123)

        checkpoint = callbacks.ModelCheckpoint('D:\Bushi\Dummy of Project\Dummy of Project\Face_Recognition/trained_model.h5',save_best_only=True, monitor='val_accuracy', save_weights_only=True, verbose=1)
                                            
        train_model.fit(x_train, y_train,
                    batch_size=128,
                    epochs=10,
                    verbose=1,
                    validation_data=(x_test, y_test),
                    shuffle=True,callbacks=[checkpoint])
                    
      
        # Print the numer of faces trained and end program
        # Plot training & test accuracy values
        plt.plot(train_model.history['acc'])
        plt.plot(train_model.history['val_acc'])
        plt.title('Model accuracy')
        plt.ylabel('Accuracy')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Test'], loc='upper left')
        plt.show()

        # Plot training & test loss values
        plt.plot(train_model.history['loss'])
        plt.plot(train_model.history['val_loss'])
        plt.title('Model loss')
        plt.ylabel('Loss')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Test'], loc='upper left')
        plt.show()

        from sklearn.metrics import confusion_matrix,f1_score, precision_score, recall_score
        import seaborn as sn
        y_true = np.argmax(y_test, axis=1)
        y_pred = np.argmax(self.model.predict(x_test), axis=1)
        data = confusion_matrix(y_true, y_pred)
        df_cm = pd.DataFrame(data, columns=np.unique(y_true), index = np.unique(y_true))
        df_cm.index.name = 'Actual'
        df_cm.columns.name = 'Predicted'
        plt.figure(figsize = (10,7))
        sn.set(font_scale=1.4)#for label size
        sn.heatmap(df_cm, cmap="Blues", annot=True,annot_kws={"size": 16})#



        messagebox.showinfo("Result","Training Dataset Complated!",parent=Toplevel())
        print("\n [INFO] " + str(n_faces) + " faces trained. Exiting Program")
    
    # function to get the images and label data
    def getImagesAndLabels(self,path):
        # Path for face image databasw
        path = 'D:\Bushi\Dummy of Project\Datasets\data/'
        
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
        faceSamples=[]
        ids = []


        for imagePath in imagePaths:
            #print(imagePath)
            #if there is an error saving any jpegs
            try:
                PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
            except:
                continue   
            img_numpy = np.array(PIL_img,'uint8')
            print(img_numpy)
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faceSamples.append(img_numpy)
            ids.append(id)
        return faceSamples,ids
   
    def downsample_image(self,img):
        img = Image.fromarray(img.astype('uint8'), 'L')
        img = img.resize((100,100), Image.LANCZOS)
        return np.array(img)

    def model(self,shape,num_faces):
   
        model = Sequential()

        model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=shape))
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
        model.add(Dense(256))
        model.add(BatchNormalization())
        model.add(Dense(128))
        model.add(BatchNormalization())
       #
        model.add(Dense(num_faces, activation='softmax'))
        model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

        model.summary()
        return model
    


    
if __name__ == "__main__":
    train()
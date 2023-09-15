from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
from keras.optimizers import RMSprop
from keras.callbacks import ModelCheckpoint, EarlyStopping
import cv2
import numpy as np
from tkinter import messagebox
from keras.callbacks import EarlyStopping
from keras_vggface.vggface import VGGFace
import numpy as np
import keras.utils as image
from keras_vggface import utils
import os
import pandas as pd
import numpy as np
import tensorflow as tf
import keras as keras
import matplotlib.pyplot as plt

from keras.layers import Dense, GlobalAveragePooling2D


from keras.applications.mobilenet import preprocess_input

from keras.preprocessing.image import ImageDataGenerator

from keras.models import Model

from keras.optimizers import Adam

class Train:
    alive=False 
    def destroy(self):
        # Restore the attribute on close.
        print("destroy ma ni aya")
        self.__class__.alive = False
        
       

    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1920x1088+0+0")
        self.root.title("Train Pannel")
        self.__class__.alive = True
        root.protocol("WM_DELETE_WINDOW", self.destroy())

        
        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\Mubashir\Downloads\banner.jpg")
        img=img.resize((1920,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1920,height=130)

        # backgorund image 
        bg1=Image.open(r"C:\Users\Mubashir\Downloads\bg2.jpg")
        bg1=bg1.resize((1920,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1920,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Image Training Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=-200,y=0,width=1920,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"C:\Users\Mubashir\Downloads\2401770.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.train_classifier,image=self.std_img1,cursor="hand2")
        std_b1.place(x=680,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.train_classifier,text="Train Dataset",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=680,y=350,width=180,height=45)

    # ==================Create Function of Traing===================
        

        
    def train_classifier(self):
        train_data_dir = 'D:\Bushi\Dummy of Project\Datasets/train'
        validation_data_dir = 'D:\Bushi\Dummy of Project\Datasets/validation'
        test_data_dir = 'D:\Bushi\Dummy of Project\Datasets/test'
        # Create data generators for train, validation, and test
        train_datagen =  train_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)
        train_generator = train_datagen.flow_from_directory(train_data_dir,
                                            target_size=(224,224),color_mode='rgb',batch_size=32,
                                            class_mode='categorical',shuffle=True)

        validation_datagen = train_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)
        validation_generator =  validation_datagen.flow_from_directory(validation_data_dir,
                                            target_size=(224,224),color_mode='rgb',batch_size=32,
                                            class_mode='categorical',shuffle=True)
        test_datagen = train_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)

        test_generator =  test_datagen.flow_from_directory(test_data_dir,
                                            target_size=(224,224),color_mode='rgb',batch_size=32,
                                            class_mode='categorical',shuffle=True)
        

        train_generator.class_indices.values()
        # dict_values([0, 1, 2])
        NO_CLASSES = len(train_generator.class_indices.values())

        

        base_model = VGGFace(include_top=False,
            model='vgg16',
            input_shape=(224, 224, 3),
            weights='vggface')
        base_model.summary()


        print(len(base_model.layers))
        # 26 layers in the original VGG-Face

        
        x = base_model.output
        x = GlobalAveragePooling2D()(x)

        x = Dense(1024, activation='relu')(x)
        x = Dense(1024, activation='relu')(x)
        x = Dense(512, activation='relu')(x)


        # final layer with softmax activation
        preds = Dense(NO_CLASSES, activation='softmax')(x)

        # create a new model with the base model's original input and the 
        # new model's output
        model = Model(inputs = base_model.input, outputs = preds)
        model.summary()
        import os
        import cv2
        import numpy as np
        

        # don't train the first 19 layers - 0..18
        for layer in model.layers[:19]:
            layer.trainable = False

        # train the rest of the layers - 19 onwards
        for layer in model.layers[19:]:
            layer.trainable = True


        model.compile(optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy'])
        checkpoint = ModelCheckpoint('transfer_learning_trained' +'_face_cnn_model_pangay_latest-0.h5',
                             monitor="val_loss",
                             mode="min",
                             save_best_only = True,
                             verbose=1)
        early_stopping = EarlyStopping(
                            monitor='val_loss',     # Metric to monitor (e.g., 'val_loss' or 'val_accuracy')
                            patience=5,             # Number of epochs with no improvement after which training will be stopped
                            restore_best_weights=True) 
        callbacks = [early_stopping, checkpoint]

        model.fit(train_generator,validation_data=validation_generator,batch_size = 20,verbose = 1,epochs =1,callbacks=callbacks)
        # creates a HDF5 file
        model.save('transfer_learning_trained' +'_face_cnn_model_pangay_latest-0.h5')
        test_loss, test_accuracy = model.evaluate(test_generator)
        print("Test Accuracy:", test_accuracy)


        import pickle

        class_dictionary = train_generator.class_indices
        class_dictionary = {
            value:key for key, value in class_dictionary.items()
        }
        print(class_dictionary)

        # save the class dictionary to pickle
        face_label_filename = 'face-labels-pangay-latest-0.pickle'
        with open(face_label_filename, 'wb') as f: pickle.dump(class_dictionary, f)
        messagebox.showinfo("Result","Training Dataset Complated!",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    
    obj=Train(root)
    root.mainloop()
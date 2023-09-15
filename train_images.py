from sys import path

import numpy as np
import keras.utils as image
from keras_vggface.vggface import VGGFace
from keras_vggface import utils
import os
import pickle
import pandas as pd
import numpy as np
import tensorflow as tf
import keras as keras
import matplotlib.pyplot as plt
import cv2 as cv2
from sklearn.preprocessing import normalize

from keras.layers import Dense, GlobalAveragePooling2D


from keras.applications.mobilenet import preprocess_input

from keras.preprocessing.image import ImageDataGenerator

from keras.models import Model

from keras.optimizers import Adam

from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from keras.callbacks import EarlyStopping
from keras_vggface.vggface import VGGFace

model = VGGFace(model='senet50')
import numpy as np
import keras.utils as image
from keras_vggface.vggface import VGGFace
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
        title_lb1 = Label(bg_img,text="Welcome to Image Training Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=-200,y=0,width=1920,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"D:\Bushi\Employees Face Recognition System\icons\2401770.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.train_classifier,image=self.std_img1,cursor="hand2")
        std_b1.place(x=680,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.train_classifier,text="Train Dataset",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=680,y=350,width=180,height=45)

    # ==================Create Function of Traing===================
       

        
    def train_classifier(self):
        train_datagen = ImageDataGenerator(
            preprocessing_function=preprocess_input)

        train_generator = \
            train_datagen.flow_from_directory('D:\Bushi\Employees Face Recognition System\dataset',
                                            target_size=(224,224),color_mode='rgb',batch_size=32,
                                            class_mode='categorical',shuffle=True)

        train_generator.class_indices.values()
        # dict_values([0, 1, 2])
        NO_CLASSES = len(train_generator.class_indices.values())

        

        base_model = VGGFace(include_top=False,
            model='vgg16',
            input_shape=(224, 224, 3))
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

        # don't train the first 19 layers - 0..18
        for layer in model.layers[:19]:
            layer.trainable = False

        # train the rest of the layers - 19 onwards
        for layer in model.layers[19:]:
            layer.trainable = True


        model.compile(optimizer='Adam',
            loss='categorical_crossentropy',
            metrics=['accuracy'])

        model.fit(train_generator,
        batch_size = 16,
        verbose = 1,
        epochs = 1)
        # creates a HDF5 file
        model.save('D:\\Bushi\\Employees Face Recognition System\\trained model\\'+'transfer_learning_trained' + '_face_cnn_model-testing.h5')


        class_dictionary = train_generator.class_indices
        class_dictionary = {
            value:key for key, value in class_dictionary.items()
        }
        print(class_dictionary)

        # save the class dictionary to pickle
        face_label_filename ='D:\\Bushi\\Employees Face Recognition System\\trained model\\'+ 'face-labels-testing.pickle'
        with open(face_label_filename, 'wb') as f: pickle.dump(class_dictionary, f)
        def preprocess_image(image):
            image = cv2.resize(image, (224, 224))
            image = preprocess_input(image)
            return image
        def calculate_embedding(image):
            preprocessed_image = preprocess_image(image)
            embedding = model.predict(np.expand_dims(preprocessed_image, axis=0))
            return embedding

        # Directory containing face images of different individuals
        base_dataset_dir = 'D:\Bushi\Employees Face Recognition System\dataset'  # Replace with your base dataset directory

        # List of directories corresponding to different individuals
        person_directories = os.listdir(base_dataset_dir)

        known_embeddings = []
        known_identities = []

        # Iterate through each person's directory
        for person_dir in person_directories:
            person_path = os.path.join(base_dataset_dir, person_dir)
            if os.path.isdir(person_path):
                embeddings = []
                for image_name in os.listdir(person_path):
                    image_path = os.path.join(person_path, image_name)
                    image = cv2.imread(image_path)
                    preprocessed_image = preprocess_image(image)
                    embedding = base_model.predict(np.expand_dims(preprocessed_image, axis=0))
                    #print("values of embeddings during",embedding)
                    embeddings.append(embedding)
                known_embeddings.extend(embeddings)
                known_identities.extend([person_dir] * len(embeddings))  # Assign the person's identity to each embedding

        # Convert lists to numpy arrays
        known_embeddings = np.array(known_embeddings)
        known_embeddings_2d = known_embeddings.reshape(known_embeddings.shape[0], -1)
        known_embeddings_normalized = normalize(known_embeddings_2d, axis=1, norm='l2')
        #print("Embeddings before",known_embeddings)

        #num_embeddings = known_embeddings.shape[0]
        #embedding_dimension = np.prod(known_embeddings.shape[1:])
        #embedding_array = known_embeddings.reshape(num_embeddings, embedding_dimension)
        #known_embeddings_normalized = normalize(embedding_array, axis=1, norm='l2')
        known_identities = np.array(known_identities)
        

# Assuming you have 'known_embeddings' and 'known_identities' arrays

        # Define the file paths
        embeddings_file_path = 'D:\\Bushi\\Employees Face Recognition System\\trained model\\known_embeddings-1.pkl'
        identities_file_path = 'D:\\Bushi\\Employees Face Recognition System\\trained model\\known_identities-1.pkl'

        # Save known embeddings using pickle
        with open(embeddings_file_path, 'wb') as embeddings_file:
            pickle.dump(known_embeddings_normalized, embeddings_file)

        # Save known identities using pickle
        with open(identities_file_path, 'wb') as identities_file:
            pickle.dump(known_identities, identities_file)
        
        
        
        
        messagebox.showinfo("Result","Training Dataset Complated!",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    
    obj=Train(root)
    root.mainloop()
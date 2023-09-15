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


class training:
    alive=False
    def destroy(self):
        # Restore the attribute on close.
        self.__class__.alive = False
        return super().destroy()
    
    def __init__(self):
        self.__class__.alive = True
        img = image.load_img('D:\Bushi\Dummy of Project\Dummy of Project\Face_Recognition/Matthias_Sammer.png', target_size=(224, 224))
        model = VGGFace(model='senet50')
        # prepare the image
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = utils.preprocess_input(x, version=1)

        # perform prediction
        preds = model.predict(x)
        print('Predicted:', utils.decode_predictions(preds))

        

        train_datagen = ImageDataGenerator(
            preprocessing_function=preprocess_input)

        train_generator = \
            train_datagen.flow_from_directory('D:\Bushi\Dummy of Project\Datasets',
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
        batch_size = 20,
        verbose = 1,
        epochs = 1)
        # creates a HDF5 file
        model.save(
            'transfer_learning_trained' +
            '_face_cnn_model.h5')


        import pickle

        class_dictionary = train_generator.class_indices
        class_dictionary = {
            value:key for key, value in class_dictionary.items()
        }
        print(class_dictionary)

        # save the class dictionary to pickle
        face_label_filename = 'face-labels.pickle'
        with open(face_label_filename, 'wb') as f: pickle.dump(class_dictionary, f)

if __name__ == "__main__":
    training()
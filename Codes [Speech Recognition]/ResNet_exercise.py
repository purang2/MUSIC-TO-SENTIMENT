# -*- coding: utf-8 -*-


import tensorflow as tf 
from tensorflow import keras
from sklearn.datasets import load_sample_image
import numpy as np 


china = load_sample_image("china.jpg") /255
flower = load_sample_image("flower.jpg") /255 

images= np.array( [china,flower] )


#ResNet-50 Model expects 224 x 224 size image
images_resized = tf.image.resize(images, [224,224])

inputs = keras.applications.resnet50.preprocess_input(images_resized * 255)

Y_prob = model.predict(inputs)

top_K = keras.applications.resnet50.decode_predictions(Y_proba, top=3)
for image_index in range(len(images)):
    print("이미지 #{}".format(image_index))
    for class_id, name, y_prob in top_K[image_index]:
        print("    {} - {:12s} {:.2f}%".format(class_id, name, y_prob *100))
    print()
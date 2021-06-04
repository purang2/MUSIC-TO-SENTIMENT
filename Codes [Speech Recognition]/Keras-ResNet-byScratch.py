<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 16:44:59 2021


# ResNet 핸즈온 머신러닝 Keras 구현 코드를 copy하여 변형함

@author: PC
"""

import tensorflow as tf 
from tensorflow import keras
from sklearn.datasets import load_sample_image
import numpy as np 

from tensorflow.keras import datasets, layers, models

import cv2 #OpenCV for load images

import os, re, glob

from sklearn.model_selection import train_test_split


#ResNet 2015를 직접 구현 
class ResidualUnit(keras.layers.Layer):
    def __init__(self,filters,strides=1,activation="relu", **kwargs):
        super().__init__(**kwargs)
        self.activation = keras.activations.get(activation)
        self.main_layers = [
            keras.layers.Conv2D(filters,3,strides=strides,
                                padding="same",use_bias =False),
            keras.layers.BatchNormalization(),
            self.activation,
            keras.layers.Conv2D(filters,3,strides=1,
                                padding="same",use_bias =False),
            keras.layers.BatchNormalization()]
        
        self.skip_layers = []
        if strides > 1:
            self.skip_layers = [
                    keras.layers.Conv2D(filters,1,strides=strides,
                                        padding="same", use_bias=False),
                    keras.layers.BatchNormalization()]
    
    def call(self, inputs):
        Z = inputs 
        for layer in self.main_layers:
            Z = layer(Z)
        skip_Z = inputs 
        
        for layer in self.skip_layers:
            skip_Z =layer(skip_Z)
        
        return self.activation(Z + skip_Z)
    
            

#load Dataset 

X_train, X_test, Y_train, Y_test = np.load('../img_data.npy',allow_pickle=True)        


'''
    
#uses

model = keras.models.Sequential()
model.add(keras.layers.Conv2D(64, 7, strides=2, input_shape=[224,224,3],
                              padding="same", use_bias=False))
model.add(keras.layers.BatchNormalization())
model.add(keras.layers.Activation("relu"))
model.add(keras.layers.MaxPool2D(pool_size=3, strides=2, padding="same"))

prev_filters = 64

# [64,64,64,128,128,128,128,256,.....,512,...]
for filters in [64] * 3 + [128] * 4 + [256] * 6  + [512] * 3:
    strides = 1 if filters == prev_filters else 2
    model.add(ResidualUnit(filters, strides=strides))
    prev_filters = filters 
model.add(keras.layers.GlobalAvgPool2D())
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(10, activation="softmax"))



'''





            
=======
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 16:44:59 2021


# ResNet 핸즈온 머신러닝 Keras 구현 코드를 copy하여 변형함

@author: PC
"""

import tensorflow as tf 
from tensorflow import keras
from sklearn.datasets import load_sample_image
import numpy as np 

from tensorflow.keras import datasets, layers, models

import cv2 #OpenCV for load images

import os, re, glob

from sklearn.model_selection import train_test_split


#ResNet 2015를 직접 구현 
class ResidualUnit(keras.layers.Layer):
    def __init__(self,filters,strides=1,activation="relu", **kwargs):
        super().__init__(**kwargs)
        self.activation = keras.activations.get(activation)
        self.main_layers = [
            keras.layers.Conv2D(filters,3,strides=strides,
                                padding="same",use_bias =False),
            keras.layers.BatchNormalization(),
            self.activation,
            keras.layers.Conv2D(filters,3,strides=1,
                                padding="same",use_bias =False),
            keras.layers.BatchNormalization()]
        
        self.skip_layers = []
        if strides > 1:
            self.skip_layers = [
                    keras.layers.Conv2D(filters,1,strides=strides,
                                        padding="same", use_bias=False),
                    keras.layers.BatchNormalization()]
    
    def call(self, inputs):
        Z = inputs 
        for layer in self.main_layers:
            Z = layer(Z)
        skip_Z = inputs 
        
        for layer in self.skip_layers:
            skip_Z =layer(skip_Z)
        
        return self.activation(Z + skip_Z)
    
            

#load Dataset 

X_train, X_test, Y_train, Y_test = np.load('../img_data.npy',allow_pickle=True)        


'''
    
#uses

model = keras.models.Sequential()
model.add(keras.layers.Conv2D(64, 7, strides=2, input_shape=[224,224,3],
                              padding="same", use_bias=False))
model.add(keras.layers.BatchNormalization())
model.add(keras.layers.Activation("relu"))
model.add(keras.layers.MaxPool2D(pool_size=3, strides=2, padding="same"))

prev_filters = 64

# [64,64,64,128,128,128,128,256,.....,512,...]
for filters in [64] * 3 + [128] * 4 + [256] * 6  + [512] * 3:
    strides = 1 if filters == prev_filters else 2
    model.add(ResidualUnit(filters, strides=strides))
    prev_filters = filters 
model.add(keras.layers.GlobalAvgPool2D())
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(10, activation="softmax"))



'''





            
>>>>>>> c71b5c5ab1f616eab67c157445af5220992cd27d
        
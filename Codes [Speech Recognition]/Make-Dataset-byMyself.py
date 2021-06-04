<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 17:13:54 2021

@author: PC



To Make my dateset[image-Label]
"""
import os, re, glob
import cv2
import numpy as np
from sklearn.model_selection import train_test_split


folder_path = '../Data/images_original/'


categories = ['blues','classical','country','disco','hiphop',
              'jazz','metal','pop','reggae','rock']

num_classes = len(categories)


# Resizing 432 x 288  -> 224 x 224 [for ResNet]
 

image_w = 224
image_h = 224 

X = []
Y = []

for index, category in enumerate(categories):
    label = [0 for i in range(num_classes)]
    label[index] = 1
    image_dir = folder_path + category +'/'
    
    for top, dir, f in os.walk(image_dir):
        for filename in f:
            print(image_dir+filename)
            img = cv2.imread(image_dir + filename)
            img = cv2.resize(img, None, fx=image_w/img.shape[0], fy = image_h/img.shape[1])
            X.append(img/256)
            Y.append(label)
            
            
X = np.array(X)
Y = np.array(Y)


X_train, X_test, Y_train, Y_test = train_test_split(X,Y)
xy = (X_train, X_test, Y_train, Y_test)


np.save("../img_data.npy", xy) #. npy 파일 => numpy format의 파일 


=======
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 17:13:54 2021

@author: PC



To Make my dateset[image-Label]
"""
import os, re, glob
import cv2
import numpy as np
from sklearn.model_selection import train_test_split


folder_path = '../Data/images_original/'


categories = ['blues','classical','country','disco','hiphop',
              'jazz','metal','pop','reggae','rock']

num_classes = len(categories)


# Resizing 432 x 288  -> 224 x 224 [for ResNet]
 

image_w = 224
image_h = 224 

X = []
Y = []

for index, category in enumerate(categories):
    label = [0 for i in range(num_classes)]
    label[index] = 1
    image_dir = folder_path + category +'/'
    
    for top, dir, f in os.walk(image_dir):
        for filename in f:
            print(image_dir+filename)
            img = cv2.imread(image_dir + filename)
            img = cv2.resize(img, None, fx=image_w/img.shape[0], fy = image_h/img.shape[1])
            X.append(img/256)
            Y.append(label)
            
            
X = np.array(X)
Y = np.array(Y)


X_train, X_test, Y_train, Y_test = train_test_split(X,Y)
xy = (X_train, X_test, Y_train, Y_test)


np.save("../img_data.npy", xy) #. npy 파일 => numpy format의 파일 


>>>>>>> c71b5c5ab1f616eab67c157445af5220992cd27d

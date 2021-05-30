# -*- coding: utf-8 -*-
"""

# 음악장르 분류 알고리즘 by Blog 

@author: purang2
"""

import pandas as pd 
import sklearn 
import librosa 
import numpy as np 
from sklearn.model_selection import train_test_split 



import IPython.display as ipd 
import matplotlib.pyplot as plt
import librosa.display


df = pd.read_csv('../Data/features_3_sec.csv')

#print(df.head())


X = df.drop(columns=['filename','length','label'])
y = df['label'] #장르명

scaler = sklearn.preprocessing.MinMaxScaler()
np_scaled = scaler.fit_transform(X)


X = pd.DataFrame(np_scaled, columns=X.columns)

print(X.head())   


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2,random_state=2021)

print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)


#학습 및 검증 


from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score 

xgb = XGBClassifier(n_estimators=1000, learning_rate=0.05)
xgb.fit(X_train, y_train) #학습 

y_preds = xgb.predict(X_test) #검증 

print('Accuracy: %.2f' %accuracy_score(y_test,y_preds))


#Confusion Matrix로 보는 성능 시각화 

from sklearn.metrics import confusion_matrix 
import seaborn as sns 
cm = confusion_matrix(y_test,y_preds)

plt.figure(figsize=(16,9))
sns.heatmap(
    cm,
    annot=True,
    xticklabels=["blues","classical","country","disco","hiphop","jazz","metal","pop","reggae","rock"],
    yticklabels=["blues","classical","country","disco","hiphop","jazz","metal","pop","reggae","rock"]
)
plt.show()







# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 21:58:39 2017

@author: new
"""
import pandas as pd
from sklearn import preprocessing,cross_validation,neighbors
import numpy as np
df=pd.read_csv("D:/machine learning/Pokemon.csv")
df.replace('?',-9999,inplace=True)
df.drop(['Defense'],1,inplace=True)

#X=np.array(df.drop['Legendary'],1)
#y=df['Name']

for y in df['Name']:
    
X=np.array(df['Name'])
y=np.array(df['Legendary'])
X = np.atleast_2d(X).T

X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.1)
#knn = KNeighborsClassifier()
clf=neighbors.KNeighborsClassifier(n_neighbors=9)
#X_train, y_train = X[:, :-1], Y[:, -1]
print(X)
print(y)
clf.fit(X_train,y_train)
g=clf.predict("a")
acc=clf.score(X_train,y_train)
print(g)
print(acc)
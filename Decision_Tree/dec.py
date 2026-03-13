#Decision tree classifier with restaurant eaitring problem

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,classification_report

df=pd.read_csv('restaurant_waiting_dataset.csv')
print(df.sample(5))


le=LabelEncoder()

for column in df.columns:
    df[column]=le.fit_transform(df[column])
print("data after Label Encoder:\n",df)

X=df.drop('Wait',axis=1)
y=df['Wait']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=DecisionTreeClassifier()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print("Decision Tree interpretation")
print("Acuracy Score:",accuracy_score(y_test,y_pred))
print("Recall Score:",recall_score(y_test,y_pred))
print("Precision Score:",precision_score(y_test,y_pred))
print("Classification report Score:",classification_report(y_test,y_pred))

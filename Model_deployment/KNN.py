import numpy as np
import pandas as pd

training_data = pd.read_csv('/Users/avinashronanki/Downloads/ml_classification/storepurchasedata.csv') # load it into pandas 

training_data.describe() # stat info the data 

X = training_data.iloc[:, :-1].values # independent variables 
y = training_data.iloc[:,-1].values   # dependent variable 

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =.20,random_state=0)  # splitting the data 80:20 train/test

from sklearn.preprocessing import StandardScaler # scaling the data 
sc = StandardScaler() 
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier
# minkowski is for ecledian distance
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2) # model

# Model training
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
y_prob = classifier.predict_proba(X_test)[:,1] #probability of the purchase 

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred) 

from sklearn.metrics import accuracy_score

print(accuracy_score(y_test,y_pred)) # 0.875


from sklearn.metrics import classification_report

print(classification_report(y_test,y_pred)) # precision , recall and F1 score 


new_prediction = classifier.predict(sc.transform(np.array([[40,20000]]))) #  new value for testing the model

new_prediction_proba = classifier.predict_proba(sc.transform(np.array([[40,20000]])))[:,1] # probablity 

new_pred = classifier.predict(sc.transform(np.array([[42,50000]]))) #test2 

new_pred_proba = classifier.predict_proba(sc.transform(np.array([[42,50000]])))[:,1] #test2 



#Picking the Model and Standard Scaler

import pickle

model_file = "classifier.pickle" # kn model 

pickle.dump(classifier, open(model_file,'wb')) #(binary file )

scaler_file = "sc.pickle" # scalar object 

pickle.dump(sc, open(scaler_file,'wb')) #(binary file )
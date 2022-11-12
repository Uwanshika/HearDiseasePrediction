import pandas  as pandas
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("hello Wolrd")
heartData = pandas.read_csv('heart.csv')
print(heartData['target'].value_counts())
X = heartData.drop(columns ='target',axis = 1)
Y = heartData['target']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, stratify = Y, random_state = 0)

print(X.shape, X_train.shape, X_test.shape)
# Training the Random Forest model with Training data
RandomForestClassifiermodel =  RandomForestClassifier()
RandomForestClassifiermodel.fit(X_train, Y_train)

# training data accuracy
X_train_prediction_RandomForestClassifier = RandomForestClassifiermodel.predict(X_train)

#   git config --global user.email "shashiuwanshi97@gmail.com"
#   git config --global user.name "ShashiniU"


# test data accuracy
X_test_prediction_RandomForestClassifier = RandomForestClassifiermodel.predict(X_test)
training_data_accuracy_RandomForestClassifier = accuracy_score(X_train_prediction_RandomForestClassifier, Y_train)
print('Accuracy on training data Random Forest model : ', training_data_accuracy_RandomForestClassifier)
print('Random Forest : ' ,round( training_data_accuracy_RandomForestClassifier*100,2),'%')
testing_data_accuracy_RandomForestClassifier = accuracy_score(X_test_prediction_RandomForestClassifier, Y_test)
print('Accuracy on testing data Random Forest model : ', testing_data_accuracy_RandomForestClassifier)
print('Random Forest : ' ,round( testing_data_accuracy_RandomForestClassifier*100,2),'%')

input_data = (56,0,0,134,409,0,0,150,1,1.9,1,2,3)
#change input data to numpy array

input_data_as_numpy_array = np.asarray(input_data)

#reshape numpy array
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction_RandomForestClassifiermodel = RandomForestClassifiermodel.predict(input_data_reshaped)

print(prediction_RandomForestClassifiermodel)

if(prediction_RandomForestClassifiermodel[0] == 0):
  print('No heart disease')  
else:
  print('Patient have heart disease')


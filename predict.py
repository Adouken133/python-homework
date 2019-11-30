from sklearn.datasets import load_wine
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

wine = load_wine()
columns_names = wine.feature_names

x = wine.data
y = wine.target

x_train, x_test, y_train,y_test = train_test_split(x,y, test_size=0.35)

LR = LogisticRegression()
LR.fit(x_train, y_train)

#Predicting the results for our test
Predicted_test_values = LR.predict(x_test)

#printing the residuals: difference between real and predicted
for(real, predicted) in list(zip(y_test, Predicted_test_values)):
    print(f'Value:{real}, pred:{predicted} {"is different" if real != predicted else""}')

#printing the Classification report
from sklearn.metrics import classification_report, confusion_matrix, f1_score
print('Classification Report')
print(classification_report(y_test, Predicted_test_values))

#printing the confusion matrix
print('confusion_matrix')
print(confusion_matrix(y_test, Predicted_test_values))

print the F1 Score
print('F1_score')
print(f1_score(y_test, Predicted_test_values, average="macro"))

from sklearn.model_selection import cross_val_score, ShuffleSplit
print(cross_val_score(LR, x, y, cv=5))


# Cross validation using shuffle split
cv = ShuffleSplit(n_splits=5)
print(cross_val_score(LR, x, y, cv=cv))


# Output of the training is a model
#print(f"Intercept per class: {LR.intercept_}\n")
#print(f"Coeficients per class: {LR.coef_}\n")

#print(f"Available classes: {LR.classes_}\n")
#print(f"Named Coeficients for class 0: {pd.DataFrame(LR.coef_[0], columns_names)}\n")
#print(f"Named Coeficients for class 1: {pd.DataFrame(LR.coef_[1], columns_names)}\n")
#print(f"Named Coeficients for class 2: {pd.DataFrame(LR.coef_[2], columns_names)}\n")

#print(f"Number of iterations generating model: {LR.n_iter_}")
import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import neighbors
from sklearn import metrics


wine = load_wine()
x = wine.data
y = wine.target
x_train, x_test, y_train,y_test = train_test_split(x,y, test_size=0.35)
knn = neighbors.KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train, y_train)

pred = knn.predict(x_test)

#print(metrics.classification_report(y_test, pred))
print(pred)
from sklearn.datasets import load_wine
from sklearn import svm
from sklearn.model_selection import train_test_split

wine = load_wine()
x = wine.data
y = wine.target

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.35)

knc = neighbors.KNeighborsClassifier(n_neighbors=1)
knc.fit(x_train, y_train)
print(wine.target_names[knc.predict([[14, 23, 13, 2]])])

import pandas as pd

iris = pd.read_csv('iris.csv')
setosa = iris[iris['species']=='setosa']
versicolor = iris[iris['species']=='versicolor']
virginica = iris[iris['species']=='virginica']

iris.hist(column='sepal_length', by='species', bins=20)
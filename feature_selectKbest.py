import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# SelectKBest code snippet borrowed from the scikit-learn doc:
### Author: Andreas Mueller <amueller@ais.uni-bonn.de>
### License: BSD 3 clause
### [] http://scikit-learn.org/stable/auto_examples/feature_stacker.html#sphx-glr-auto-examples-feature-stacker-py


from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest

#iris = load_iris()

#X, y = iris.data, iris.target
csv_in = r"C:\...\Improving Foster Care Placements\outGB.csv"
df_in = pd.read_csv(csv_in)

X = df_in.ix[:, 2:-1]
#X.drop('Age.Range.Served', axis=1, inplace=True)
#X.drop('Gender.Served', axis=1, inplace=True) #Gender.Served

#need to convert string data to numerical values for use downstream in SelectKMeans
from sklearn.preprocessing import LabelEncoder
#y2 = ["A","1","4","F","A","1","4","F"]
lb = LabelEncoder()
#print lb.fit_transform(df_in['Age.Range.Served'].values)
df_in['Age.Range.Served'] = lb.fit_transform(df_in['Age.Range.Served'].values)
#X.drop('Age.Range.Served', axis=1, inplace=True)


y = df_in.ix[:, -1:]

# This dataset is way too high-dimensional. Better do PCA:
#pca = PCA(n_components=2)

# Maybe some original features where good, too?
#selection = SelectKBest(k=1)
selection = SelectKBest(k=10)

# Build estimator from PCA and Univariate selection:

#combined_features = FeatureUnion([("pca", pca), ("univ_select", selection)])

# Use combined features to transform dataset:
X_features = selection.fit(X, y).transform(X)

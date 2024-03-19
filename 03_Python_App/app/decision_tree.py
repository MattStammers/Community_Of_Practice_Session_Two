import numpy as np
import pandas as pd
from app.generic_model import Basic_model
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier


class Decision_tree(Basic_model):
    def __init__(self, df):
        super().__init__(df)

    def train_model(self):
        self.train_data()
        dt_clf = DecisionTreeClassifier(random_state=0)
        dt_clf.fit(self.X_train, self.y_train)
        return dt_clf

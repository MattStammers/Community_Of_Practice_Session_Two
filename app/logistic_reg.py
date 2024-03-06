from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
from app.generic_model import Basic_model

class Logictic_model(Basic_model):
    def __init__(self, df):
        super().__init__(df)
    
    def log_reg(self):
        X_train, X_test, y_train, y_test = train_test_split(self.rescaledX2, self.y, test_size=0.25)
        logreg = LogisticRegression()
        logreg.fit(X_train, y_train)
        y_pred = logreg.predict(X_test)
        return y_test,y_pred
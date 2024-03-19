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
    
    def train_model(self):
        self.train_data()
        lr_model = LogisticRegression(max_iter=1000)
        lr_model.fit(self.X_train, self.y_train)
        return lr_model
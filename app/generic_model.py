from abc import ABC
import pandas as pd
from sklearn.preprocessing import StandardScaler

class Basic_model(ABC):
    def __init__(self, df):
        self.df = df
        self.X = self.df[['Gender', 'Diabetes','Hipertension', 'Scholarship', 'SMS_received',
        'Handicap_0','Handicap_1','Handicap_2','Handicap_3','Handicap_4', 'Num_App_Missed', 'Age', 'AwaitingTime']]
        self.y = df["No-show"]
        self.X_train = pd.get_dummies(self.X)
        scaler = StandardScaler().fit(self.X_train)
        self.rescaledX2 = scaler.transform(self.X_train)
    
    def get_inital_input(self):
        return self.X_train
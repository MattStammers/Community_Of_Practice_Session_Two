from sklearn.ensemble import RandomForestClassifier


from app.generic_model import Basic_model

class Random_forest(Basic_model):
    def __init__(self, df):
        super().__init__(df)
    
    def train_model(self):
        self.train_data()
        rf_clf = RandomForestClassifier(random_state=0)
        rf_clf.fit(self.X_train, self.y_train)
        return rf_clf
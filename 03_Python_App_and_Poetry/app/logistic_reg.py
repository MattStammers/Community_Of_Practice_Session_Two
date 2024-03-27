from sklearn.linear_model import LogisticRegression
from app.generic_model import Basic_model

class Logictic_model(Basic_model):
    def __init__(self, df):
        super().__init__(df)
    
    def train_model(self):
        self.train_data()
        lr_model = LogisticRegression(max_iter=1000)
        lr_model.fit(self.X_train, self.y_train)
        return lr_model
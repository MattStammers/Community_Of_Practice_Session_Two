from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

from .generic_model import Basic_model


class Logistic_model(Basic_model):
    def __init__(self, df):
        super().__init__(df)
        self.auc = None  # Initialize the AUC score attribute

    def train_model(self):
        self.train_data()
        lr_model = LogisticRegression(max_iter=1000)
        lr_model.fit(self.X_train, self.y_train)

        # Predict probabilities for the test set
        y_probs = lr_model.predict_proba(self.X_test)[:, 1]

        # Calculate the AUC score and store it
        self.auc = roc_auc_score(self.y_test, y_probs)

        return lr_model

    def get_auc(self):
        # Ensure AUC has been calculated
        if self.auc is None:
            raise ValueError("AUC not calculated. Please train the model first.")
        return self.auc

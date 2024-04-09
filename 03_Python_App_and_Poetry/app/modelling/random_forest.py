from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

from .generic_model import Basic_model


class Random_forest(Basic_model):
    def __init__(self, df):
        super().__init__(df)
        self.auc = None  # Initialize the AUC score attribute

    def train_model(self):
        self.train_data()
        rf_clf = RandomForestClassifier(random_state=42)
        rf_clf.fit(self.X_train, self.y_train)

        # Predict probabilities for the test set
        y_probs = rf_clf.predict_proba(self.X_test)[:, 1]

        # Calculate the AUC score and store it
        self.auc = roc_auc_score(self.y_test, y_probs)

        return rf_clf

    def get_auc(self):
        # Ensure AUC has been calculated
        if self.auc is None:
            raise ValueError("AUC not calculated. Please train the model first.")
        return self.auc

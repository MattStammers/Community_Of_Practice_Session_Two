from sklearn.metrics import roc_auc_score
from sklearn.tree import DecisionTreeClassifier

from .generic_model import Basic_model


class Decision_tree(Basic_model):
    def __init__(self, df):
        super().__init__(df)
        self.auc = None  # Initialize the AUC score attribute

    def train_model(self):
        self.train_data()
        dt_clf = DecisionTreeClassifier(random_state=42)
        dt_clf.fit(self.X_train, self.y_train)

        # Predict probabilities for the test set
        y_probs = dt_clf.predict_proba(self.X_test)[:, 1]

        # Calculate the AUC score and store it
        self.auc = roc_auc_score(self.y_test, y_probs)

        return dt_clf

    def get_auc(self):
        # Ensure AUC has been calculated
        if self.auc is None:
            raise ValueError("AUC not calculated. Please train the model first.")
        return self.auc

from abc import ABC, abstractmethod

import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class Basic_model(ABC):
    def __init__(self, df):
        """Initialize the model with a DataFrame. Preprocess and split the data."""
        self.df = df
        self.X = df.drop(["No-show"], axis=1)
        self.y = df["No-show"]

        # Scale features
        scaler = StandardScaler()
        self.X = pd.DataFrame(scaler.fit_transform(self.X), columns=self.X.columns)

    def train_data(self):
        """Split the data into training and testing sets."""
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=0
        )

    @abstractmethod
    def train_model(self):
        """Abstract method to train the model. Should be implemented by subclasses."""
        pass

    def prob_status(self, group_by):
        """Calculate the probability of no-show grouped by a specific column."""
        df = self.df.groupby(group_by)["No-show"].mean().reset_index()
        df.columns = [group_by, "probNoShow"]
        return df

    def feature_importance(self, feature_importance):
        """Generate a chart for feature importance."""
        feature_df = pd.DataFrame(
            {"features": self.X.columns, "features_importance": feature_importance}
        )
        chart = (
            alt.Chart(feature_df, width=500, height=400)
            .mark_bar()
            .encode(x="features_importance", y=alt.Y("features", sort="-x"))
        )
        return chart

    def calc_roc(self, model):
        """Calculate ROC curve and AUC score."""
        y_pred_proba = model.predict_proba(self.X_test)[:, 1]
        self.fpr, self.tpr, _ = roc_curve(self.y_test, y_pred_proba)
        self.auc = roc_auc_score(self.y_test, y_pred_proba)

    def plot_roc(self, m_label, filename):
        """Plot ROC curve and save as PNG."""
        plt.figure()
        plt.plot(self.fpr, self.tpr, label=f"{m_label} AUC = {self.auc:.2f}")
        plt.plot([0, 1], [0, 1], "r--", label="Chance (AUC = 0.5)")
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title(f"ROC Curve for {m_label} Classifier")
        plt.legend(loc="lower right")
        plt.savefig(f"app/static/{filename}.png", format="png")

    def get_auc(self):
        """Return the AUC score."""
        return self.auc

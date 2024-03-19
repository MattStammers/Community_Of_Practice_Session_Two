from abc import ABC

import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.model_selection import train_test_split


class Basic_model(ABC):
    def __init__(self, df):
        self.df = df
        self.X = self.df.drop(["No-show"], axis=1)
        self.y = self.df["No-show"]

    def train_data(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=0
        )

    def get_inital_input(self):
        return self.X

    def get_x_train(self):
        return self.X_train

    def get_y_test_train(self):
        return self.y_train, self.y_test

    def prob_status(self, dataset, group_by):
        df = dataset.groupby(group_by)["No-show"].mean().reset_index()
        df.columns = [group_by, "probNoShow"]
        return df

    def feature_importance(self, feature_importance):
        features = self.X.columns
        features_l = features.to_list()
        feature_df = pd.DataFrame(
            np.column_stack([features_l, feature_importance]),
            columns=["features", "features_importance"],
        )
        feature_df["features_importance"] = feature_df["features_importance"].astype(
            float
        )
        chart = (
            alt.Chart(feature_df, width=500, height=400)
            .mark_bar()
            .encode(x="features_importance", y=alt.Y("features", sort="-x"))
        )
        return chart

    def calc_roc(self, model):
        # Predict probabilities for the positive class (1)
        y_pred_proba = model.predict_proba(self.X_test)[:, 1]

        # Compute ROC curve and AUC
        self.fpr, self.tpr, _ = roc_curve(self.y_test, y_pred_proba)
        self.auc = roc_auc_score(self.y_test, y_pred_proba)

    def plot_roc(self, m_label, filename):
        # Plot the ROC curve
        plt.figure()
        plt.plot(self.fpr, self.tpr, label=f"{m_label} AUC = {self.auc:.2f}")
        plt.plot([0, 1], [0, 1], "r--", label="Chance (AUC = 0.5)")
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title(f"ROC Curve for {m_label} Classifier")
        plt.legend(loc="lower right")
        plt.savefig(f"app/static/{filename}.png", format="png")

    def get_auc(self):
        return self.auc

        # # Plot the ROC curve
        # plt.figure()#figsize=(8, 6))
        # plt.plot(fpr_rf, tpr_rf, label=f'{m_label} AUC = {auc_rf:.2f}')
        # plt.plot([0, 1], [0, 1], 'r--', label='Chance (AUC = 0.5)')
        # plt.xlabel('False Positive Rate')
        # plt.ylabel('True Positive Rate')
        # plt.title(f'ROC Curve for {m_label} Classifier')
        # plt.legend(loc='lower right')
        # plt.savefig(f'app/static/{filename}.png', format='png', dpi=600)

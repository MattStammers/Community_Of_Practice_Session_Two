# Import pypi imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Import local imports
from app.decision_tree import Decision_tree
from app.logistic_reg import Logictic_model
from app.pre_process import Pre_process
from app.random_forest import Random_forest
from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve
from sklearn.preprocessing import StandardScaler

# Load data
df = pd.read_csv("app/data/KaggleV2-May-2016.csv")
df.head()

# Preprocess data
pre_processer = Pre_process(df)
df_proc = pre_processer.format_and_get_df()

# Scale the processed data
scaler = StandardScaler()
df_proc_scaled = scaler.fit_transform(df_proc)

print(df_proc_scaled)
df_proc_scaled_df = pd.DataFrame(df_proc_scaled, columns=df_proc.columns)

# Logistic Regression Model
# Assuming Logictic_model can accept a max_iter parameter
log = Logictic_model(df_proc_scaled)  # Adjusted with scaled data
log_reg = log.train_model()

feature_importance = abs(log_reg.coef_[0])
log.feature_importance(
    feature_importance,
    "logistic_regression",
    "feature_importance_logistic_regression_classifier",
)
log.calc_roc(
    log_reg, "logistic_regression", "ROC_curve_for_logistic_regression_classifier"
)

# Decision Tree Model
dt = Decision_tree(df_proc_scaled)  # Adjusted with scaled data
dt_model = dt.train_model()

feature_importances = dt_model.feature_importances_
dt.feature_importance(
    feature_importances, "decision_tree", "feature_importance_decision_tree_classifier"
)
dt.calc_roc(dt_model, "decision_tree", "ROC_curve_for_decision_tree_classifier")

# Random Forest Model
rf = Random_forest(df_proc_scaled)  # Adjusted with scaled data
rf_model = rf.train_model()

feature_importances = rf_model.feature_importances_
rf.feature_importance(
    feature_importances, "random_forest", "feature_importance_random_forest_classifier"
)
rf.calc_roc(rf_model, "random_forest", "ROC_curve_for_random_forest_classifier")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from app.decision_tree import Decision_tree
from app.logistic_reg import Logictic_model
from app.pre_process import Pre_process
from app.random_forest import Random_forest
from sklearn import metrics
from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve

df = pd.read_csv("KaggleV2-May-2016.csv")

pre_processer = Pre_process(df)
df_proc = pre_processer.format_and_get_df()
print(df_proc)

log = Logictic_model(df_proc)
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

dt = Decision_tree(df_proc)
dt_model = dt.train_model()
feature_importances = dt_model.feature_importances_
dt.feature_importance(
    feature_importances, "decision_tree", "feature_importance_decision_tree_classifier"
)
dt.calc_roc(dt_model, "decision_tree", "ROC_curve_for_decision_tree_classifier")

rf = Random_forest(df_proc)
rf_model = rf.train_model()
feature_importances = rf_model.feature_importances_
rf.feature_importance(
    feature_importances, "random_forest", "feature_importance_random_forest_classifier"
)
rf.calc_roc(rf_model, "random_forest", "ROC_curve_for_random_forest_classifier")

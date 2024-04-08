import pandas as pd
from app.data_processing.pre_process import Pre_process
from app.modelling.decision_tree import Decision_tree
from app.modelling.logistic_reg import Logistic_model
from app.modelling.random_forest import Random_forest

df = pd.read_csv("app/static/data/KaggleV2-May-2016.csv")

pre_processer = Pre_process(df)
df_proc = pre_processer.format_and_get_df()
print(df_proc)

log = Logistic_model(df_proc)
log_reg = log.train_model()
feature_importance = abs(log_reg.coef_[0])
chart = log.feature_importance(feature_importance)
chart.save("app/static/logistic_regression_features.html")
log.calc_roc(log_reg)
log.plot_roc("logistic_regression", "ROC_curve_for_logistic_regression_classifier")

dt = Decision_tree(df_proc)
dt_model = dt.train_model()
feature_importances = dt_model.feature_importances_
chart = dt.feature_importance(feature_importances)
chart.save("app/static/decision_tree_features.html")
dt.calc_roc(dt_model)
dt.plot_roc("decision_tree", "ROC_curve_for_decision_tree_classifier")

rf = Random_forest(df_proc)
rf_model = rf.train_model()
feature_importances = rf_model.feature_importances_
chart = rf.feature_importance(feature_importances)
chart.save("app/static/random_forest_features.html")
rf.calc_roc(rf_model)
rf.plot_roc("random_forest", "ROC_curve_for_random_forest_classifier")

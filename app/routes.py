from flask import render_template, flash, redirect, url_for
from app.pre_process import Pre_process
from app.logistic_reg import Logictic_model
from app.decision_tree import Decision_tree
from app.random_forest import Random_forest
from app import app
import pandas as pd
import matplotlib
matplotlib.use('Agg')

df = pd.read_csv("app/static/data/KaggleV2-May-2016.csv")
pre_processer = Pre_process(df)
df_proc = pre_processer.format_and_get_df()

log = Logictic_model(df_proc)
log_reg = log.train_model()
feature_importance = abs(log_reg.coef_[0])
log.feature_importance(feature_importance, "logistic_regression","feature_importance_logistic_regression_classifier")
log.calc_roc(log_reg, "logistic_regression", "ROC_curve_for_logistic_regression_classifier")

dt = Decision_tree(df_proc)
dt_model = dt.train_model()
feature_importances = dt_model.feature_importances_
dt.feature_importance(feature_importances, "decision_tree","feature_importance_decision_tree_classifier")
dt.calc_roc(dt_model, "decision_tree", "ROC_curve_for_decision_tree_classifier")

rf = Random_forest(df_proc)
rf_model = rf.train_model()
feature_importances = rf_model.feature_importances_
rf.feature_importance(feature_importances, "random_forest","feature_importance_random_forest_classifier")
rf.calc_roc(rf_model, "random_forest", "ROC_curve_for_random_forest_classifier")


@app.route('/')
@app.route('/index')
def index():
    plt_1 = "feature_importance_logistic_regression_classifier.png"
    plt_2 = 'ROC_curve_for_logistic_regression_classifier.png'
    info = plt_1
    print(info)
    return render_template('index.html', links=info)
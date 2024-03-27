from flask import render_template, flash, redirect, url_for
from app.pre_process import Pre_process
from app.logistic_reg import Logictic_model
from app.decision_tree import Decision_tree
from app.random_forest import Random_forest
from app import app
import altair as alt
import pandas as pd
import matplotlib
from matplotlib.figure import Figure
matplotlib.use('Agg')

df = pd.read_csv("app/static/data/KaggleV2-May-2016.csv")
pre_processer = Pre_process(df)
df_proc = pre_processer.format_and_get_df()

log = Logictic_model(df_proc)
log_reg = log.train_model()
log.calc_roc(log_reg)
log.plot_roc("logistic_regression", "ROC_curve_for_logistic_regression_classifier")

dt = Decision_tree(df_proc)
dt_model = dt.train_model()

# dt.feature_importance(feature_importances, "decision_tree","feature_importance_decision_tree_classifier")
dt.calc_roc(dt_model)
dt.plot_roc("decision_tree", "ROC_curve_for_decision_tree_classifier")

rf = Random_forest(df_proc)
rf_model = rf.train_model()

# rf.feature_importance(feature_importances, "random_forest","feature_importance_random_forest_classifier")
rf.calc_roc(rf_model)
rf.plot_roc("random_forest", "ROC_curve_for_random_forest_classifier")


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/log_page')
def log_page():
    auc = log.get_auc()
    return render_template('log_page.html', auc=auc)

@app.route('/log_reg_features')
def log_reg_features():
    feature_importance = abs(log_reg.coef_[0])
    chart = log.feature_importance(feature_importance)
    return chart.to_json()

@app.route('/dt_page')
def dt_page():
    auc = dt.get_auc()
    return render_template('dt_page.html',auc=auc)

@app.route('/dt_features')
def dt_features():
    feature_importances = dt_model.feature_importances_
    chart = dt.feature_importance(feature_importances)
    return chart.to_json()

@app.route('/rf_page')
def rf_page():
    auc = rf.get_auc()
    return render_template('rf_page.html',auc=auc)

@app.route('/rf_features')
def rf_features():
    feature_importances = rf_model.feature_importances_
    chart = rf.feature_importance(feature_importances)
    return chart.to_json()
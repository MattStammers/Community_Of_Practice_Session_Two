# routes.py
from app import app
from flask import render_template

from .model_setup import models


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/log_page")
def log_page():
    auc = models["log_model"].get_auc()
    return render_template("log_page.html", auc=auc)


@app.route("/log_reg_features")
def log_reg_features():
    feature_importance = abs(models["logistic_regression"].coef_[0])
    chart = models["log_model"].feature_importance(feature_importance)
    return chart.to_json()


@app.route("/dt_page")
def dt_page():
    auc = models["dt_model"].get_auc()
    return render_template("dt_page.html", auc=auc)


@app.route("/dt_features")
def dt_features():
    feature_importances = models["decision_tree"].feature_importances_
    chart = models["dt_model"].feature_importance(feature_importances)
    return chart.to_json()


@app.route("/rf_page")
def rf_page():
    auc = models["rf_model"].get_auc()
    return render_template("rf_page.html", auc=auc)


@app.route("/rf_features")
def rf_features():
    feature_importances = models["random_forest"].feature_importances_
    chart = models["rf_model"].feature_importance(feature_importances)
    return chart.to_json()

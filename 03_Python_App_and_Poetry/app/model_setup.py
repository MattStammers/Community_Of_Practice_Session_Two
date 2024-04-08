# model_setup.py
import pandas as pd
from app.data_processing.pre_process import Pre_process
from app.modelling.decision_tree import Decision_tree
from app.modelling.logistic_reg import Logistic_model
from app.modelling.random_forest import Random_forest


def setup_models():
    # Load and preprocess the dataset
    df = pd.read_csv("app/static/data/KaggleV2-May-2016.csv")
    pre_processer = Pre_process(df)
    df_proc = pre_processer.format_and_get_df()

    # Initialize and train models
    log_model = Logistic_model(df_proc)
    log_reg = log_model.train_model()

    dt_model = Decision_tree(df_proc)
    dt = dt_model.train_model()

    rf_model = Random_forest(df_proc)
    rf = rf_model.train_model()

    # Store models and other necessary data in a dictionary for easy access
    models = {
        "logistic_regression": log_reg,
        "decision_tree": dt,
        "random_forest": rf,
        "log_model": log_model,
        "dt_model": dt_model,
        "rf_model": rf_model,
    }

    return models


# This ensures models are set up once when the application starts.
models = setup_models()

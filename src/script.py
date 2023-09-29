import os

import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso, LinearRegression, LogisticRegression, Ridge
import joblib
history_file = "history.csv"
result_dir = "results"
model_file_path = "model/regression_lineaire.joblib"

def process_files(history_file="history.csv", result_dir="results"):
    if not os.path.exists(history_file):
        result_df = pd.DataFrame(columns=["file", "evaluated"])
    else:
        result_df = pd.read_csv(history_file)

    for file in os.listdir("data"):
        if file.endswith(".csv") and file not in result_df["file"].values:
            print("Evaluating {}".format(file))
            df = pd.read_csv("data/{}".format(file))
            X = df.drop("y", axis=1)
            y = df["y"]
            model = joblib.load(model_file_path)
            score = model.score(X, y)
            result_df = result_df.append(
                {"file": file, "evaluated": score}, ignore_index=True
            )

    result_df.to_csv(os.path.join(result_dir, history_file), index=False)

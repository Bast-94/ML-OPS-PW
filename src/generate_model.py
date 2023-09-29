import os

import joblib
import numpy as np
from sklearn.linear_model import Lasso

model_file_path = "model/regression_lineaire.joblib"


def generate_model():
    if os.path.exists(model_file_path):
        return 0

    X = np.random.randn(10, 2)
    y = 0.1 + 0.1 * X[:, 0] - 0.2 * X[:, 1]
    model = Lasso()
    model.fit(X, y)
    joblib.dump(model, model_file_path)


if __name__ == "__main__":
    generate_model()

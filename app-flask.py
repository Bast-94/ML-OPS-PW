from flask import Flask
from flask import request
import json
import joblib

def load_model(model_file_path:str):
    return joblib.load(model_file_path)

model = load_model('model/regression_lineaire.joblib')
app = Flask(__name__)

@app.route("/fake-predict")
def prediction():
    y_pred = [50000]
    return json.dumps({"prediction": y_pred})


@app.route("/predict", methods=['POST'])#permet de spécifier quand la fonction juste en dessous doit être appelée
def predict():
    #suppose que le client envoie une requête avec dedans X
    print(request.get_json())
    X = request.get_json()['X']
    return X
  

if __name__ == "__main__":
    app.run("0.0.0.0")
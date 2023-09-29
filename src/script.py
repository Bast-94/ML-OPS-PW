import os 
from sklearn.linear_model import LogisticRegression, LinearRegression, Ridge, Lasso
import pandas as pd
import numpy as np
history_file = 'history.csv'
result_dir = 'results'
if not os.path.exists(history_file):
    result_df = pd.DataFrame(columns=['file', 'evaluated'])
else:
    result_df = pd.read_csv(history_file)

for file in os.listdir('data'):
    if file.endswith('.csv') and file not in result_df['file'].values:
        print('Evaluating {}'.format(file))
        df = pd.read_csv('data/{}'.format(file))
        X = df.drop('y', axis=1)
        y = df['y']
        model = LogisticRegression()
        model.fit(X, y)
        score = model.score(X, y)
        result_df = result_df.append({'file': file, 'evaluated': score}, ignore_index=True)
    
result_df.to_csv(os.path.join(result_dir,history_file), index=False)



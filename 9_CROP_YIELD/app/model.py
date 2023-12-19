import pickle
import numpy as np
import pandas as pd
import xgboost as xgb
import tensorflow as tf
from keras.models import load_model


model=load_model("crop_recommendation.h5")
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')

features_1 = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
features_2 = ['Item', 'Year', 'average_rain_fall_mm_per_year', 'pesticides_tonnes','avg_temp']

ln1 = pickle.load(open('crop.pkl', 'rb'))

with open('yield.pkl', 'rb') as file:
    xgb_r = pickle.load(file)
def pred_pipe_1(X):
    X = np.array(X).reshape(1,-1)
    pred = model.predict(X)
    return ln1.inverse_transform(np.argmax(pred, axis=1).reshape(1, -1))[0]


def pred_pipe_2(l):
    l = np.array(l).reshape(1, -1)
    df = pd.DataFrame(l, columns=features_2)

    ln2 = pickle.load(open('yield_item.pkl', 'rb'))

    try:
        df['Item'] = ln2.transform(df['Item'])
    except ValueError as e:
        print(f"Warning: {e}")
        # Handle the error, e.g., by setting unseen labels to a default value
        df['Item'] = -1  # Set unseen labels to -1 (adjust as needed)

    X = df.values.reshape(1, -1)
    pred = xgb_r.predict(X)

    return pred[0]

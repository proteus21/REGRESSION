import matplotlib.pyplot as plt
import pandas as pd
import pickle

base = 'Epileptic Seizure Recognition.csv'
with open("svc_eeg.pkl", "rb") as file:
    model = pickle.load(file)
df = pd.read_csv('Epileptic Seizure Recognition.csv')
df = df.drop(columns = df.columns[0])

def predict(data):
    new_input1 = [df.iloc[data, :177]]

    new_output = model.predict(new_input1)
    if new_output == [1]:
        s = 'Yes, you might get seizure. It is dangeres for you'
    else:
        s = 'You are safe no worries :)'
    return s

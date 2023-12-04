from flask import Flask, render_template, request
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
from model import predict


app = Flask(__name__)

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = set(['png','jpg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
df = pd.read_csv('Epileptic Seizure Recognition.csv')
df = df.drop(columns = df.columns[0])


@app.route('/')
def home():  # put application's code here
    return  render_template('index.html')

@app.route('/', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        plt.switch_backend('Agg')

        # Use get method with a default value to handle missing or empty form field
        file_value = request.form.get('file1', '')

        # Check if the value is non-empty
        if file_value:
                file1 = int(file_value)
                # Continue processing with the integer value 'file1'
                plt.plot(df.iloc[file1, :177].values)
                plt.savefig(f'{UPLOAD_FOLDER}/signal.png')
                s = predict(file1)
                print(s)
                return render_template('index.html', result=s)


if __name__ == '__main__':
    app.run(debug=True)

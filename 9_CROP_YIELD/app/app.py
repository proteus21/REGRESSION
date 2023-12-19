from flask import Flask, request, render_template
#from model import *
from model  import  features_1, features_2, pred_pipe_1, pred_pipe_2

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def start():
    return render_template('index.html')

@app.route('/recommend', methods=['GET', 'POST'])
def recommend_1():
    l = []
    if request.method == 'POST':
        for i in features_1:
            print(i)
            try:
                l.append(float(request.form[i]))
            except ValueError:
                l.append(request.form[i])
        recommendation = pred_pipe_1(l)
    else:
        recommendation = ''
    return render_template('index.html', rec=recommendation)

@app.route('/yield', methods=['GET', 'POST'])
def yield_():
    l1 = []
    if request.method == 'POST':
        for i in features_2:
            try:
                l1.append(float(request.form[i]))
            except ValueError:
                l1.append(request.form[i])
        y = pred_pipe_2(l1)
    else:
        y = 0
    return render_template('index.html', yi=y)

if __name__ == '__main__':
    app.run(DEBUG=True)
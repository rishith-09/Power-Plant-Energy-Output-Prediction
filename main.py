import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    at = request.form.get('at')
    v = request.form.get('v')
    ap = request.form.get('ap')
    rh = request.form.get('rh')
    predict = model.predict([[at,v,ap,rh]])[0]
    return render_template('index.html',prediction_text = f'Total Energy Output is {np.round(predict,2)}')


if __name__ == '__main__':
    app.run(debug=True)
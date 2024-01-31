from sklearn import datasets
from joblib import load
import numpy as np
import json


#from flask import jsonify, render_template, request, redirect, url_for
#from flask import send_file
from flask import request, jsonify
import pandas as pd
UPLOAD_FOLDER='.'

def upload(filename):
    f = request.files['file']
    f.save(filename)
    return filename

def file_prediction(filename):
    my_model = load('bean_mdl.pkl')
    name = upload(filename)
    test_data = pd.read_csv(name)
    test_np = test_data.to_numpy()
    pred = my_model.predict(test_np)
    pred_list = pred.tolist()
    json_str = json.dumps(pred_list)
    return json_str

    

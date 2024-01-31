from sklearn import datasets
from joblib import load
import numpy as np
import json


def bean_prediction(id):
    my_model = load('bean_mdl.pkl')
    if type(id) is np.ndarray:
      print("I am a numpy array")
      prediction = my_model.predict(id)
    else:
      dummy = np.array(id)
      dummyT = dummy.reshape(1,-1)
      dummy_str = dummy.tolist()
      prediction = my_model.predict(dummyT)
      pred_list = prediction.tolist()
      json_str = json.dumps(pred_list)
    return json_str

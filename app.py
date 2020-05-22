from flask import Flask,request,redirect,url_for,render_template
import camera
import sys,os,glob,re
import numpy as np
import requests
import json
import feat
from keras.preprocessing import image
import cv2
from keras.models import load_model
from keras.applications.imagenet_utils import preprocess_input,decode_predictions
from werkzeug.utils import secure_filename
from keras.models import model_from_json
import keras
from keras.layers import *
from keras.models import Model , load_model
from keras.preprocessing import image
from keras.utils import np_utils
from keras.models import model_from_json
from keras.applications.resnet50 import ResNet50
from keras.optimizers import Adam
import matplotlib.pyplot as plt
app = Flask(__name__,static_url_path="",static_folder="templates")

app = Flask(__name__)


@app.route('/')
def hello_world():
    data = requests.get("https://disease.sh/v2/countries/India?yesterday=true&strict=true")
    data_dict = data.json()
    var = "hello"
    return render_template('index.html',data = data_dict)

@app.route('/detect')
def detect():
    os.system('python get_pulse.py')
    return render_template('index.html')

@app.route('/xray')
def xray():
    os.system('python X_Ray_Detection.py')
    return render_template('index.html')



@app.route('/analyze', methods=["POST"])
def analyze():

    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname('uploads')
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        print("In the analyze funciton")
        f.save(file_path)

        # pred_class = decode_predictions(preds, top=1)
        # result = str(pred_class[0][0][1])
        # # return result
        #
        # return json.dumps({"image": result})
    return None


if __name__ == '__main__':
    app.run()

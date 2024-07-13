from flask import Flask, render_template, request
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/classify')
def classify():
    return render_template("index.html", prediction="No file part")

if __name__ == '__main__':
    app.run(debug=False)

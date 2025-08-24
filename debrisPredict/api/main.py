from flask import Flask, request, jsonify
import os
import io
import base64
from PIL import Image
import numpy as np

app = Flask(__name__)

# Your existing app code here
@app.route('/')
def home():
    return "Debris Detection API is running!"

# Add your existing routes here
# @app.route('/predict', methods=['POST'])
# def predict():
#     # Your prediction logic here
#     pass

# This is needed for Vercel
if __name__ == '__main__':
    app.run(debug=True)

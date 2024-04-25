
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd  # Ensure pandas is imported
from joblib import load
import os

# Define the root directory path
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Initialize the Flask application
app = Flask(__name__, root_path=ROOT_PATH)
model = load(os.path.join(ROOT_PATH, 'app', 'california_housing_model.joblib'))

@app.route('/')
def index():
    # Print the path to the templates directory for debugging
    print(f"Templates directory: {app.template_folder}")
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()  # Get data as JSON
        features = [float(data[key]) for key in sorted(data)]  # Convert and sort the data
        feature_names = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']  # Ensure these match your training data
        df = pd.DataFrame([features], columns=feature_names)
        prediction = model.predict(df)
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        print("Error:", str(e))  # Printing the error might give more insights in debugging
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

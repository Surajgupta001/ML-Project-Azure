from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

from src.logger import logging

application = Flask(__name__)
app = application

logging.info("Flask application started")

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html') 

# Route for prediction
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        # Render the input form
        return render_template('home.html')
    else:
        # Collect data from the form and create a CustomData object
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            # Fixed the swap here
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )
        
        # Convert input to DataFrame
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        
        # Initialize and run the prediction pipeline
        predict_pipeline = PredictPipeline()
        logging.info("Before Prediction")
        results = predict_pipeline.predict(pred_df)
        logging.info("After Prediction")
        
        # Render the result on the home page
        return render_template('home.html', results=results[0])
    

if __name__ == "__main__":
    # Run the Flask application
    app.run(host='0.0.0.0', port=8080)
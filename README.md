# Diabetes Prediction Web Application

This project is a web application that predicts the likelihood of diabetes based on user-input health data. It uses a machine learning model trained on a diabetes prediction dataset.

## Features

- User-friendly web interface for input of health data
- Predicts diabetes likelihood based on various health factors
- Uses a logistic regression model for prediction

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/diabetes-prediction-app.git
   cd diabetes-prediction-app
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open a web browser and navigate to `http://localhost:5000`

## Usage

1. Fill in the health data form on the web page.
2. Click the "Predict" button.
3. The application will display whether you are likely to have diabetes based on the input data.

## Files

- `app.py`: Contains the Flask application and routing logic
- `diabetes.py`: Contains the machine learning model and prediction logic
- `templates/index.html`: HTML template for the web interface (not provided in the given code)
- `model.joblib`: Saved machine learning model (generated when running `diabetes.py`)

## Data

The model is trained on a diabetes prediction dataset. Make sure to place the dataset file `diabetes_prediction_dataset.csv` in the correct path as specified in `diabetes.py`.

## Note

This application is for educational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment.

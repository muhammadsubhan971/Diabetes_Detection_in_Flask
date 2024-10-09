from flask import Flask, render_template, request
from diabetes import predication

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        try:
            gender = int(request.form['gender'])
            smoking_history = int(request.form['smoking_history'])
            age = int(request.form['age'])
            bmi = float(request.form['bmi'])
            glucose = int(request.form['blood_glucose_level'])
            hba1c = float(request.form['HbA1c_level'])
            hypertension = 1 if request.form['hypertension'] == 'yes' else 0
            heart_disease = 1 if request.form['heart_disease'] == 'yes' else 0

            input_features = [[gender, age, hypertension, heart_disease, smoking_history, bmi, hba1c, glucose]]


            prediction = predication(input_features)
            print(type(prediction))
            print(prediction)

            result = 'Yes' if prediction == 1 else 'No'
            return render_template('index.html', prediction_text=f'Prediction: Diabetes: {result}')

        except KeyError as e:
            return f"Missing form field: {e}", 400
        except ValueError as e:
            return f"Invalid input: {e}", 400

    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

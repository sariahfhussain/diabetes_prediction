from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('diabetes_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve input values from the form
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    
    # Make prediction
    prediction = model.predict(final_features)
    output = 'Diabetic' if prediction[0] == 1 else 'Not Diabetic'
    
    return render_template('index.html', prediction_text=f'Result: {output}')

if __name__ == "__main__":
    app.run(debug=True)



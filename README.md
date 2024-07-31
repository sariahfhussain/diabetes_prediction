<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>
    <h1>Diabetes Prediction Project</h1>
    <p>This project demonstrates a machine learning model for predicting diabetes. It includes a Jupyter notebook for training the model and a Flask web application for making predictions using the trained model.</p>
    
 <h2>Files in the Repository</h2>
    <ul>
        <li><code>diabetes_prediction.ipynb</code>: Jupyter notebook containing the code for training the Random Forest model on the diabetes dataset and saving the trained model.</li>
        <li><code>diabetes.csv</code>: Dataset used for training the model (assumed to be present in the same directory).</li>
        <li><code>diabetes_model.joblib</code>: The trained Random Forest model saved as a joblib file.</li>
        <li><code>app.py</code>: Flask web application for making predictions using the trained model.</li>
        <li><code>templates/index.html</code>: HTML template for the web application's home page (assumed to be present in the <code>templates</code> directory).</li>
    </ul>
    
 <h2>Jupyter Notebook</h2>
    <h3>Training the Model</h3>
    <ol>
        <li><strong>Load the Dataset</strong>: The dataset <code>diabetes.csv</code> is loaded using pandas.</li>
        <li><strong>Define Features and Target Variable</strong>: Features (X) and target variable (y) are defined.</li>
        <li><strong>Split the Data</strong>: The data is split into training and testing sets using <code>train_test_split</code>.</li>
        <li><strong>Train the Model</strong>: A Random Forest classifier is initialized and trained on the training set.</li>
        <li><strong>Save the Model</strong>: The trained model is saved as <code>diabetes_model.joblib</code> using joblib.</li>
        <li><strong>Evaluate the Model</strong>: The model's accuracy is evaluated on the test set and printed.</li>
    </ol>
    
<h2>Flask Web Application</h2>
    <h3>app.py</h3>
    <ol>
        <li><strong>Load the Model</strong>: The trained model is loaded using joblib.</li>
        <li><strong>Define Routes</strong>:
            <ul>
                <li><code>/</code>: Renders the home page (<code>index.html</code>).</li>
                <li><code>/predict</code>: Handles form submissions, makes predictions using the loaded model, and displays the result on the home page.</li>
            </ul>
        </li>
        <li><strong>Run the Application</strong>: The Flask application is run in debug mode.</li>
    </ol>
    
<h2>Usage</h2>
    <h3>Prerequisites</h3>
    <ul>
        <li>Python 3.x</li>
        <li>Required Python packages: pandas, scikit-learn, joblib, Flask, numpy</li>
    </ul>
    
<h3>Installation</h3>
    <ol>
        <li>Clone the repository.</li>
        <li>Install the required packages:
            <pre><code>pip install pandas scikit-learn joblib Flask numpy</code></pre>
        </li>
        <li>Ensure <code>diabetes.csv</code> is present in the same directory as <code>diabetes_prediction.ipynb</code> and <code>app.py</code>.</li>
    </ol>
    
 <h3>Running the Notebook</h3>
    <ol>
        <li>Open <code>diabetes_prediction.ipynb</code> in Jupyter Notebook or JupyterLab.</li>
        <li>Execute the cells to train the model and save it as <code>diabetes_model.joblib</code>.</li>
    </ol>
    
 <h3>Running the Flask Application</h3>
    <ol>
        <li>Ensure the trained model (<code>diabetes_model.joblib</code>) is present in the same directory as <code>app.py</code>.</li>
        <li>Run the Flask application:
            <pre><code>python app.py</code></pre>
        </li>
        <li>Open a web browser and go to <code>http://127.0.0.1:5000</code> to access the application.</li>
    </ol>
    
</body>
</html>


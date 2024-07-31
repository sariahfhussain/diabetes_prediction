import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
file_path = r'C:\Users\saria\OneDrive\Desktop\diabetes prediction\diabetes.csv'
data = pd.read_csv(file_path)

# Define features and target variable
X = data.drop(columns='Outcome')
y = data['Outcome']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Save the trained model
model_path = r'C:\Users\saria\OneDrive\Desktop\diabetes prediction\diabetes_model.joblib'
joblib.dump(clf, model_path)

print(f"Model saved to {model_path}")


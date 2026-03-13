#implement multi linear regression for PIMA indian Diabetes dataset

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load dataset
df = pd.read_csv("pima-indians-diabetes.csv")

# Display first few rows
print(df.head())

# Independent variables (features)
X = df[['Pregnancies', 'Glucose', 'BloodPressure',
        'SkinThickness', 'Insulin', 'BMI',
        'DiabetesPedigreeFunction', 'Age']]

# Dependent variable
y = df['Outcome']

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict values
y_pred = model.predict(X_test)

# Model coefficients
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# Model error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Predict diabetes outcome for a new patient
new_patient = [[2, 120, 70, 20, 79, 25.3, 0.5, 33]]
prediction = model.predict(new_patient)

print("Predicted Diabetes Value:", prediction)

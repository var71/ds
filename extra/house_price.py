#Implement multi linear regression using python or r to predict the price of house 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Example dataset
data = {
    'Area': [1000, 1500, 2000, 2500, 3000],
    'Bedrooms': [2, 3, 3, 4, 4],
    'Age': [10, 5, 3, 2, 1],
    'Price': [200000, 300000, 400000, 500000, 600000]
}

df = pd.DataFrame(data)

# Features (independent variables)
X = df[['Area', 'Bedrooms', 'Age']]

# Target variable
y = df['Price']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict price
prediction = model.predict([[2200, 3, 5]])

print("Predicted House Price:", prediction[0])

# Model coefficients
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

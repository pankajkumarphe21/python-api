from sklearn.linear_model import LinearRegression
import numpy as np
import pickle

# Create and train the model
X = np.array([[1], [2], [3], [4], [5]])  # Example data
y = np.array([1.5, 3.0, 4.5, 6.0, 7.5])  # Example target
model = LinearRegression()
model.fit(X, y)

# Save the model to a file
with open("linear_model.pkl", "wb") as f:
    pickle.dump(model, f)

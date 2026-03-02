# import pandas as pd
# from sklearn.linear_model import LinearRegression
# import pickle

# data = pd.read_csv(r"C:\Users\HP\Documents\Projects\House-Price-Project\dataset\House Price Prediction Dataset.csv")

# X = data[['Area','Bathrooms','YearBuilt']]
# y = data['Price']

# model = LinearRegression()
# model.fit(X,y)

# pickle.dump(model,open("model.pkl","wb"))

# print("Model trained and saved!")


import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle

# Load dataset
data = pd.read_csv(r"C:\Users\HP\Documents\Projects\House-Price-Project\dataset\House Price Prediction Dataset.csv")

# Select important columns
# data = data[['GrLivArea','BedroomAbvGr','FullBath','SalePrice']]

X = data[['Area','Bathrooms','YearBuilt']]
y = data['Price']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train,y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate model
score = r2_score(y_test,y_pred)

print("Model R2 Score:",score)

# Save model
pickle.dump(model, open("model.pkl","wb"))

print("Model trained and saved successfully")
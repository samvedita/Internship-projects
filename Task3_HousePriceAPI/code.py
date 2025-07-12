# task3_house_price_api.py

# === Step 1: Create dataset ===
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from flask import Flask, request, jsonify

# Create sample data
data = {
    'area': [1000, 1500, 1200, 1800, 900, 1300],
    'bedrooms': [3, 4, 3, 4, 2, 3],
    'age': [10, 5, 12, 8, 15, 7],
    'price': [200000, 350000, 250000, 400000, 180000, 300000]
}
df = pd.DataFrame(data)
df.to_csv('house_data.csv', index=False)

# === Step 2: Train model ===
X = df[['area', 'bedrooms', 'age']]
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
joblib.dump(model, 'model.pkl')

# === Step 3: Flask API ===
app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return "Welcome to the House Price Predictor API!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    area = data.get('area')
    bedrooms = data.get('bedrooms')
    age = data.get('age')
    
    prediction = model.predict([[area, bedrooms, age]])
    return jsonify({'predicted_price': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)

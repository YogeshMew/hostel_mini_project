from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Example historical data (replace with your actual historical data)
# Example historical data (replace with your actual historical data)
historical_data = [
    {"previousBill": 2000, "currentMonthBill": 1800, "nextMonthBill": 2100},
    {"previousBill": 2200, "currentMonthBill": 1900, "nextMonthBill": 2300},
    {"previousBill": 2400, "currentMonthBill": 2000, "nextMonthBill": 2500},
    {"previousBill": 2100, "currentMonthBill": 2200, "nextMonthBill": 2600},
    {"previousBill": 2300, "currentMonthBill": 2100, "nextMonthBill": 2700},
    {"previousBill": 2500, "currentMonthBill": 2300, "nextMonthBill": 2800},
    {"previousBill": 2600, "currentMonthBill": 2400, "nextMonthBill": 2900},
    {"previousBill": 2700, "currentMonthBill": 2500, "nextMonthBill": 3000},
    {"previousBill": 2800, "currentMonthBill": 2600, "nextMonthBill": 3100},
    {"previousBill": 2900, "currentMonthBill": 2700, "nextMonthBill": 3200},
    {"previousBill": 9000, "currentMonthBill": 8000, "nextMonthBill": 7000},
    {"previousBill": 2000, "currentMonthBill": 1000, "nextMonthBill": 800},
    # Additional historical data with increasing order from 100 to 1000
    {"previousBill": 50, "currentMonthBill": 100, "nextMonthBill": 150},
    {"previousBill": 150, "currentMonthBill": 200, "nextMonthBill": 250},
    {"previousBill": 250, "currentMonthBill": 300, "nextMonthBill": 350},
    {"previousBill": 350, "currentMonthBill": 400, "nextMonthBill": 450},
    {"previousBill": 450, "currentMonthBill": 500, "nextMonthBill": 550},
    {"previousBill": 550, "currentMonthBill": 600, "nextMonthBill": 650},
    {"previousBill": 650, "currentMonthBill": 700, "nextMonthBill": 750},
    {"previousBill": 750, "currentMonthBill": 800, "nextMonthBill": 850},
    {"previousBill": 850, "currentMonthBill": 900, "nextMonthBill": 950},
    {"previousBill": 950, "currentMonthBill": 1000, "nextMonthBill": 1050},
    # Additional historical data with decreasing order from 1000 to 100
    {"previousBill": 1050, "currentMonthBill": 1000, "nextMonthBill": 950},
    {"previousBill": 950, "currentMonthBill": 900, "nextMonthBill": 850},
    {"previousBill": 850, "currentMonthBill": 800, "nextMonthBill": 750},
    {"previousBill": 750, "currentMonthBill": 700, "nextMonthBill": 650},
    {"previousBill": 650, "currentMonthBill": 600, "nextMonthBill": 550},
    {"previousBill": 550, "currentMonthBill": 500, "nextMonthBill": 450},
    {"previousBill": 450, "currentMonthBill": 400, "nextMonthBill": 350},
    {"previousBill": 350, "currentMonthBill": 300, "nextMonthBill": 250},
    {"previousBill": 250, "currentMonthBill": 200, "nextMonthBill": 150},
    {"previousBill": 150, "currentMonthBill": 100, "nextMonthBill": 50},
    
    {"previousBill": 1000, "currentMonthBill": 1100, "nextMonthBill": 1200},
    {"previousBill": 1200, "currentMonthBill": 1300, "nextMonthBill": 1400},
    {"previousBill": 1400, "currentMonthBill": 1500, "nextMonthBill": 1600},
    {"previousBill": 1600, "currentMonthBill": 1700, "nextMonthBill": 1800},
    {"previousBill": 1800, "currentMonthBill": 1900, "nextMonthBill": 2000},
    {"previousBill": 2000, "currentMonthBill": 2100, "nextMonthBill": 2200},
    {"previousBill": 2200, "currentMonthBill": 2300, "nextMonthBill": 2400},
    {"previousBill": 2400, "currentMonthBill": 2500, "nextMonthBill": 2600},
    {"previousBill": 2600, "currentMonthBill": 2700, "nextMonthBill": 2800},
    {"previousBill": 2800, "currentMonthBill": 2900, "nextMonthBill": 3000},
    # Additional historical data with decreasing order from 3000 to 1000
    {"previousBill": 3000, "currentMonthBill": 2900, "nextMonthBill": 2800},
    {"previousBill": 2800, "currentMonthBill": 2700, "nextMonthBill": 2600},
    {"previousBill": 2600, "currentMonthBill": 2500, "nextMonthBill": 2400},
    {"previousBill": 2400, "currentMonthBill": 2300, "nextMonthBill": 2200},
    {"previousBill": 2200, "currentMonthBill": 2100, "nextMonthBill": 2000},
    {"previousBill": 2000, "currentMonthBill": 1900, "nextMonthBill": 1800},
    {"previousBill": 1800, "currentMonthBill": 1800, "nextMonthBill": 1700},
    {"previousBill": 1700, "currentMonthBill": 1600, "nextMonthBill": 1500},
    {"previousBill": 1500, "currentMonthBill": 1400, "nextMonthBill": 1300},
    {"previousBill": 1300, "currentMonthBill": 1200, "nextMonthBill": 1100},
    
    {"previousBill": 3000, "currentMonthBill": 3100, "nextMonthBill": 3200},
    {"previousBill": 3200, "currentMonthBill": 3300, "nextMonthBill": 3400},
    {"previousBill": 3400, "currentMonthBill": 3500, "nextMonthBill": 3600},
    {"previousBill": 3600, "currentMonthBill": 3700, "nextMonthBill": 3800},
    {"previousBill": 3800, "currentMonthBill": 3900, "nextMonthBill": 4000},
    {"previousBill": 4000, "currentMonthBill": 4100, "nextMonthBill": 4200},
    {"previousBill": 4200, "currentMonthBill": 4300, "nextMonthBill": 4400},
    {"previousBill": 4400, "currentMonthBill": 4500, "nextMonthBill": 4600},
    {"previousBill": 4600, "currentMonthBill": 4700, "nextMonthBill": 4800},
    {"previousBill": 4800, "currentMonthBill": 4900, "nextMonthBill": 5000},
    {"previousBill": 5000, "currentMonthBill": 5100, "nextMonthBill": 5200},
    {"previousBill": 5200, "currentMonthBill": 5300, "nextMonthBill": 5400},
    
    {"previousBill": 5400, "currentMonthBill": 5500, "nextMonthBill": 5600},
    {"previousBill": 5600, "currentMonthBill": 5700, "nextMonthBill": 5800},
    {"previousBill": 5800, "currentMonthBill": 5900, "nextMonthBill": 6000},
    {"previousBill": 6000, "currentMonthBill": 6100, "nextMonthBill": 6200},
    {"previousBill": 6200, "currentMonthBill": 6300, "nextMonthBill": 6400},
    {"previousBill": 6400, "currentMonthBill": 6500, "nextMonthBill": 6600},
    {"previousBill": 6600, "currentMonthBill": 6700, "nextMonthBill": 6800},
    {"previousBill": 6800, "currentMonthBill": 6900, "nextMonthBill": 7000},
    # Additional historical data with decreasing order from 7000 to 3000
    {"previousBill": 7000, "currentMonthBill": 6900, "nextMonthBill": 6800},
    {"previousBill": 6800, "currentMonthBill": 6700, "nextMonthBill": 6600},
    {"previousBill": 6600, "currentMonthBill": 6500, "nextMonthBill": 6400},
    {"previousBill": 6400, "currentMonthBill": 6300, "nextMonthBill": 6200},
    {"previousBill": 6200, "currentMonthBill": 6200, "nextMonthBill": 6100},
    {"previousBill": 6000, "currentMonthBill": 5900, "nextMonthBill": 5800},
    {"previousBill": 5800, "currentMonthBill": 5800, "nextMonthBill": 5700},
    {"previousBill": 5700, "currentMonthBill": 5600, "nextMonthBill": 5500},
    {"previousBill": 5500, "currentMonthBill": 5400, "nextMonthBill": 5300},
    {"previousBill": 5300, "currentMonthBill": 5200, "nextMonthBill": 5100},
    {"previousBill": 5100, "currentMonthBill": 5000, "nextMonthBill": 4900},
    {"previousBill": 4900, "currentMonthBill": 4800, "nextMonthBill": 4700},
    {"previousBill": 4700, "currentMonthBill": 4600, "nextMonthBill": 4500},
    {"previousBill": 4500, "currentMonthBill": 4400, "nextMonthBill": 4300},
    {"previousBill": 4300, "currentMonthBill": 4200, "nextMonthBill": 4100},
    {"previousBill": 4100, "currentMonthBill": 4000, "nextMonthBill": 3900},
    {"previousBill": 3900, "currentMonthBill": 3800, "nextMonthBill": 3700},
    {"previousBill": 3700, "currentMonthBill": 3600, "nextMonthBill": 3500},
    {"previousBill": 3500, "currentMonthBill": 3400, "nextMonthBill": 3300},
    {"previousBill": 3300, "currentMonthBill": 3200, "nextMonthBill": 3100},
    {"previousBill": 3200, "currentMonthBill": 3100, "nextMonthBill": 3000},
    
    {"previousBill": 7000, "currentMonthBill": 7100, "nextMonthBill": 7200},
    {"previousBill": 7200, "currentMonthBill": 7300, "nextMonthBill": 7400},
    {"previousBill": 7400, "currentMonthBill": 7500, "nextMonthBill": 7600},
    {"previousBill": 7600, "currentMonthBill": 7700, "nextMonthBill": 7800},
    {"previousBill": 7800, "currentMonthBill": 7900, "nextMonthBill": 8000},
    {"previousBill": 8000, "currentMonthBill": 8100, "nextMonthBill": 8200},
    {"previousBill": 8200, "currentMonthBill": 8300, "nextMonthBill": 8400},
    {"previousBill": 8400, "currentMonthBill": 8500, "nextMonthBill": 8600},
    {"previousBill": 8600, "currentMonthBill": 8700, "nextMonthBill": 8800},
    {"previousBill": 8800, "currentMonthBill": 8900, "nextMonthBill": 9000},
    {"previousBill": 9000, "currentMonthBill": 9100, "nextMonthBill": 9200},
    {"previousBill": 9200, "currentMonthBill": 9300, "nextMonthBill": 9400},
    {"previousBill": 9400, "currentMonthBill": 9500, "nextMonthBill": 9600},
    {"previousBill": 9600, "currentMonthBill": 9700, "nextMonthBill": 9800},
    {"previousBill": 9800, "currentMonthBill": 9900, "nextMonthBill": 10000},
    {"previousBill": 10000, "currentMonthBill": 10100, "nextMonthBill": 10200},
    {"previousBill": 10200, "currentMonthBill": 10300, "nextMonthBill": 10400},
    {"previousBill": 10400, "currentMonthBill": 10500, "nextMonthBill": 10600},
    {"previousBill": 10600, "currentMonthBill": 10700, "nextMonthBill": 10800},
    {"previousBill": 10800, "currentMonthBill": 10900, "nextMonthBill": 11000},
    {"previousBill": 11000, "currentMonthBill": 11100, "nextMonthBill": 11200},
    {"previousBill": 11200, "currentMonthBill": 11300, "nextMonthBill": 11400},
    {"previousBill": 11400, "currentMonthBill": 11500, "nextMonthBill": 11600},
    {"previousBill": 11600, "currentMonthBill": 11700, "nextMonthBill": 11800},
    {"previousBill": 11800, "currentMonthBill": 11900, "nextMonthBill": 12000},
    # Additional historical data with decreasing order from 12000 to 7000
    {"previousBill": 12000, "currentMonthBill": 11900, "nextMonthBill": 11800},
    {"previousBill": 11800, "currentMonthBill": 11700, "nextMonthBill": 11600},
    {"previousBill": 11600, "currentMonthBill": 11500, "nextMonthBill": 11400},
    {"previousBill": 11400, "currentMonthBill": 11300, "nextMonthBill": 11200},
    {"previousBill": 11200, "currentMonthBill": 11100, "nextMonthBill": 11000},
    {"previousBill": 11000, "currentMonthBill": 10900, "nextMonthBill": 10800},
    {"previousBill": 10800, "currentMonthBill": 10700, "nextMonthBill": 10600},
    {"previousBill": 10600, "currentMonthBill": 10500, "nextMonthBill": 10400},
    {"previousBill": 10400, "currentMonthBill": 10300, "nextMonthBill": 10200},
    {"previousBill": 10200, "currentMonthBill": 10100, "nextMonthBill": 10000},
    {"previousBill": 10000, "currentMonthBill": 9900, "nextMonthBill": 9800},
    {"previousBill": 9800, "currentMonthBill": 9700, "nextMonthBill": 9600},
    {"previousBill": 9600, "currentMonthBill": 9500, "nextMonthBill": 9400},
    {"previousBill": 9400, "currentMonthBill": 9300, "nextMonthBill": 9200},
    {"previousBill": 9200, "currentMonthBill": 9100, "nextMonthBill": 9000},
    {"previousBill": 9000, "currentMonthBill": 8900, "nextMonthBill": 8800},
    {"previousBill": 8800, "currentMonthBill": 8700, "nextMonthBill": 8600},
    {"previousBill": 8600, "currentMonthBill": 8500, "nextMonthBill": 8400},
    {"previousBill": 8400, "currentMonthBill": 8300, "nextMonthBill": 8200},
    {"previousBill": 8200, "currentMonthBill": 8100, "nextMonthBill": 8000},
    {"previousBill": 8000, "currentMonthBill": 7900, "nextMonthBill": 7800},
    {"previousBill": 7800, "currentMonthBill": 7700, "nextMonthBill": 7600},
    {"previousBill": 7600, "currentMonthBill": 7500, "nextMonthBill": 7400},
    {"previousBill": 7400, "currentMonthBill": 7300, "nextMonthBill": 7200},
    
    {"previousBill": 12000, "currentMonthBill": 12100, "nextMonthBill": 12200},
    {"previousBill": 12200, "currentMonthBill": 12300, "nextMonthBill": 12400},
    {"previousBill": 12400, "currentMonthBill": 12500, "nextMonthBill": 12600},
    {"previousBill": 12600, "currentMonthBill": 12700, "nextMonthBill": 12800},
    {"previousBill": 12800, "currentMonthBill": 12900, "nextMonthBill": 13000},
    {"previousBill": 13000, "currentMonthBill": 13100, "nextMonthBill": 13200},
    {"previousBill": 13200, "currentMonthBill": 13300, "nextMonthBill": 13400},
    {"previousBill": 13400, "currentMonthBill": 13500, "nextMonthBill": 13600},
    {"previousBill": 13600, "currentMonthBill": 13700, "nextMonthBill": 13800},
    {"previousBill": 13800, "currentMonthBill": 13900, "nextMonthBill": 14000},
    {"previousBill": 14000, "currentMonthBill": 14100, "nextMonthBill": 14200},
    {"previousBill": 14200, "currentMonthBill": 14300, "nextMonthBill": 14400},
    {"previousBill": 14400, "currentMonthBill": 14500, "nextMonthBill": 14600},
    {"previousBill": 14600, "currentMonthBill": 14700, "nextMonthBill": 14800},
    {"previousBill": 14800, "currentMonthBill": 14900, "nextMonthBill": 15000},
    {"previousBill": 15000, "currentMonthBill": 15100, "nextMonthBill": 15200},
    {"previousBill": 15200, "currentMonthBill": 15300, "nextMonthBill": 15400},
    {"previousBill": 15400, "currentMonthBill": 15500, "nextMonthBill": 15600},
    {"previousBill": 15600, "currentMonthBill": 15700, "nextMonthBill": 15800},
    {"previousBill": 15800, "currentMonthBill": 15900, "nextMonthBill": 16000},
    # Additional historical data with decreasing order from 16000 to 12000
    {"previousBill": 16000, "currentMonthBill": 15900, "nextMonthBill": 15800},
    {"previousBill": 15800, "currentMonthBill": 15700, "nextMonthBill": 15600},
    {"previousBill": 15600, "currentMonthBill": 15500, "nextMonthBill": 15400},
    {"previousBill": 15400, "currentMonthBill": 15300, "nextMonthBill": 15200},
    {"previousBill": 15200, "currentMonthBill": 15100, "nextMonthBill": 15000},
    {"previousBill": 15000, "currentMonthBill": 14900, "nextMonthBill": 14800},
    {"previousBill": 14800, "currentMonthBill": 14700, "nextMonthBill": 14600},
    {"previousBill": 14600, "currentMonthBill": 14500, "nextMonthBill": 14400},
    {"previousBill": 14400, "currentMonthBill": 14300, "nextMonthBill": 14200},
    {"previousBill": 14200, "currentMonthBill": 14100, "nextMonthBill": 14000},
    {"previousBill": 14000, "currentMonthBill": 13900, "nextMonthBill": 13800},
    {"previousBill": 13800, "currentMonthBill": 13700, "nextMonthBill": 13600},
    {"previousBill": 13600, "currentMonthBill": 13500, "nextMonthBill": 13400},
    {"previousBill": 13400, "currentMonthBill": 13300, "nextMonthBill": 13200},
    {"previousBill": 13200, "currentMonthBill": 13100, "nextMonthBill": 13000},
    {"previousBill": 13000, "currentMonthBill": 12900, "nextMonthBill": 12800},
    {"previousBill": 12800, "currentMonthBill": 12700, "nextMonthBill": 12600},
    {"previousBill": 12600, "currentMonthBill": 12500, "nextMonthBill": 12400},
    {"previousBill": 12400, "currentMonthBill": 12300, "nextMonthBill": 12200},
    {"previousBill": 12200, "currentMonthBill": 12100, "nextMonthBill": 12000},
    
    {"previousBill": 16000, "currentMonthBill": 16100, "nextMonthBill": 16200},
    {"previousBill": 16200, "currentMonthBill": 16300, "nextMonthBill": 16400},
    {"previousBill": 16400, "currentMonthBill": 16500, "nextMonthBill": 16600},
    {"previousBill": 16600, "currentMonthBill": 16700, "nextMonthBill": 16800},
    {"previousBill": 16800, "currentMonthBill": 16900, "nextMonthBill": 17000},
    {"previousBill": 17000, "currentMonthBill": 17100, "nextMonthBill": 17200},
    {"previousBill": 17200, "currentMonthBill": 17300, "nextMonthBill": 17400},
    {"previousBill": 17400, "currentMonthBill": 17500, "nextMonthBill": 17600},
    {"previousBill": 17600, "currentMonthBill": 17700, "nextMonthBill": 17800},
    {"previousBill": 17800, "currentMonthBill": 17900, "nextMonthBill": 18000},
    {"previousBill": 18000, "currentMonthBill": 18100, "nextMonthBill": 18200},
    {"previousBill": 18200, "currentMonthBill": 18300, "nextMonthBill": 18400},
    {"previousBill": 18400, "currentMonthBill": 18500, "nextMonthBill": 18600},
    {"previousBill": 18600, "currentMonthBill": 18700, "nextMonthBill": 18800},
    {"previousBill": 18800, "currentMonthBill": 18900, "nextMonthBill": 19000},
    {"previousBill": 19000, "currentMonthBill": 19100, "nextMonthBill": 19200},
    {"previousBill": 19200, "currentMonthBill": 19300, "nextMonthBill": 19400},
    {"previousBill": 19400, "currentMonthBill": 19500, "nextMonthBill": 19600},
    {"previousBill": 19600, "currentMonthBill": 19700, "nextMonthBill": 19800},
    {"previousBill": 19800, "currentMonthBill": 19900, "nextMonthBill": 20000},
    # Additional historical data with decreasing order from 20000 to 16000
    {"previousBill": 20000, "currentMonthBill": 19900, "nextMonthBill": 19800},
    {"previousBill": 19800, "currentMonthBill": 19700, "nextMonthBill": 19600},
    {"previousBill": 19600, "currentMonthBill": 19500, "nextMonthBill": 19400},
    {"previousBill": 19400, "currentMonthBill": 19300, "nextMonthBill": 19200},
    {"previousBill": 19200, "currentMonthBill": 19100, "nextMonthBill": 19000},
    {"previousBill": 19000, "currentMonthBill": 18900, "nextMonthBill": 18800},
    {"previousBill": 18800, "currentMonthBill": 18700, "nextMonthBill": 18600},
    {"previousBill": 18600, "currentMonthBill": 18500, "nextMonthBill": 18400},
    {"previousBill": 18400, "currentMonthBill": 18300, "nextMonthBill": 18200},
    {"previousBill": 18200, "currentMonthBill": 18100, "nextMonthBill": 18000},
    {"previousBill": 18000, "currentMonthBill": 17900, "nextMonthBill": 17800},
    {"previousBill": 17800, "currentMonthBill": 17700, "nextMonthBill": 17600},
    {"previousBill": 17600, "currentMonthBill": 17500, "nextMonthBill": 17400},
    {"previousBill": 17400, "currentMonthBill": 17300, "nextMonthBill": 17200},
    {"previousBill": 17200, "currentMonthBill": 17100, "nextMonthBill": 17000},
    {"previousBill": 17000, "currentMonthBill": 16900, "nextMonthBill": 16800},
    {"previousBill": 16800, "currentMonthBill": 16700, "nextMonthBill": 16600},
    {"previousBill": 16600, "currentMonthBill": 16500, "nextMonthBill": 16400},
    {"previousBill": 16400, "currentMonthBill": 16300, "nextMonthBill": 16200},
    {"previousBill": 16200, "currentMonthBill": 16100, "nextMonthBill": 16000},

]


# Train the linear regression model
X = [[entry["previousBill"], entry["currentMonthBill"]] for entry in historical_data]
y = [entry["nextMonthBill"] for entry in historical_data]
model = LinearRegression()
model.fit(X, y)

# Endpoint for making predictions
@app.route('/api/predict-next-month-bill', methods=['POST'])
def predict_next_month_bill():
    data = request.get_json()
    previous_bill = data.get('previousBill')
    current_month_bill = data.get('currentMonthBill')

    # Perform prediction
    next_month_prediction = make_prediction(float(previous_bill), float(current_month_bill))

    # Generate feedback
    feedback_message = generate_feedback(float(previous_bill), float(current_month_bill), next_month_prediction)

    return jsonify({
        'nextMonthPrediction': next_month_prediction,
        'feedbackMessage': feedback_message
    })

def make_prediction(previous_bill, current_month_bill):
    next_month_prediction = model.predict([[previous_bill, current_month_bill]])
    return round(next_month_prediction[0], 2)

def generate_feedback(previousBill, current_month_bill, next_month_prediction):
    if next_month_prediction < current_month_bill:
        feedback_message = "Based on your current spending pattern, your next month's bill is predicted to decrease. Great job on managing your expenses!"
    elif next_month_prediction == current_month_bill:
        feedback_message = "Based on your current spending pattern, your next month's bill is predicted to remain the same. Keep up the good work!"
    else:
        feedback_message = "Based on your current spending pattern, your next month's bill is predicted to increase. Consider budgeting or reducing expenses."

    return feedback_message


  



if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Run Flask app on port 5001
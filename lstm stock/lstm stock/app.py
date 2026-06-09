from flask import Flask, render_template, request
import numpy as np
import joblib
import yfinance as yf
from tensorflow.keras.models import load_model

app = Flask(__name__)

company_map = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Google": "GOOGL",
    "Amazon": "AMZN",
    "Tesla": "TSLA",
    "Meta": "META",
    "Netflix": "NFLX",
    "Nvidia": "NVDA",
    "TCS": "TCS.NS",
    "Infosys": "INFY.NS",
    "Reliance": "RELIANCE.NS"
}

models = {}
scalers = {}

for name, ticker in company_map.items():
    models[ticker] = load_model(f"models/{ticker}.h5")
    scalers[ticker] = joblib.load(f"scalers/{ticker}_scaler.pkl")

@app.route('/')
def home():
    return render_template('index.html', companies=company_map.keys())

@app.route('/predict', methods=['POST'])
def predict():
    company_name = request.form['company']
    ticker = company_map[company_name]
    
    model = models[ticker]
    scaler = scalers[ticker]
    
    df = yf.download(ticker, period="3mo")
    close_data = df[['Close']].values
    
    scaled_data = scaler.transform(close_data)
    
    last_60 = scaled_data[-60:]
    X_input = last_60.reshape(1, 60, 1)
    
    prediction = model.predict(X_input)
    predicted_price = scaler.inverse_transform(prediction)[0][0]
    
    current_price = close_data[-1][0]
    
    if predicted_price > current_price + 1:
        status = "📈 Market likely to RISE"
        color = "green"
    elif predicted_price < current_price - 1:
        status = "📉 Market likely to FALL"
        color = "red"
    else:
        status = "➖ Market likely to remain STABLE"
        color = "orange"
    
    last_60_actual = scaler.inverse_transform(last_60).flatten()
    last_60_actual = [float(x) for x in last_60_actual]

    future_pred = float(predicted_price)

    graph_actual = last_60_actual
    graph_pred = last_60_actual[1:] + [future_pred]
    
    return render_template(
        'result.html',
        company=company_name,
        current=round(current_price, 2),
        predicted=round(predicted_price, 2),
        status=status,
        color=color,
        actual=graph_actual,
        predicted_list=graph_pred
    )

if __name__ == '__main__':
    app.run(debug=True)
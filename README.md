\# 📈 Stock Price Prediction using LSTM



A deep learning web application that predicts stock prices using Long Short-Term Memory (LSTM) neural networks.



\## 🚀 Demo

Upload a stock ticker and get future price predictions instantly through a clean web interface.



\## 📊 Supported Stocks

| Stock | Symbol |

|-------|--------|

| Apple | AAPL |

| Amazon | AMZN |

| Google | GOOGL |

| Microsoft | MSFT |

| Tesla | TSLA |

| Netflix | NFLX |

| NVIDIA | NVDA |

| Meta | META |

| Infosys | INFY.NS |

| TCS | TCS.NS |

| Reliance | RELIANCE.NS |



\## 🛠️ Tech Stack

\- \*\*Python\*\* - Core language

\- \*\*TensorFlow / Keras\*\* - LSTM model

\- \*\*Flask\*\* - Web framework

\- \*\*Pandas \& NumPy\*\* - Data processing

\- \*\*Matplotlib\*\* - Visualization

\- \*\*Scikit-learn\*\* - Data scaling



\## 📁 Project Structure



lstm stock/

├── app.py               # Flask application

├── datasets/            # Historical stock CSVs

├── models/              # Trained LSTM models (.h5)

├── scalers/             # Saved scalers (.pkl)

├── templates/           # HTML pages

│   ├── index.html

│   └── result.html

└── static/

└── style.css





\## ⚙️ Installation



1\. Clone the repository

```bash

git clone https://github.com/Anudheeph/Stock-Price-Prediction.git

cd Stock-Price-Prediction

```



2\. Install dependencies

```bash

pip install flask tensorflow pandas numpy scikit-learn matplotlib

```



3\. Run the app

```bash

python app.py

```



4\. Open your browser and go to `http://localhost:5000`



\## 📌 How It Works

1\. Historical stock data is loaded from CSV files

2\. Data is scaled using MinMaxScaler

3\. LSTM model predicts future closing prices

4\. Results are displayed as interactive charts



\## 👨‍💻 Author

\*\*Anudheeph\*\*  

\[GitHub](https://github.com/Anudheeph)


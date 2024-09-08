# Stock Market Prediction App

Welcome to the Stock Market Prediction App! This application utilizes machine learning model to predict stock prices. It leverages historical data to train an LSTM-based model and provides predictions for future stock prices.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Model Description](#model-description)
4. [App Description](#app-description)
5. [How to Use the App](#how-to-use)

## Installation <a id="installation"></a>

To get started, you'll need to install the required Python packages. Follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jadhav-kunal/stock-market-prediction.git
   cd stock-market-prediction-app
   ```

2. **Install the dependencies**:
   Make sure you have `pip` installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage <a id="usage"></a>

To run the application, use Streamlit. Make sure you're in the root directory of the project, then execute the following command:

```bash
streamlit run stock.py
```

This will start a local server, and you can access the web application via your browser at `http://localhost:8501`.

## Model Description <a id="model-description"></a>

The app uses an LSTM (Long Short-Term Memory) model to predict future stock prices based on historical data. Here's a brief overview of how the model works:

1. **Data Preparation**:
   - Historical stock data is fetched using the `yfinance` library.
   - The data is scaled using `MinMaxScaler` for normalization.
   - A dataset matrix is created using a time step of 15 to define the input and output sequences.

2. **Model Building**:
   - An LSTM model is built with three LSTM layers and one Dense layer.
   - The model is compiled with the Adam optimizer and mean squared error loss function.
   - It is trained on the historical stock data.

3. **Prediction**:
   - The model predicts stock prices for both the training and testing sets.
   - Predictions are inverse-transformed to match the original scale.
   - Future stock prices for the next 30 days are forecasted using the trained model.

## App Description <a id="app-description"></a>

The web application provides an interface for users to visualize stock price predictions. It includes:

- **Historical Data Visualization**: Displays historical stock prices along with the model's predictions.
- **Future Price Forecast**: Shows predictions for the next 30 days based on the trained LSTM model.

## How to Use the App <a id="how-to-use"></a>
1. Select a Stock:

Use the dropdown menu to choose the stock symbol you want to analyze. This will fetch the historical data for the selected stock:

![Screenshot 2024-09-08 at 9 00 53 PM](https://github.com/user-attachments/assets/3f1095c9-bdf2-4d41-87e9-c735e42ea5ab)

2. Choose the time range for the analysis using the date picker controls. You can select a custom range to tailor the analysis to your needs.
Submit:
![image](https://github.com/user-attachments/assets/f8c8ac86-0370-46f1-a01e-b66aec12410e)

Click the "Submit" button to start the analysis. The app will fetch the data, train the model, and generate predictions. This may take a few moments depending on the stock and time range selected.

3. Review Results:

Graphs: The app will display graphs showing historical stock prices, along with the model's predictions.
Next 30 Days Prediction: View the forecast for the next 30 days. This will include predicted stock prices for each day in this future period.

![image](https://github.com/user-attachments/assets/d4910623-c6e8-4aef-a195-9a9c8eab9287)
![Screenshot 2024-09-08 at 9 07 14 PM](https://github.com/user-attachments/assets/c4e3dc08-9d7c-4046-a905-59b5113ca384)


Happy predicting! 📈

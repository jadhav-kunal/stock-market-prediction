import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import datetime
import streamlit as st
import model_building as m

# Define a list of available stock symbols
available_stocks = ['RELIANCE', 'BRITANNIA', 'ADANIENT', 'ASIANPAINT', 'SUZLON', 'TATAMOTORS', 'IRCTC', 'SBIN', 'FEDERALBNK']

# Sidebar for user input
with st.sidebar:
    st.markdown("# Stock Market Prediction")
    user_input = st.selectbox('Please select the stock', available_stocks, index=0)
    user_input = user_input + '.NS'
    st.markdown("Choose Date for your analysis")
    START = st.date_input("From", datetime.date(2020, 1, 1))
    END = st.date_input("To", datetime.date(2024, 5, 30))
    bt = st.button('Submit')

# Adding a button to submit and process data
if bt:
# Importing dataset------------------------------------------------------
    df = yf.download(user_input, start=START, end=END)
    plotdf, future_predicted_values =m.create_model(df)
    df.reset_index(inplace = True)
    st.title('Stock Market Prediction')
    st.header(f'Data collected from the source for {user_input}')
    st.write(df)

    stockname_1=df.drop(["Adj Close"],axis=1).reset_index(drop=True)
    stockname_2=stockname_1.dropna().reset_index(drop=True)

    stockname=stockname_2.copy()
    stockname['Date']=pd.to_datetime(stockname['Date'],format='%Y-%m-%d')
    stockname=stockname.set_index('Date')
    st.title('EDA')
    st.write(stockname)


# ---------------------------Graphs--------------------------------------

    st.title('Visualizations')

    st.header("Graphs")
    plt.figure(figsize=(20,10))
    #Plot 1
    plt.subplot(2,2,1)
    plt.plot(stockname['Open'],color='green')
    plt.xlabel('Date')
    plt.ylabel('Open Price')
    plt.title('Open')
    #Plot 2
    plt.subplot(2,2,2)
    plt.plot(stockname['Close'],color='red')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title('Close')
    #Plot 3
    plt.subplot(2,2,3)
    plt.plot(stockname['High'],color='green')
    plt.xlabel('Date')
    plt.ylabel('High Price')
    plt.title('High')
    #Plot 4
    plt.subplot(2,2,4)
    plt.plot(stockname['Low'],color='red')
    plt.xlabel('Date')
    plt.ylabel('Low Price')
    plt.title('Low')
    st.pyplot()

#------------------------box-plots---------------------------------

    # Creating box-plots
    st.header("Box Plots")

    plt.figure(figsize=(20,10))
    #Plot 1
    plt.subplot(2,2,1)
    plt.boxplot(stockname['Open'])
    plt.xlabel('Date')
    plt.ylabel('Open Price')
    plt.title('Open')
    #Plot 2
    plt.subplot(2,2,2)
    plt.boxplot(stockname['Close'])
    plt.xlabel('Date')
    plt.ylabel('Cloes Price')
    plt.title('Close')
    #Plot 3
    plt.subplot(2,2,3)
    plt.boxplot(stockname['High'])
    plt.xlabel('Date')
    plt.ylabel('High Price')
    plt.title('High')
    #Plot 4
    plt.subplot(2,2,4)
    plt.boxplot(stockname['Low'])
    plt.xlabel('Date')
    plt.ylabel('Low Price')
    plt.title('Low')
    st.pyplot()

#---------------------Histogram---------------------------------------

    st.header("Histogram")
    # Ploting Histogram
    plt.figure(figsize=(20,10))
    #Plot 1
    plt.subplot(2,2,1)
    plt.hist(stockname['Open'],bins=50, color='green')
    plt.xlabel("Open Price")
    plt.ylabel("Frequency")
    plt.title('Open')
    #Plot 2
    plt.subplot(2,2,2)
    plt.hist(stockname['Close'],bins=50, color='red')
    plt.xlabel("Close Price")
    plt.ylabel("Frequency")
    plt.title('Close')
    #Plot 3
    plt.subplot(2,2,3)
    plt.hist(stockname['High'],bins=50, color='green')
    plt.xlabel("High Price")
    plt.ylabel("Frequency")
    plt.title('High')
    #Plot 4
    plt.subplot(2,2,4)
    plt.hist(stockname['Low'],bins=50, color='red')
    plt.xlabel("Low Price")
    plt.ylabel("Frequency")
    plt.title('Low')
    st.pyplot()


#-------------------------KDE Plots-----------------------------------------

    st.header("KDE Plots")
    # KDE-Plots
    plt.figure(figsize=(20,10))
    #Plot 1
    plt.subplot(2,2,1)
    sns.kdeplot(stockname['Open'], color='green')
    plt.title('Open')
    #Plot 2
    plt.subplot(2,2,2)
    sns.kdeplot(stockname['Close'], color='red')
    plt.title('Close')
    #Plot 3
    plt.subplot(2,2,3)
    sns.kdeplot(stockname['High'], color='green')
    plt.title('High')
    #Plot 4
    plt.subplot(2,2,4)
    sns.kdeplot(stockname['Low'], color='red')
    plt.title('Low')
    st.pyplot()


    st.header('Years vs Volume')
    st.line_chart(stockname['Volume'])


#-------------------Finding long-term and short-term trends---------------------

    st.title('Finding long-term and short-term trends')
    stockname_ma=stockname.copy()
    stockname_ma['30-day MA']=stockname['Close'].rolling(window=30).mean()
    stockname_ma['200-day MA']=stockname['Close'].rolling(window=200).mean()

    st.write(stockname_ma)


    st.subheader('Stock Price vs 30-day Moving Average')
    plt.plot(stockname_ma['Close'],label='Original data')
    plt.plot(stockname_ma['30-day MA'],label='30-MA')
    plt.legend()
    plt.title('Stock Price vs 30-day Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Price')
    st.pyplot()


    st.subheader('Stock Price vs 200-day Moving Average')
    plt.plot(stockname_ma['Close'],label='Original data')
    plt.plot(stockname_ma['200-day MA'],label='200-MA')
    plt.legend()
    plt.title('Stock Price vs 200-day Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Price')
    st.pyplot()

    df1 = pd.DataFrame(future_predicted_values)
    st.markdown("### Next 30 days forecast")
    df1.rename(columns={0: "Predicted Prices"}, inplace=True)
    st.write(df1)

    st.markdown("### Original vs predicted close price")
    fig= plt.figure(figsize=(20,10))
    sns.lineplot(data=plotdf)
    st.pyplot(fig)
    
    
else:
    st.markdown("### Please click on the submit button to get the EDA and Prediction")
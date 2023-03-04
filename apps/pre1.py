import numpy as np
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import yfinance as yf
from keras.models import load_model
import streamlit as st

def app():
    yf.pdr_override()
    
    start = dt.datetime(2010,1,1)
    end = dt.datetime(2019,12,31)
    
    
    st.title('Stock Treand Prediction')
    
    user_input = st.text_input('Enter Stock Ticker', 'AAPL')
    df = web.get_data_yahoo(user_input, start, end)
    
    #describing data
    st.subheader('Data from 2010 - 2019')
    st.write(df.describe())

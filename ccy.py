import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px

# Streamlit app title
st.title('為替の日中データチャート')

# User input for the currency pair
currency_pair = st.text_input('通貨ペアを入力してください（例：USDJPY=X）', 'USDJPY=X')

# User input for the date range
start_date = st.date_input('開始日を選択してください')
end_date = st.date_input('終了日を選択してください')

# Fetching the currency data with 1-hour interval
data = yf.download(currency_pair, start=start_date, end=end_date, interval='1m')

# Check if data is empty
if data.empty:
    st.write('指定された期間でのデータが見つかりません。')
else:
    # Plotting the closing prices
    fig = px.line(data, x=data.index, y='Close', title=f'{currency_pair} の日中データ')
    st.plotly_chart(fig)

    # Displaying the raw data
    st.write('生データ:')
    st.dataframe(data)

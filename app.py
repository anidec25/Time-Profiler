import pandas as pd
import numpy as np

import streamlit as st

from io import StringIO

import altair as alt
import plotly as plt



def load_csv():
    
    df_input = pd.DataFrame()  
    df_input=pd.read_csv(input,sep=None ,engine='python', encoding='utf-8',
                            parse_dates=True,
                            infer_datetime_format=True)
    return df_input


def prep_data(df):

    df_input = df.rename({date_col:"ds",metric_col:"y"},errors='raise',axis=1)
    st.markdown("The selected date column is now labeled as **ds** and the values columns as **y**")
    df_input = df_input[['ds','y']]
    df_input =  df_input.sort_values(by='ds',ascending=True)
    return df_input


st.title('Forecasting Application')
st.write('This app enables you to generate time series forecast withouth any dependencies.')
st.markdown("""The forecasting library used is **[Prophet](https://facebook.github.io/prophet/)**.""")

df =  pd.DataFrame()  


input = st.file_uploader('')

if input is None:
    st.write("Or use sample dataset to try the application")
    sample = st.checkbox("Download sample data from GitHub")

try:
    if sample:
        st.markdown("""[download_link](https://raw.githubusercontent.com/anidec25/Time-Profiler/main/data/daily-minimum-temperatures-in-me.csv)""")    
        
except:

    if input:
        with st.spinner('Loading data..'):
            df = load_csv()
    
            st.write("Columns:")
            st.write(df.describe())

            st.write(df.head())
            columns = list(df.columns)

            col1,col2 = st.columns(2)
            with col1:
                date_col = st.selectbox("Select date column",index= 0,options=columns,key="date")
            with col2:
                metric_col = st.selectbox("Select values column",index=1,options=columns,key="values")

            df = prep_data(df)
            output = 0


    if st.checkbox('Chart data',key='show'):
        with st.spinner('Plotting data..'):
            col1,col2 = st.columns(2)
            with col1:
                st.dataframe(df)
                
            with col2:    
                st.write("Dataframe description:")
                st.write(df.describe())
        
        try:
                line_chart = alt.Chart(df).mark_line().encode(
                    x = 'ds:T',
                    y = "y:Q",tooltip=['ds:T', 'y']).properties(title="Time series preview").interactive()
                st.altair_chart(line_chart,use_container_width=True)
                
        except:
            st.line_chart(df['y'],use_container_width =True,height = 300)


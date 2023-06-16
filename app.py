import pandas as pd
import numpy as np
import streamlit as st
from io import StringIO



def load_csv():
    
    df_input = pd.DataFrame()  
    df_input=pd.read_csv(input,sep=None ,engine='python', encoding='utf-8',
                            parse_dates=True,
                            infer_datetime_format=True)
    return df_input


input = st.file_uploader('')
    
if input is None:
    st.write("Or use sample dataset to try the application")
    sample = st.checkbox("Download sample data from GitHub")

try:
    if sample:
        st.markdown("""[download_link](https://gist.github.com/giandata/e0b5c2d2e71d4fd4388295eb5b71aeeb)""")    
        
except:

    if input:
        with st.spinner('Loading data..'):
            df = load_csv()
    
            st.write("Columns:")
            st.write(list(df.columns))
            columns = list(df.columns)
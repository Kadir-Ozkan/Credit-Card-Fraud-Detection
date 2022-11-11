
# import the necessary packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import timeit
import warnings
warnings.filterwarnings("ignore")
import streamlit as st


df=st.cache(pd.read_csv)('creditcard.csv')
st.session_state['df'] = df



# Print valid and fraud transactions
fraud=df[df.Class==1]
valid=df[df.Class==0]
percent_fraud=(df.Class.value_counts()[1]/df.Class.value_counts()[0])*100
st.write('#### Dependent variable: Credit card fraud')
st.write('Fraudulent transactions are: %.3f%%'%percent_fraud)
st.write('Fraud Cases: ',len(fraud))
st.write('Valid Cases: ',len(valid))


# Print shape and description of the data
st.write('#### The Dataset:')
st.write('Shape of the dataframe: ',df.shape)
st.write(df.head(3))
st.write('#### Descriptive Statistics: \n',df.describe())

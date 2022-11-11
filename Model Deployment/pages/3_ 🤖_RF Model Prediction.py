from re import M
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image





st.markdown("<h1 style='text-align: center; color: Indigo;'>Credit Card Fraud Prediction</h1>", unsafe_allow_html=True)

_, col2, _ = st.columns([2.3, 3, 2])


with col2:  
    img = Image.open("Online-credit-card-fraud.jpg")
    st.image(img, width=320)


df=st.cache(pd.read_csv)('ccfraud_mini.csv')


col1, col2 = st.columns([4, 4])
with col1:
    st.markdown("###### Please select the time of the day")
    
    DayTime = st.radio("daytime",
            ('22-02-Hours', '03-09-Hours', '10-21-Hours')
        )


if DayTime == '03-09-Hours':
    DayTime = 1.0 
    
if DayTime == "10-21-Hours":
    DayTime = 2.0

else:
    DayTime = 3.0

        

with col2:
    st.markdown("###### Please select amount of transaction")
    TransactionAmount = st.slider(
        "Transaction Amount", min_value=int(df["amount"].min()), max_value=int(df["amount"].max()), step=1)
    

v1 = st.slider("Parameter 1:", min_value=float(df["v_1"].min()), max_value=float(df["v_1"].max()))
v2 = st.slider("Parameter 2:", min_value=float(df["v_2"].min()), max_value=float(df["v_2"].max()))
v3 = st.slider("Parameter 3:", min_value=float(df["v_3"].min()), max_value=float(df["v_3"].max()))
v4 = st.slider("Parameter 4:", min_value=float(df["v_4"].min()), max_value=float(df["v_4"].max()))
v5 = st.slider("Parameter 5:", min_value=float(df["v_5"].min()), max_value=float(df["v_5"].max()))
v6 = st.slider("Parameter 6:", min_value=float(df["v_6"].min()), max_value=float(df["v_6"].max()))
v7 = st.slider("Parameter 7:", min_value=float(df["v_7"].min()), max_value=float(df["v_7"].max()))
v8 = st.slider("Parameter 8:", min_value=float(df["v_8"].min()), max_value=float(df["v_8"].max()))
v9 = st.slider("Parameter 9:", min_value=float(df["v_9"].min()), max_value=float(df["v_9"].max()))
v10 = st.slider("Parameter 10:", min_value=float(df["v_10"].min()), max_value=float(df["v_10"].max()))
v11 = st.slider("Parameter 11:", min_value=float(df["v_11"].min()), max_value=float(df["v_11"].max()))
v12 = st.slider("Parameter 12:", min_value=float(df["v_12"].min()), max_value=float(df["v_12"].max()))
v13 = st.slider("Parameter 13:", min_value=float(df["v_13"].min()), max_value=float(df["v_13"].max()))
v14 = st.slider("Parameter 14:", min_value=float(df["v_14"].min()), max_value=float(df["v_14"].max()))
v15 = st.slider("Parameter 15:", min_value=float(df["v_15"].min()), max_value=float(df["v_15"].max()))
v16 = st.slider("Parameter 16:", min_value=float(df["v_16"].min()), max_value=float(df["v_16"].max()))
v17 = st.slider("Parameter 17:", min_value=float(df["v_17"].min()), max_value=float(df["v_17"].max()))
v18 = st.slider("Parameter 18:", min_value=float(df["v_18"].min()), max_value=float(df["v_18"].max()))
v19 = st.slider("Parameter 19:", min_value=float(df["v_19"].min()), max_value=float(df["v_19"].max()))
v20 = st.slider("Parameter 20:", min_value=float(df["v_20"].min()), max_value=float(df["v_20"].max()))
v21 = st.slider("Parameter 21:", min_value=float(df["v_21"].min()), max_value=float(df["v_21"].max()))
v22 = st.slider("Parameter 22:", min_value=float(df["v_22"].min()), max_value=float(df["v_22"].max()))
v23 = st.slider("Parameter 23:", min_value=float(df["v_23"].min()), max_value=float(df["v_23"].max()))
v24 = st.slider("Parameter 24:", min_value=float(df["v_24"].min()), max_value=float(df["v_24"].max()))
v25 = st.slider("Parameter 25:", min_value=float(df["v_25"].min()), max_value=float(df["v_25"].max()))
v26 = st.slider("Parameter 26:", min_value=float(df["v_26"].min()), max_value=float(df["v_26"].max()))
v27 = st.slider("Parameter 27:", min_value=float(df["v_27"].min()), max_value=float(df["v_27"].max()))
v28 = st.slider("Parameter 28:", min_value=float(df["v_28"].min()), max_value=float(df["v_28"].max()))



my_dict = {
    'daytime': DayTime,
    'amount': TransactionAmount,
    'v_1': v1,
    'v_2': v2,
    'v_3': v3,
    'v_4': v4,
    'v_5': v5,
    'v_6': v6,
    'v_7': v7,
    'v_8': v8,
    'v_9': v9,
    'v_10': v10,
    'v_11': v11,
    'v_12': v12,
    'v_13': v13,
    'v_14': v14,
    'v_15': v15,
    'v_16': v16,
    'v_17': v17,
    'v_18': v18,
    'v_19': v19,
    'v_20': v20,
    'v_21': v21,
    'v_22': v22,
    'v_23': v23,
    'v_24': v24,
    'v_25': v25,
    'v_26': v26,
    'v_27': v27,
    'v_28': v28,
}


df=pd.DataFrame.from_dict([my_dict])


import pickle
filename = 'FraudDetection_RF_Model.pkl'
model = pickle.load(open(filename, 'rb'))


col, col2 = st.columns([4, 4])

with col: 
    st.info("The Predictors of Credit Card Fraud")
    my_dict


with col2: 
    if st.button("Predict"):
        pred = model.predict(df)
        if int(pred[0]) == 1:
            st.error("This transaction is likely to be a fraud case")
        else:
            st.success("This transaction is UNLIKELY to be a fraud case")
            
st.markdown('###### Trained and Deployed by G2')

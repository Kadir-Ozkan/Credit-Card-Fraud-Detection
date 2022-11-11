import streamlit as st
from PIL import Image
import altair as alt



st.write("#### Number of fraud cases")
st.write("According to the following graph, number of fraud cases are not randomly distributed during the day. 02:00 and 11:00 are the two top time periods where the number of credit card fraud cases are at the highest level")
image1 = Image.open('figure_1.png')
st.image(image1, width=800)


st.write("#### Total amount of loss")
st.write("When we examine the amount lost to credit card frauds, we see some outlier values, particularly after $500 level.")

image2 = Image.open('figure_2.png')
st.image(image2, width=800)


st.write("#### Average amount of loss")
st.write("findings indicate that highest average losses occur during 24:00 and 10:00.")
image3 = Image.open('figure_3.png')
st.image(image3, width=800)





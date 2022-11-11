
# import the necessary packages
import streamlit as st
from PIL import Image


st.write("Since the size of the original data is over 150 MB, we could not upload it here. Instead, we have uploaded the screenshots of the outputs here.")


st.write("#### Dependent variable: Credit card fraud")
image1 = Image.open('fraud.png')
st.image(image1, width=700)


st.write("#### The Dataset:")
image2 = Image.open('shape.png')
st.image(image2, width=800)


st.write("#### Descriptive Statistics:")
image3 = Image.open('descriptives.png')
st.image(image3, width=800)



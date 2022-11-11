import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="No-Code Machine Learning",
    page_icon=":car:",
)


st.title("G2 Credit Card Fraud Detection Project")


"Hello visitor!" 
"Welcome to our streamlit page!" 
"In this web app, we present you the findings of our ML/DL project on credit card fraud detection. Hopefully, we will the the champion with this project."
"You can navigate the analysis pages using the sidebar on the left hand side."

"Best regards,"

"G2 Team"




page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://cyberdefender.hk/en-us/wp-content/uploads/2021/07/theif.png");
background-size: 30%;
background-position: bottom right;
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)



def navbar_component():
    with open("assets/images/settings.png", "rb") as image_file:
        image_as_base64 = base64.b64encode(image_file.read())

    navbar_items = ''
    for key, value in NAVBAR_PATHS.items():
        navbar_items += (f'<a class="navitem" href="/?nav={value}">{key}</a>')

    settings_items = ''
    for key, value in SETTINGS.items():
        settings_items += (
            f'<a href="/?nav={value}" class="settingsNav">{key}</a>')

    component = rf'''
            ....
    '''
    st.markdown(component, unsafe_allow_html=True)
    
    js = '''
    <script>
    ....
    </script>
    '''
    html(js)

#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Contents of ~/my_app/streamlit_app.py

import time  # to simulate a real time data, time loop
from PIL import Image
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
import plotly.express as px
import matplotlib.pyplot as plt
from typing import List, Tuple

st.set_page_config(
        page_title="DFRA Fraude Data Detection",
        page_icon=""
    )

st.write("# DFRA-OML : <br> Welcome to our web scraping app !", unsafe_allow_html=True)

def main_page():
    st.sidebar.success("Home")

    st.markdown(
        """
        <p style='color: Black and Neon Blue; font-size:20px;font-family: Arial; font-weight: bold'><strong> 👉 Web/Social media scraping relatif à la fraude Data.</strong></p>

       <p style='color: Black and Neon Blue; font-size:18px'> Ces résultats nous permettent d'avoir une idée d'une par sur le niveau d'attraction des internautes sur la fraude data et d'autre part, de comprendre, les techniques & outils utilisés pour baypasser nos système de facturation. Cela pourrait aider à prendre des décision afin de réduire le volume trafic data frauduleux.</p>
        <p style='color: darq green; font-size:20px;font-family: Arial; font-weight: bold'><strong> 👉 Source des données :</strong> </p> 
        <h2 style='color: Black and Neon Blue; font-size:15px;font-weight: bold' '>Google, Facebook, Instagram, Twitter, Telegram.</h2> </p>
        <p style='color: Black and Neon Blue; font-size:18px'> Pour chacune des sources, il existe des packages Python ou APIs dédiés pour le scraping.
        Les données extraites sont compilées, nétoyées et analysées à des fin de visualisation.</p>
        <p style='color: darq green; font-size:20px;font-family: Arial; font-weight: bold'><strong>👈 Select a page from the sidebar ! </strong> </p>

        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
            forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
            Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """, unsafe_allow_html=True
    )


def page2():
st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

def page3():
st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
"Main Page": main_page,
"Page 2": page2,
"Page 3": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()


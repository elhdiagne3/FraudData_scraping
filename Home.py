#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st

st.set_page_config(
        page_title="DFRA Fraude Data Detection",
        page_icon="",initial_sidebar_state="expanded"
    )

st.write("# DFRA-OML : <br> Welcome to our web scraping app !", unsafe_allow_html=True)

def show() : 
    
    st.sidebar.success("Select a demo above.")

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


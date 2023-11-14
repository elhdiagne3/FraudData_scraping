#!/usr/bin/env python
# coding: utf-8

# In[12]:


#!/usr/bin/env python
# coding: utf-8
# In[2]:
import time  # to simulate a real time data, time loop
from PIL import Image
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
import matplotlib.pyplot as plt
from typing import List, Tuple
import base64
import matplotlib.pyplot as plt
#from gensim.models import Word2Vec
#from sklearn.decomposition import PCA
#from nltk.tokenize import word_tokenize
#import nltk
#from nltk.corpus import stopwords
#import spacy
#import re
#from unidecode import unidecode
#from nltk.tokenize import word_tokenize
#from gensim.models import Word2Vec, Phrases

#st.markdown("# Facebook 🎈")
#st.sidebar.markdown("# Facebook 🎈")
st.set_page_config(
        page_title="OML Fraude Data Web Scraping",
        page_icon="🤳",
        layout="wide"
    )

def main_page():
    
    col1, col2, col3 = st.columns(3)
    image = Image.open("téléchargement.png")
    with col1 : 
        st.markdown(
        """
        <style>
            button[title^=Exit]+div [data-testid=stImage]{
                text-align: center;
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 50%;
                body {
                    color: Ivory;
                } </style>
        """, unsafe_allow_html=True)
        st.image(image, width=75)
    ###################### dashboard title
    with col2 : 
        st.markdown(
            f"""
            <h1 style='text-align: center; font-size: 25px; font-family: Arial; font-weight: bold;'>Data Fraud OML: <br> Web/Social Media scraping</h1>
            """, 
           unsafe_allow_html=True
        )
    st.markdown(
    """
    <style>
    /* CSS to change sidebar font color */
    .sidebar .sidebar-content {
        color: purple; /* Change 'purple' to the color you desire */
    }
    </style>
    """,
    unsafe_allow_html=True
)
    
    st.sidebar.success("")

    st.markdown(
        """
        <p style='color: Black and Neon Blue; font-size:20px;font-family: Arial; font-weight: bold'><strong> 👉 Web/Fraud Data OML Social media scraping.</strong></p>

       <p style='color: Black and Neon Blue; font-size:18px; font-weight: bold'> Ces résultats nous permettent d'avoir une idée d'une par sur le niveau d'attraction des internautes sur la fraude data et d'autre part, de comprendre, les techniques & outils utilisés pour baypasser nos système de facturation.
       <br> Cela pourrait aider à prendre des décision afin de réduire le volume trafic data frauduleux.</p>
        <p style='color: darq green; font-size:20px;font-family: Arial; font-weight: bold'><strong> 👉 Source des données :</strong> </p> 
        <h2 style='color: Black and Neon Blue; font-size:15px;font-weight: bold' '>Google, Facebook, Instagram, Twitter, Telegram.</h2> </p>
        <p style='color: Black and Neon Blue; font-size:18px; font-weight: bold'> Pour chacune des sources, il existe des packages Python ou APIs dédiés pour le scraping.
        Les données extraites sont compilées, nétoyées et analysées (à l'anonymat) à des fin de visualisation.</p>
        <p style='color: darq green; font-size:20px;font-family: Arial; font-weight: bold'><strong>👈 Select a page from the sidebar ! </strong> </p>
    """, unsafe_allow_html=True
    )


def page2():
    st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)

    # read csv from a github repo
    dataset_url = "https://raw.githubusercontent.com/elhdiagne3/FraudData_scraping/master/goups_post.csv"
    dataset_url2 = "https://raw.githubusercontent.com/elhdiagne3/FraudData_scraping/master/group.csv"
    # read csv from a URL
    @st.cache_data(ttl=60, persist="disk", show_spinner=False)
    def get_data() -> pd.DataFrame:
        return pd.read_csv(dataset_url, sep=';', encoding='utf-8', encoding_errors= 'ignore'), pd.read_csv(dataset_url2, sep=';', encoding='utf-8', encoding_errors= 'ignore')
    df, df1 = get_data()
    df.drop_duplicates('post_id', inplace = True)
    df = df[df.post_id!='613.339.656.815.365']
    df1.drop_duplicates('id', inplace = True)
    #df = data
    #def show() : 
    st.sidebar.header("")
    left_co, cent_co,last_co = st.columns(3)
    default_year = [2018, 2019,2020,2021]
    with cent_co:
        st.markdown(
        """
        <style>
            .multiselect label, .multiselect select {
                width: 100%;
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 15px;
                background-color: #f7f7f7;
                color: #333;
            }
        </style>
        """,
        unsafe_allow_html=True
        )
        source_filter = st.multiselect("Select the year of posts", pd.unique(df["year"]), default=default_year)
        #source_filter_ = st.multiselect("Select the post_type of posts", pd.unique(df["post_type"]), default=default_year)
        placeholder = st.empty()
        df = df[df.post_type == 'fraud_post']
        df = df[df["year"].isin(source_filter)]
        dfs = df['post_id'].groupby(df['year_mm']).count().reset_index()
        dfs['nb_post'] = dfs['post_id']
        df_ = df['likes'].groupby(df['year_mm']).sum().reset_index().sort_values('year_mm')
        df__ = df['comments'].groupby(df['year_mm']).sum().reset_index().sort_values('year_mm')
    # Fonction pour formater les grands nombres en K ou M
    def format_number(num):
        if num >= 1000000:  # Si le nombre est supérieur à 1 million
            return f"{num / 1_000_000:.1f} M"  # Convertir en millions et formater avec une décimale
        elif num >= 10000:  # Si le nombre est supérieur à 1 mille
            return f"{num / 1000:.1f} K"  # Convertir en milliers et formater avec une décimale
        else:
            return str(num)  # Garder le nombre inchangé s'il est plus petit

    for seconds in range(200):
        # creating KPIs
        nb_group = df1.id.count()
        nb_member = df1['members'].sum()
        nb_post = df["post_id"].count()
        nb_likes = int(df.likes.sum())
        nb_comments = df.comments.sum()
        nb_shares = df.shares.sum()
    with st.container():
            col1, col2, col3 = st.columns(3)
            kpi1, kpi2, kpi3, kpi4, kpi5, kpi6 = st.columns(6)

                    # Display the embellished label and kpi1.metric in col1
            with col1:
                with kpi1 : 
                    st.markdown(
                        "<div style='text-align: center; font-size: 18px; font-family: Arial; font-weight: bold; color: black;'>"
                        "nb group 👪</div>",
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        "<div style='text-align: center; font-size: 35px; font-family: Arial; font-weight: bold; color: green;'>"
                        f"{format_number(nb_group)}</div>",
                        unsafe_allow_html=True
                    )
                with kpi2 :
                    st.markdown(
                        "<div style='text-align: center; font-size: 18px; font-family: Arial; font-weight: bold; color: black;'>"
                        "nb members 🙌</div>",
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        "<div style='text-align: center; font-size: 35px; font-family: Arial; font-weight: bold; color: green;'>"
                        f"{format_number(nb_member)}</div>",
                        unsafe_allow_html=True
                    )
            with col2:
                with kpi3 :                
                    st.markdown(
                        "<div style='text-align: center; font-size: 18px; font-family: Arial; font-weight: bold; color: black;'>"
                        "nb posts ⏳</div>",
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        "<div style='text-align: center; font-size: 35px; font-family: Arial; font-weight: bold; color: green;'>"
                        f"{format_number(nb_post)}</div>",
                        unsafe_allow_html=True
                    )
                with kpi4:
                    st.markdown(
                            "<div style='text-align: center; font-size: 18px; font-family: Arial; font-weight: bold; color: black;'>"
                            "nb likes 👍</div>",
                            unsafe_allow_html=True
                        )
                    st.markdown(
                            "<div style='text-align: center; font-size: 35px; font-family: Arial; font-weight: bold; color: green;'>"
                            f"{format_number(nb_likes)}</div>",
                            unsafe_allow_html=True
                        )

            with col3:
                with kpi5 : 
                    st.markdown(
                            "<div style='text-align: center; font-size: 18px; font-family: Arial; font-weight: bold; color: black;'>"
                            "nb comments ✍️</div>",
                            unsafe_allow_html=True
                        )
                    st.markdown(
                            "<div style='text-align: center; font-size: 35px; font-family: Arial; font-weight: bold; color: green;'>"
                            f"{format_number(nb_comments)}</div>",
                            unsafe_allow_html=True
                        )

                with kpi6 : 
                    st.markdown(
                        "<div style='text-align: center; font-size: 18px; font-family: Arial; font-weight: bold; color: black;'>"
                        "nb shares 👋</div>",
                        unsafe_allow_html=True
                    )
                    st.markdown(
                        "<div style='text-align: center; font-size: 35px; font-family: Arial; font-weight: bold; color: green;'>"
                        f"{format_number(nb_shares)}</div>",
                        unsafe_allow_html=True
                    )
            fig_col1, fig_col2 = st.columns(2)
            with fig_col1:
                fig = px.line(dfs, x = 'year_mm', y = 'nb_post',markers = True,  line_shape="spline", render_mode="svg", 
                width=600, height=400)
                fig.update_layout(title_text='📈 : Evolution du nombre de posts par mois', title_x=0.4)
                st.write(fig)
            with fig_col2:
                fig = px.line(width=600, height=400,markers = True, render_mode="svg")
                fig.update_layout(title_text='📈 : Evolution du nombre de likes & de comments par mois', title_x=0.1)
                fig.add_scatter(x=df_['year_mm'], y=df_['likes'], mode='lines', line_shape="spline",marker= dict(color = 'blue'), name='nb_likes')
                fig.add_scatter(x=df__['year_mm'], y=df__['comments'], mode='lines', line_shape="spline", marker= dict(color = 'green'), name='nb_Comments')
                st.plotly_chart(fig) 
            col1, col2 = st.columns(2)
            with col1 :
                df1.sort_values('members',ascending=False, inplace=True)
                df1_ = df1[~df1.name.str.contains('MTN')].head(15)
                df1_.sort_values('members', ascending = False, inplace = True)
                fig = px.bar(df1_, x = 'name', y = 'members', 
                width=600, height=800)
                fig.update_layout(
                xaxis_title='Name groups',
                yaxis_title='Number of members',
                plot_bgcolor='white',  # Transparent plot background
                paper_bgcolor='rgb(255,255,255)',  # White background
                font=dict(family='Arial', size=12, color='black'),  # Font style
                margin=dict(l=50, r=50, t=50, b=50),  # Setting margins
                xaxis=dict(tickangle=45),  # Rotating x-axis labels
                yaxis=dict(tickformat=',d'),  # Adding comma to y-axis labels for thousands separator, 
                title = '📊 Graph III : Nb_members : Top 10 group',
                title_x = 0.4
            )
            st.write(fig)         
            from wordcloud import ImageColorGenerator
            from wordcloud import WordCloud
            with st.container() : 
                df['text'].fillna(".", inplace =True)
                text = str(df.text.tolist())
                def custom_tokenize(text):
                    # Remove accents using unidecode
                    text_no_accents = unidecode(text)
                    # Keep only alphabetic characters
                    words = re.findall(r'\b\w+\b', text_no_accents.lower())
                    return words
                text_ = custom_tokenize(text)
                text_ =' '.join(text_)
                #text_.encode('utf-16').decode('utf-16')
                cloud = WordCloud(font_path= 'font.ttf', width=1000, height=500,background_color='black',min_word_length =6, colormap = 'Oranges').generate(text_)
                #Plot the wordcloud
                #plt.figure(figsize=(15,10))
                #plt.text(0.5, 1.15, f"Word Cloud Fraud Data Post", size=24, ha='center', transform=plt.gca().transAxes
                st.markdown("""<p text-align: centerstyle='color: Black and Neon Blue; font-size:15px;font-family: Arial; font-weight: bold'>📚 WordCloud Data Fraud 2021-2023. </p>""", unsafe_allow_html = True) 
                st.image(cloud.to_array(), width=0, use_column_width=True,caption = "" )
def page3():
    st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)
    st.sidebar.header('')
    dataset_url = "https://raw.githubusercontent.com/elhdiagne3/FraudData_scraping/master/goog_process.csv"
    dataset_url2 = "https://raw.githubusercontent.com/elhdiagne3/FraudData_scraping/master/google_all.csv"
    # read csv from a URL
    @st.cache_data(ttl=60, persist="disk", show_spinner=False)
    def get_data() -> pd.DataFrame:
        return pd.read_csv(dataset_url, sep=',', encoding='utf-8', encoding_errors= 'ignore'), pd.read_csv(dataset_url2, sep=',', encoding='utf-8', encoding_errors= 'ignore')
    data, df = get_data()
    df = df[~df.Link.str.contains('orangemali.com')]
    nb_pages = df.drop_duplicates().shape[0]
    data = data[data.word != '...'].head(15)
    
    col1, col2, col3 = st.columns(3)
    with col2:
        st.markdown(
            "<div style='text-align: center; font-size: 18px; font-family: Arial; font-weight: bold; color: black;'>"
            "nb pages 👪</div>",
            unsafe_allow_html=True
        )
        st.markdown(
            "<div style='text-align: center; font-size: 35px; font-family: Arial; font-weight: bold; color: green;'>"
            f"{nb_pages}</div>",
            unsafe_allow_html=True
        )
    
    fig = px.bar(data, x = 'word', y = 'count', 
    width=1200, height=600 )
    fig.update_layout(
    xaxis_title='words',
    yaxis_title='Frequency of word',
    plot_bgcolor='white',  # Transparent plot background
    paper_bgcolor='rgb(250,250,250)',  # White background
    font=dict(family='Arial', size=12, color='black'),  # Font style
    margin=dict(l=50, r=50, t=50, b=50),  # Setting margins
    xaxis=dict(tickangle=45),  # Rotating x-axis labels
    yaxis=dict(tickformat=',d'),  # Adding comma to y-axis labels for thousands separator, 
    title = '📊 TOP 15 of words',
    title_x = 0.4
    ) 
    st.write(fig)
    def get_table_download_link_csv(df):
        csv = df.to_csv(index=False, encoding = 'utf_8')
        b64 = base64.b64encode(csv.encode()).decode()  # Encoding the CSV file
        href = f'<a href="data:file/csv;base64,{b64}" download="data.csv">Download Table (CSV) File</a>'
        return href
    # Option to download the DataFrame as a CSV file
    st.markdown(f"""<p style='text-align: center; color: Black and Neon Blue; font-size:30px;font-family: Arial; font-weight: bold'>{get_table_download_link_csv(df)}''</p>""", unsafe_allow_html=True)
    get_table_download_link_csv(df)
                
def page4():
    st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)
    st.sidebar.header('')
def page5():
    st.markdown("""<style>
        .sidebar .sidebar-content {
            font-family: 'Arial', sans-serif;
            font-size: 25px;
            font-weight: bold;
        }
    </style>""", unsafe_allow_html=True)
    st.sidebar.header('')
        # read csv from a github repo
    dataset_url = "https://raw.githubusercontent.com/elhdiagne3/FraudData_scraping/main/goups_post.csv"
    dataset_url2 = "https://raw.githubusercontent.com/elhdiagne3/FraudData_scraping/main/group.csv"
    # read csv from a URL
    @st.cache_data(ttl=60, persist="disk", show_spinner=False)
    
    def get_data() -> pd.DataFrame:
        return pd.read_csv(dataset_url, sep=',', encoding='utf-8', encoding_errors= 'ignore'), pd.read_csv(dataset_url2, sep=',', encoding='utf-8', encoding_errors= 'ignore')
    df, df1 = get_data()
    def get_table_download_link_csv(df):
        csv = df.to_csv(index=False, encoding = 'utf_8')
        b64 = base64.b64encode(csv.encode()).decode()  # Encoding the CSV file
        href = f'<a href="data:file/csv;base64,{b64}" download="data.csv">Download Table (CSV) File</a>'
        return href
    st.title('DataTable with Download Option to CSV')
    # Display DataTable
    df = df.drop('header', axis = 1)
    st.dataframe(df[df.post_type == 'fraud_post'].sample(15))
    st.dataframe(df1.sample(15))
    # Option to download the DataFrame as a CSV file 
    st.markdown(f"""<p style='text-align: center; color: Black and Neon Blue; font-size:15px;font-family: Arial; font-weight: bold >{get_table_download_link_csv(df)}""", unsafe_allow_html=True)
        
    time.sleep(1)
page_names_to_funcs = {
    "Home": main_page,
    "Google": page3,
    "Facebook": page2,
    "Kibaru": page4,
    "DataTable": page5,
}
# Streamlit sidebar with icons, font, and bold text
st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            font-family: 'Arial', sans-serif;
            font-size: 25px;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("🌟 Navigation")

# Customize the appearance of the radio buttons with icons
selected_page = st.sidebar.radio(
    "",
    list(page_names_to_funcs.keys()),
    format_func=lambda page: f"{page} {'🏠' if page == 'Home' else '🔍' if page == 'Google' else '📘' if page == 'Facebook' else '📊' if page == 'DataTable' else '⚙️'}",
)

# Call the selected page function
page_names_to_funcs[selected_page]()


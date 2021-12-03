import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network

# set header title
def app():

    st.markdown("### Product Category: Electronics")
    # query = st.text_input("Enter a custom query")

    # if not query:
    #     st.warning("Please enter a custom query")
    # else:
    #     st.write("Your query is: ", query)

    # uncomment this to show the graph 
    #HtmlFile = open('nodes.html','r',encoding='utf-8')
    #source_code = HtmlFile.read()
    #components.html(source_code, height = 1200, width = 1200)

    df = pd.read_excel("cluster.xlsx")
    #df = df.loc[:10]
    #st.table(df.sort_values("helpful_votes", ascending = False).sort_values("star_rating", ascending = False))
    #cols = ["product_title", "helpful_votes", "star_rating"]
    drop_cols = ["Sentiment", "total_votes", "keyword_value", "attention", "label"]
    df = df.drop(columns = drop_cols)
    #st_ms = st.multiselect("Columns", df.columns.tolist(), default=cols)
    # slider to filter by price 
    #values = st.sidebar.slider("Price range", float(df.price.min()), 1000., (50., 300.))
    st.dataframe(df.head(15).sort_values("helpful_votes", ascending = False).sort_values("star_rating", ascending = False))


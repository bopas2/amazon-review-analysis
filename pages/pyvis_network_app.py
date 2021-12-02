import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network

# set header title
def app():

    query = st.text_input("Enter a custom query")

    if not query:
        st.warning("Please enter a custom query")

#HtmlFile = open('nodes.html','r',encoding='utf-8')
#source_code = HtmlFile.read()
#components.html(source_code, height = 1200, width = 1000)
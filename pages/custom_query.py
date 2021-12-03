import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
from pages import make_network

# set header title
def app():

    st.markdown("### Input a Custom Query")
    st.markdown("What kind of mobile electronic product are you interested in?")
    
    query = st.text_input("Enter a custom query")

    if not query:
        st.warning("Please enter a custom query")
    else:
        st.write("Your query is: ", query)
        make_network.make_network(query)

        HtmlFile = open('nodes.html','r',encoding='utf-8')
        source_code = HtmlFile.read()
        components.html(source_code, height = 1200, width = 1200)

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
import pickle
from pyvis.network import Network
from pages import make_network

from transformers import DistilBertTokenizerFast
from transformers import TFDistilBertForSequenceClassification

# set header title
def app():

    ## load models 
    # pre-trained attention model should be saved in a folder name sentiment
    # pre-trained clustering model should be saved as a file named k_means_model.pickle
    attention_model = TFDistilBertForSequenceClassification.from_pretrained("./pages/sentiment/", output_attentions=True)
    tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')
    clustering_model = pickle.load(open('./pages/k_means_model.pickle', 'rb'))

    st.markdown("### Input a Custom Query")
    st.markdown("What kind of mobile electronic product are you interested in?")
    
    query = st.text_input("Enter a custom query")

    if not query:
        st.warning("Please enter a custom query")
    else:
        st.write("Your query is: ", query)
        df = make_network.make_network(query, tokenizer, attention_model, clustering_model)

        HtmlFile = open('nodes.html','r',encoding='utf-8')
        source_code = HtmlFile.read()
        components.html(source_code, height = 1000, width = 1200)
        st.dataframe(df.head(100).sort_values("rating", ascending = False))
        #st.dataframe(df.head(15).sort_values("helpful_votes", ascending = False).sort_values("star_rating", ascending = False))


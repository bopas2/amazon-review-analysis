import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
from pages import AmazonViz

<<<<<<< HEAD
def make_network(query, tokenizer, attention_model, clustering_model):
    df = AmazonViz.create(query, tokenizer, attention_model, clustering_model)
    return df
=======
def make_network(query = None):
    df = AmazonViz.create(query)

    return df
>>>>>>> 9ca6a1dea3d7cf53ecbabdc9f705069e5f9c3f03

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
from pages import AmazonViz

def make_network(query, tokenizer, attention_model, clustering_model):
    df = AmazonViz.create(query, tokenizer, attention_model, clustering_model)
    return df

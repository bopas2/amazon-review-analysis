from transformers import DistilBertTokenizerFast
from transformers import TFDistilBertForSequenceClassification
from pyvis.network import Network
import pandas as pd
import numpy as np
import pickle

def create(query, tokenizer, attention_model, clustering_model):

    ## gets the attention value associated with an input
    def get_attention_value(input, attention_model):
        predict_input = tokenizer.encode(input, truncation=True, padding=True, return_tensors="tf")
        outputs = attention_model.predict(predict_input)
        attention_vectors = []
        for layer in outputs.attentions:
            X = layer.flatten()
            attention_vectors.append(X)
        attention_vectors = np.array(attention_vectors)
        attention_vectors = np.mean(attention_vectors)
        return attention_vectors

    ## gets the cluster associated with a user input
    def cluster_finder(query, tokenizer, attention_model, clustering_model):
        attention_value = [get_attention_value(query, attention_model)]
        embeded_keyword = tokenizer([query], truncation=True, padding=True)['input_ids'][0]
        pre_input = attention_value + embeded_keyword
        padding = [0] * (10 - len(pre_input)) # model requires additional padding by the way it was trained
        clustering_input = [pre_input + padding]
        return clustering_model.predict(clustering_input)[0]

    df = pd.read_excel("cluster.xlsx")
    df = df.loc[df['label'] == cluster_finder(query, tokenizer, attention_model, clustering_model)]
    df = df.applymap(str)
    df = df.sample(n=100)
    titles = list(df['product_title'])
    net = Network(height = '800px', width = '100%')

    net.add_node(1, label=query)#, value='hi')#, shape='circle')

    for i in range(2, 2 + len(df)):
        cur = df.iloc[i - 2]
        if int(float(cur['Sentiment'])) == 0:
            senti = "Negative Review"
        else:
            senti = "Positive Review"
        if int(float(cur['Sentiment'])):
            net.add_node(i, label=df.iloc[i - 2]['keyword'],
                        title=senti + "<br>" + "Product: " + str(df.iloc[i - 2]['product_title']) + '<br>' + "Rating:" + str(
                            df.iloc[i - 2]['rating']), size=int(float(cur['rating'])) * 5)
        else:
            net.add_node(i, label=df.iloc[i - 2]['keyword'],
                        title=senti + "<br>" + "Product: " + str(df.iloc[i - 2]['product_title']) + '<br>' + "Rating:" + str(
                            df.iloc[i - 2]['rating']), color="#FF0000", size=int(float(cur['rating'])) * 5)

    for i in range(2, 2 + len(df)):
        net.add_edge(1, i)

    net.hrepulsion(node_distance=100, spring_length=200)
    #net.show_buttons(filter_=['nodes'])
    # net.show('nodes.html')

    return df
    #got_net = Network(height='750px', width='100%', bgcolor='#222222', font_color='white')

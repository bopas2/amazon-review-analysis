from pyvis.network import Network
import pandas as pd

def create(query = None):
    
    def cluster_finder(query):
        # TODO - Currently hardcoded
        return 137

    df = pd.read_excel("cluster.xlsx")
    df = df.loc[df['label'] == cluster_finder(query)]
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
    net.show('nodes.html')

    return df
    #got_net = Network(height='750px', width='100%', bgcolor='#222222', font_color='white')

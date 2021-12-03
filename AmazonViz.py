from pyvis.network import Network
import pandas as pd


df = pd.read_excel("cluster.xlsx")

titles = list(df['product_title'])
net = Network()
clusters = set(list(df['label']))
#print([x for x in range(1, len(titles) + 1)])
net.add_nodes([x for x in range(1, len(titles) + 1)], label=titles)
net.add_nodes([x for x in range(len(titles) + 1, len(titles) + len(clusters) + 1)])
#net.add_node(1, label='Alex')
#net.add_node(2, label='Cathy')

#Adding list of nodes
#net.add_nodes([1, 2], label=['Alex', 'Carthy'])

#net.add_nodes([3, 4, 5, 6],
#              label=['Michael', 'Ben', 'Oliver', 'Olivia'],
#              color=['#3da831', '#9a31a8', '#3155a8', '#eb4034'])
#for c in clusters:
#1 + len(titles) -> 534 + len(titles)
for i in range(len(df)):
    net.add_edge(i + 1, int(df.iloc[i]['label']) + 1 + len(titles))

#net.add_edge(1, 5)
#net.add_edges([(2, 5), (3, 4), (1, 6), (2, 6), (3, 5)])
#(Source, Target, Weight)
#net.add_edges([(2, 5, 5), (3, 4, 2), (1, 6), (2, 6), (3, 5)])
#net.show_buttons(filter_=True)
#net.show_buttons(filter_=['physics'])
#net.repulsion(node_distance=100, spring_length=200)
net.show('nodes.html')
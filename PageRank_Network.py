
import streamlit as st
import pandas as pd
import networkx as nx
import scipy
import matplotlib.pyplot as plt


df = pd.read_csv("Dynamic_PPIN.txt", sep=",", names=["column1", "column2", "time", "weight"])
print(df)

# unweighted Graph creation
G = nx.Graph()
G = nx.from_pandas_edgelist(df, "column1", "column2")


weights = [i * 5 for i in df['weight'].tolist()]
pos = nx.spring_layout(G, k=0.9)
nx.draw_networkx_edges(G, pos, edge_color='#06D6A0', arrowsize=22, width=weights)
nx.draw_networkx_nodes(G, pos,node_color='#EF476F', node_size=100)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', font_color='black')
plt.gca().margins(0.1, 0.1)
plt.show()

# weighted Graph
G_weighted = nx.from_pandas_edgelist(df, 'column1', 'column2', create_using=nx.DiGraph, edge_attr='weight')

#Basic pagerank for the undirected graph
pr = nx.pagerank(G)
print(pr)

df_pagerank_normal = pd.DataFrame.from_dict(pr, orient="index", columns=['Page Rank'])
df_pagerank_normal = df_pagerank_normal.sort_values(by=['Page Rank'], ascending = False)
print("Basic page rank list sorted ascending:")
print(df_pagerank_normal.sort_values(by=['Page Rank'], ascending = False))
df_pagerank_normal_top = df_pagerank_normal.head()

#Personalized Page Rank for the undirected graph
pr_personalized = nx.pagerank(G, personalization={16 : 1, 130:1, 41 : 1, 124:1 })
print(pr_personalized)
df_pagerank_personalized = pd.DataFrame.from_dict(pr_personalized, orient="index", columns=['Page Rank'])

df_pagerank_personalized = df_pagerank_personalized.sort_values(by=['Page Rank'], ascending = False)
print("Personalized page rank list sorted ascending:")
print(df_pagerank_personalized.sort_values(by=['Page Rank'], ascending = False))
df_pagerank_personalized_top = df_pagerank_personalized.head()

#Visualization in Streamlit
st.title("""Personalized Page Rank PPIN_HAZBUN""")
st.write("""PPIN_HAZBUN data set:""")
st.dataframe(df)
st.write("""Pagerank network regular""")
st.dataframe(df_pagerank_normal)
st.dataframe(df_pagerank_normal_top)
st.write("""Pagerank network personalized""")
st.dataframe(df_pagerank_personalized)
st.dataframe(df_pagerank_personalized_top)

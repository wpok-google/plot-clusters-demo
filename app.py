import streamlit as st
import numpy as np
import plotly.figure_factory as ff
import pandas as pd
import plotly.express as px

# Load data
clusters_df = pd.read_csv('data/clusters.csv', index_col=[0])








fig = px.scatter(clusters_df.reset_index(), x="x0", y="x1",
                 color="label_name", custom_data=['index'], width=1000, height=800)

fig.update_traces(
    hovertemplate="<br>".join([
        "%{customdata[0]}",
    ])
)


# Plot!
st.plotly_chart(fig, use_container_width=True)

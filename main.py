import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def load_data():
    q=pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
    q=q.drop(q.columns[[0,1,17,18,19,20,21,22,23,24,33,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]],axis=1)
    return q
a=st.sidebar.selectbox(
    "Which one would you prefer?",
    ("Specific","Comparison")
)

if a=="Specific":
    q=load_data()
    t=st.selectbox('Select country/region',q['location'].unique())
    w=q[q['location']==t]
    p=st.selectbox('select',q.columns[2:])
    fig = px.line(w, x='date', y=p, title='Covid 19')
    st.plotly_chart(fig)
else:
    fig=go.Figure()
    q=load_data()
    
    t=st.selectbox('Select country/region',q['location'].unique())
    w=q[q['location']==t]
    t1=st.selectbox('Select country/region',q['location'].unique(),key=123)
    w1=q[q['location']==t1]
    p=st.selectbox('select',q.columns[2:])

    df={"a":w,"b":w1}
    
    for i in df:
        fig = fig.add_trace(go.Scatter(x =df[i]['date'],y = df[i][p]))
    fig.update_layout(
    title_text="Covid Comparison")
    fig.update_xaxes(title_text="Date")
    fig.update_yaxes(title_text=p)
    st.plotly_chart(fig)

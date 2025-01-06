import streamlit as st
import matplotlib.pyplot as plt

# Visualize Data in Streamlit
def visualize_data(data):
    st.write(data)
    st.line_chart(data.set_index(data.columns[0]))

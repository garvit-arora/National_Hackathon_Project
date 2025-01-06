import streamlit as st
from data_processor import process_real_time_data
from rag_pipeline import get_personalized_recommendations
from utils import visualize_data

# Streamlit Configuration
st.set_page_config(page_title="Real-Time Health Advisory System", layout="wide")

# App Title
st.title("🏃‍♂️ Real-Time Personalized Health Advisory System")
st.write("Empowering proactive health decisions with real-time insights.")

# Data Ingestion
st.sidebar.header("🔗 Data Sources")
data_sources = st.sidebar.multiselect(
    "Select Data Sources",
    options=["Wearable Devices", "Fitness Apps", "External APIs"],
    default=["Wearable Devices", "External APIs"]
)

# Real-Time Simulation
st.sidebar.header("⚙️ Controls")
refresh_rate = st.sidebar.slider("Data Refresh Rate (seconds)", min_value=2, max_value=10, value=5)

# Placeholder for Dynamic Content
data_placeholder = st.empty()

# Main Loop for Real-Time Updates
if st.sidebar.button("Start System"):
    st.success("System is running...")
    while True:
        # Real-Time Data Processing
        data = process_real_time_data(data_sources)
        recommendations = get_personalized_recommendations(data)
        
        # Update Dashboard
        with data_placeholder.container():
            st.subheader("📊 Health Metrics")
            visualize_data(data)
            
            st.subheader("💡 Recommendations")
            for rec in recommendations:
                st.write(f"- {rec}")
        
        st.write("---")
        st.sidebar.write("Last Updated: ", st.sidebar.markdown(f"**{st.time()}**"))
        st.sidebar.write("---")
        st.time.sleep(refresh_rate)

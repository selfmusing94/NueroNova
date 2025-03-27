import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="ForestGuardian 🌳",
    page_icon="🌳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'Dashboard'

# Custom CSS
st.markdown("""
<style>
    /* Sidebar styling */
    .stButton > button {
        width: 100%;
        text-align: left;
        padding: 0.75rem 1rem;
        background-color: transparent;
        color: #2C3E50;
        border: none;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
    }
    .stButton > button:hover {
        background-color: rgba(46, 204, 113, 0.1);
        color: #2ECC71;
    }
    .user-info {
        padding: 1rem;
        background: linear-gradient(135deg, rgba(46, 204, 113, 0.1), rgba(46, 204, 113, 0.05));
        border-radius: 10px;
        margin-top: 2rem;
    }
    /* Dashboard styling */
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    # Logo and Title
    st.markdown("""
        <div style='text-align: center; padding: 1rem;'>
            <h1 style='color: #2ECC71; font-size: 1.8rem;'>🌳 ForestGuardian</h1>
            <p style='color: #666;'>Forest Monitoring System</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    if st.button("🏠 Dashboard"):
        st.session_state.page = 'Dashboard'
    if st.button("📤 Upload"):
        st.session_state.page = 'Upload'
    if st.button("📊 Analysis"):
        st.session_state.page = 'Analysis'
    if st.button("⏱️ Time-Lapse"):
        st.session_state.page = 'Time-Lapse'
    if st.button("📑 Reports"):
        st.session_state.page = 'Reports'
    
    # Theme Toggle
    theme = st.toggle("🌙 Dark Mode", False)
    
    # User Info with your specified format
    st.markdown(f"""
        <div class='user-info'>
            <h4 style='margin:0; color: #2C3E50;'>👤 selfmusing94</h4>
            <p style='margin:0; color: #666; font-size: 0.9rem;'>🕒 2025-03-27 09:07:04 UTC</p>
        </div>
    """, unsafe_allow_html=True)

# Main Content
def show_dashboard():
    st.title("Forest Monitoring Dashboard")
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Forest Coverage", "68%", "-2.3%")
    with col2:
        st.metric("Areas Monitored", "1,234 km²", "+150 km²")
    with col3:
        st.metric("Alert Accuracy", "95%", "+0.8%")
    with col4:
        st.metric("Risk Areas", "23", "+5")
    
    # Charts
    st.subheader("Analysis")
    col1, col2 = st.columns(2)
    
    with col1:
        # Deforestation Trend
        dates = pd.date_range(start='2024-01-01', end='2025-03-27', freq='M')
        values = np.random.normal(100, 10, len(dates))
        df = pd.DataFrame({'Date': dates, 'Deforestation (ha)': values})
        
        fig = px.line(df, x='Date', y='Deforestation (ha)',
                     title='Deforestation Trend Analysis')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Cause Distribution
        causes = ['Agriculture', 'Urban Development', 'Logging', 'Natural']
        values = [40, 25, 20, 15]
        
        fig = px.pie(values=values, names=causes, title='Causes of Deforestation')
        st.plotly_chart(fig, use_container_width=True)
    
    # Recent Alerts
    st.subheader("Recent Alerts")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.error("🚨 High Risk Alert\n\nLarge deforestation detected")
    with col2:
        st.warning("⚠️ Medium Risk Alert\n\nUnusual activity detected")
    with col3:
        st.success("✅ Low Risk Alert\n\nSmall changes detected")

def show_upload():
    st.title("Upload Satellite Image")
    uploaded_file = st.file_uploader("Choose a satellite image", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_file is not None:
        # Create columns for before/after images
        col1, col2 = st.columns(2)
        
        # Display original image
        with col1:
            st.subheader("Original Image")
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_container_width=True)
        
        # Add analyze button
        if st.button("Analyze Image"):
            with col2:
                st.subheader("Analysis Results")
                st.info("Processing image... (Model integration pending)")
                # Here you would add your model processing code
                # For now, just displaying the original image
                st.image(image, caption='Processed Image', use_container_width=True)

# Page Router
if st.session_state.page == 'Dashboard':
    show_dashboard()
elif st.session_state.page == 'Upload':
    show_upload()
elif st.session_state.page == 'Analysis':
    st.title("Analysis")
    st.info("Analysis tools coming soon...")
elif st.session_state.page == 'Time-Lapse':
    st.title("Time-Lapse View")
    st.info("Time-lapse feature coming soon...")
elif st.session_state.page == 'Reports':
    st.title("Reports")
    st.info("Reporting tools coming soon...")
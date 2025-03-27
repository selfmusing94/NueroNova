import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time

# Page configuration
st.set_page_config(
    page_title="ForestGuardian 🌳",
    page_icon="🌳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2ECC71;
        text-align: center;
        padding: 1rem 0;
        animation: fadeIn 0.8s ease-in;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    .metric-card:hover {
        transform: translateY(-5px);
    }
    .sidebar-header {
        padding: 1rem;
        text-align: center;
    }
    .user-info {
        padding: 1rem;
        background: rgba(46, 204, 113, 0.1);
        border-radius: 10px;
        margin-top: 2rem;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
        <div class='sidebar-header'>
            <h1>🌳 ForestGuardian</h1>
            <p>Forest Monitoring System</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    selected = st.radio(
        "Navigation",
        ["Dashboard", "Upload", "Analysis", "Time-Lapse", "Reports"],
        index=0
    )
    
    # Theme Toggle
    theme = st.toggle("🌙 Dark Mode", False)
    
    # User Info
    current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    st.markdown(f"""
        <div class='user-info'>
            <h4>👤 selfmusing94</h4>
            <p>🕒 {current_time} UTC</p>
        </div>
    """, unsafe_allow_html=True)

# Main Content
def main_dashboard():
    # Header
    st.markdown("<h1 class='main-header'>Forest Monitoring Dashboard</h1>", unsafe_allow_html=True)
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Forest Coverage",
            value="68%",
            delta="-2.3%"
        )
    
    with col2:
        st.metric(
            label="Areas Monitored",
            value="1,234 km²",
            delta="+150 km²"
        )
    
    with col3:
        st.metric(
            label="Alert Accuracy",
            value="95%",
            delta="+0.8%"
        )
    
    with col4:
        st.metric(
            label="Risk Areas",
            value="23",
            delta="+5",
            delta_color="inverse"
        )
    
    # Charts
    st.markdown("### Analysis")
    tab1, tab2 = st.tabs(["📈 Trends", "🗺️ Map View"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            # Deforestation Trend
            dates = pd.date_range(start='2024-01-01', end='2025-03-27', freq='M')
            values = np.random.normal(100, 10, len(dates))
            df = pd.DataFrame({'Date': dates, 'Deforestation (ha)': values})
            
            fig = px.line(
                df, 
                x='Date', 
                y='Deforestation (ha)',
                title='Deforestation Trend Analysis'
            )
            fig.update_layout(
                template='plotly_white',
                plot_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Cause Distribution
            causes = ['Agriculture', 'Urban Development', 'Logging', 'Natural']
            values = [40, 25, 20, 15]
            
            fig = go.Figure(data=[go.Pie(
                labels=causes,
                values=values,
                hole=.3,
                marker_colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
            )])
            fig.update_layout(
                title='Causes of Deforestation',
                template='plotly_white'
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.info("Interactive map visualization coming soon...")
    
    # Recent Alerts
    st.markdown("### Recent Alerts")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.error("🚨 High Risk Alert\n\nLarge deforestation detected in Amazon region")
    
    with col2:
        st.warning("⚠️ Medium Risk Alert\n\nUnusual activity detected in protected area")
    
    with col3:
        st.success("✅ Low Risk Alert\n\nSmall changes detected in monitoring zone")

if selected == "Dashboard":
    main_dashboard()
elif selected == "Upload":
    st.header("Upload Satellite Image")
    uploaded_file = st.file_uploader("Choose a satellite image", type=['png', 'jpg', 'jpeg'])
    if uploaded_file:
        st.image(uploaded_file, caption='Uploaded Image')
elif selected == "Analysis":
    st.header("Analysis")
    st.info("Analysis tools coming soon...")
elif selected == "Time-Lapse":
    st.header("Time-Lapse View")
    st.info("Time-lapse feature coming soon...")
elif selected == "Reports":
    st.header("Reports")
    st.info("Reporting tools coming soon...")

# Footer
st.markdown("---")
st.markdown("ForestGuardian Dashboard v1.0 | Last updated: " + current_time)
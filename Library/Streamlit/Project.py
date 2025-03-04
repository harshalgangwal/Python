import streamlit as st
import cv2
import torch
import numpy as np
import tempfile
import os
import pickle
import pandas as pd
import datetime
from utils.video_processing import process_video
from utils.time_series import forecast_crowd

# Load YOLO model
yolo_model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolo11n.pt')

# Load forecasting models
with open('models/sarimax_model.pkl', 'rb') as f:
    sarimax_model = pickle.load(f)
with open('models/prophet_model.pkl', 'rb') as f:
    prophet_model = pickle.load(f)

# Streamlit App
st.title("🚆 Metro Mitra: Smart Crowd Management")

# Sidebar Navigation
menu = ["Home", "Upload Video", "Forecast Crowds", "Visualizations", "About"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.image("static/images/metro_banner.jpg", use_column_width=True)
    st.markdown("## Welcome to Metro Mitra!")
    st.markdown(
        "This system uses **YOLO for real-time crowd detection** and **FB Prophet & SARIMAX for forecasting** metro station crowd levels.")
    st.markdown("### Features:")
    st.markdown(
        "- 📹 **Live Video Processing** for crowd detection\n- 📈 **Time Series Forecasting** to predict congestion\n- 📊 **Visualizations & Analytics**\n- 🌐 **Scalable & Real-Time Deployment**")

elif choice == "Upload Video":
    st.header("📹 Upload a Video for Crowd Detection")
    uploaded_file = st.file_uploader("Choose a video...", type=["mp4", "avi", "mov"])

    if uploaded_file is not None:
        temp_video = tempfile.NamedTemporaryFile(delete=False)
        temp_video.write(uploaded_file.read())
        st.video(temp_video.name)

        with st.spinner("Processing Video..."):
            result_video = process_video(temp_video.name, yolo_model)

        st.success("Processing Complete!")
        st.download_button("Download Processed Video", result_video, file_name="processed_video.mp4")

elif choice == "Forecast Crowds":
    st.header("📈 Forecast Metro Station Crowds")
    station = st.selectbox("Select Metro Station", ["Station A", "Station B", "Station C"])

    if st.button("Predict Crowd Levels"):
        with st.spinner("Generating Forecast..."):
            forecast_df = forecast_crowd(station, prophet_model, sarimax_model)

        st.write("### Forecast Results:")
        st.dataframe(forecast_df)
        st.line_chart(forecast_df.set_index("Date"))

elif choice == "Visualizations":
    st.header("📊 Data Visualizations")
    st.write("Here you can explore historical trends and model predictions.")
    st.image("static/images/sample_graph.png")

elif choice == "About":
    st.header("ℹ️ About Metro Mitra")
    st.markdown(
        "Metro Mitra is a smart crowd management system designed to **predict and manage metro station congestion** using state-of-the-art AI techniques.")
    st.markdown("**Developed by:** Harish Laganwal 🚀")

st.sidebar.markdown("---")
st.sidebar.text("📍 Built with Streamlit & AI")
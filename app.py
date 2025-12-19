import streamlit as st
import numpy as np

st.set_page_config(page_title="Self Driving Car Simulator", layout="centered")

st.title("🚗 Self-Driving Car Simulator")
st.write("Simulated decision system for a self-driving car")

st.sidebar.header("Sensor Inputs")

distance_front = st.sidebar.slider("Distance to Front Object (meters)", 0, 100, 50)
lane_position = st.sidebar.slider("Lane Position (-1 = left, 0 = center, 1 = right)", -1.0, 1.0, 0.0)
speed = st.sidebar.slider("Current Speed (km/h)", 0, 150, 60)

def predict_action(distance, lane, speed):
    if distance < 20:
        return "🛑 Brake"
    elif lane < -0.5:
        return "➡️ Steer Right"
    elif lane > 0.5:
        return "⬅️ Steer Left"
    elif speed < 40:
        return "⬆️ Accelerate"
    else:
        return "✅ Maintain Speed"

action = predict_action(distance_front, lane_position, speed)

st.subheader("Car Decision")
st.success(action)

st.markdown("---")
st.write("### Input Summary")
st.write(f"- Distance Ahead: {distance_front} m")
st.write(f"- Lane Position: {lane_position}")
st.write(f"- Speed: {speed} km/h")

st.info("This is a demo logic. You can integrate a CNN or Reinforcement Learning model for real self-driving systems.")

import cv2
import numpy as np
import streamlit as st
from PIL import Image

def detect_lanes(image):
    # 1. Convert to Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # 2. Gaussian Blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # 3. Canny Edge Detection
    canny = cv2.Canny(blur, 50, 150)
    
    # 4. Define Region of Interest (ROI) - a triangle/trapezoid for the lane
    height, width = canny.shape
    mask = np.zeros_like(canny)
    polygon = np.array([[
        (0, height), 
        (width // 2, height // 2 + 50), 
        (width, height)
    ]], np.int32)
    cv2.fillPoly(mask, polygon, 255)
    masked_image = cv2.bitwise_and(canny, mask)
    
    return canny, masked_image

# --- Streamlit UI ---
st.set_page_config(page_title="Self-Driving Perception Lab", layout="wide")
st.title("🚜 Autonomous Vehicle: Lane Detection Dashboard")

uploaded_file = st.file_uploader("Upload a road image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Load image
    img = Image.open(uploaded_file)
    img_array = np.array(img)
    
    # Process image
    canny_edges, roi_edges = detect_lanes(img_array)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.header("Original")
        st.image(img, use_container_width=True)
        
    with col2:
        st.header("Canny Edges")
        st.image(canny_edges, use_container_width=True, clamp=True)
        
    with col3:
        st.header("Region of Interest")
        st.image(roi_edges, use_container_width=True, clamp=True)
        
    st.success("Perception analysis complete!")
else:
    st.info("Please upload an image of a road to start the lane detection simulation.")

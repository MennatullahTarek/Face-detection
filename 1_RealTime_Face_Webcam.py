import cv2
import streamlit as st
import numpy as np

# Streamlit app title
st.title('Video Stream Processing')

# Initialize OpenCV video capture (use your video source, e.g., a camera or video file)
cap = cv2.VideoCapture(0)  # Replace with your video source if necessary

# Check if the camera or video source is opened correctly
if not cap.isOpened():
    st.error("Error: Could not open video source.")
else:
    st.text("Press 'q' to exit the video stream.")

    # Run the video stream loop
    while True:
        ret, frame = cap.read()

        if not ret:
            st.error("Failed to grab frame.")
            break
        
        # Perform image processing here (if needed, e.g., grayscale, edge detection)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Convert the frame to RGB (Streamlit expects RGB format)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Display the processed frame as an image in Streamlit
        st.image(frame_rgb, channels="RGB", use_column_width=True)

        # Display the grayscale frame (optional)
        # st.image(gray_frame, caption="Grayscale", channels="GRAY", use_column_width=True)

        # Allow breaking the loop with a key press (but Streamlit runs in a web server, so this won't be typical for Streamlit)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture when done
    cap.release()

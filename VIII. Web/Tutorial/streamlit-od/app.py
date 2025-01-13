import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import cv2
import numpy as np
import torch
import timm
import yolov5

# Define a function to check if the link has a video and get the thumbnail
def get_video_thumbnail(link):
    if 'youtube.com' in link:
        video_id = link.split('v=')[-1]
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/0.jpg"
        return thumbnail_url
    elif 'twitter.com' in link or 'telegram.org' in link:
        # Placeholder for actual implementation
        st.error("Twitter and Telegram video extraction is not implemented yet.")
        return None
    else:
        st.error("Unsupported link.")
        return None

# Load YOLO model
def load_yolo_model():
    model = yolov5.load('yolov5s')
    return model

# Load TIMM model
def load_timm_model():
    model = timm.create_model('resnet50', pretrained=True)
    return model

# Perform object detection
def perform_detection(model, image):
    if isinstance(model, yolov5.models.yolo.Model):
        results = model(image)
        return results
    else:
        # Placeholder for TIMM-based detection
        st.error("Detection with TIMM model is not implemented.")
        return None

st.title('Video Link Object Detection App')

# User input for the link
link = st.text_input('Enter YouTube, Twitter, or Telegram link:')

if link:
    thumbnail_url = get_video_thumbnail(link)
    if thumbnail_url:
        response = requests.get(thumbnail_url)
        image = Image.open(BytesIO(response.content))
        st.image(image, caption='Video Thumbnail')

        # Select model for object detection
        model_choice = st.selectbox('Select object detection model:', ('YOLO', 'TIMM'))

        # Load the selected model
        if model_choice == 'YOLO':
            model = load_yolo_model()
        else:
            model = load_timm_model()

        # Start button for processing
        if st.button('Start Detection'):
            image_cv2 = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            results = perform_detection(model, image_cv2)

            # Display results if detection was successful
            if results:
                # Assuming results.save() saves images to a directory and we display them
                st.image(results.imgs[0], caption='Detected Image')
                st.image(image, caption='Original Image')

                # Provide download buttons for the images
                st.download_button('Download Original Image', data=BytesIO(response.content), file_name='original_image.jpg')
                st.download_button('Download Detected Image', data=BytesIO(results.imgs[0]), file_name='detected_image.jpg')

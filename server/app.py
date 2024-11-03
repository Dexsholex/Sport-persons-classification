import streamlit as st
import numpy as np
import cv2
from util import classify_image, load_saved_artifacts
import base64

# Load saved artifacts (model, class dictionaries)
load_saved_artifacts()

# App title
st.title("Sports Personality Classifier")
st.write("Upload an image of a sports personality to predict who it is!")

# Display default example images of each sports personality
ronaldo_img = './images/ronaldo.jpg'
ali_img = './images/muhammad_ali.jpg'
lebron_img = './images/lebron_james.jpg'
bolt_img = './images/usain_bolt.jpg'
serena_img = './images/serena_williams.jpg'
st.image([ronaldo_img, ali_img, lebron_img, bolt_img, serena_img], width=100, caption=[
         'Ronaldo', 'Muhammad Ali', 'LeBron James', 'Usain Bolt', 'Serena Williams'])

# Upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    img_path = 'uploaded_image.jpg'
    with open(img_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())

    # Display the uploaded image
    st.image(img_path, caption='Uploaded Image', use_column_width=True)

    # Convert the uploaded image to base64 format for classification
    with open(img_path, "rb") as image_file:
        image_base64_data = base64.b64encode(image_file.read()).decode()

    # Classify the uploaded image using your model
    results = classify_image(image_base64_data, img_path)

    # Display classification results
    if results:
        for result in results:
            st.write(f"The image is classified as: **{result['class']}**")
            st.write("**Prediction Probabilities (%):**")

            # Create a dictionary for probabilities
            prob_table = {label: f"{prob:.2f}%" for label, prob in zip(result['class_dictionary'].keys(), result['class_probability'])}

            # Display the probabilities in a table
            st.table(prob_table)
    else:
        st.write("Could not detect face with two eyes in the image. Try another image.")

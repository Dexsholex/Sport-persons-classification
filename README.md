# Sport Personality Image Classification Model
## Overview
This project is a machine learning-based image classification model that identifies famous sports personalities from images. The model focuses on five iconic figures: Ronaldo, Muhammad Ali, Usain Bolt, LeBron James, and Serena Williams. By leveraging facial recognition techniques and machine learning algorithms, this project enables users to upload an image and receive real-time predictions on which sports personality the image matches.

## Features
- Facial Detection: Utilizes OpenCV (CV2) and PyWavelet for facial feature extraction, focusing on detecting and cropping faces for optimal accuracy.
- Multiple Classification Models: Implemented three machine learning algorithms:
  - Support Vector Machine (SVM) – 80% accuracy
  - Logistic Regression – 76% accuracy
  - Random Forest – 66% accuracy
- Interactive UI: Integrated with a user-friendly Streamlit web app where users can upload images and get immediate classification results.
## Technologies Used
- OpenCV (CV2): For detecting faces and eyes in the image data.
- PyWavelet: To extract features for each image.
- Scikit-learn: Machine learning algorithms (SVM, Logistic Regression, Random Forest).
- Streamlit: Interactive web-based UI for image upload and classification.
- Python: Core programming language used for the entire workflow.
## How It Works
1. Image Preprocessing: The uploaded image is first processed using OpenCV to detect faces and focus strictly on facial features.
2. Feature Extraction: PyWavelet is used to extract important features from the detected face, which are then fed into the classifier.
3. Classification: The extracted features are classified using the SVM model, which delivers the most accurate results with 80% accuracy.
4. Result: The model predicts which sports personality the image represents, displaying the result in the Streamlit UI.
## Model Performance
After training and testing with a labeled dataset of sports personality images:

- SVM outperformed other models with an accuracy of 80%.
- Logistic Regression achieved 76% accuracy.
- Random Forest had an accuracy of 66%.
## Setup Instructions
To run this project locally:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/sport-personality-classification.git

2. **Install the required packages**:

   ```bash
   pip install -r requirements.txt

3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py

5. Upload an image and see the classification result.

## Future Improvements
- Expand the dataset to include more sports personalities.
- Enhance model accuracy by experimenting with deep learning techniques like Convolutional Neural Networks (CNNs).
- Add more robust facial feature extraction methods.
## Contributing
Feel free to fork this project and submit pull requests for improvements or additional features.

## Contact
For any inquiries or collaboration opportunities, reach out at [o.oyin1115@gmail.com](o.oyin1115@gmail.com).

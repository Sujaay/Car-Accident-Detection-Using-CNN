Accident Detection System
Overview
The Accident Detection System is a computer vision-based project designed to detect accidents in real-time using a pre-trained Convolutional Neural Network (CNN). The system processes video frames, predicts accidents, and triggers immediate notifications for timely response.
Features
•	Real-time Accident Detection: Utilizes a pre-trained CNN to analyze video frames and detect accidents.
•	Notification System: Sends SMS notifications using the Twilio API when accidents are detected.
•	Audio Alerts: Provides immediate attention through audio alerts using the winsound library.
•	Probabilistic Display: Displays real-time accident status and probability on the video feed.
Technologies Used
•	Python
•	TensorFlow, Keras
•	OpenCV
•	Twilio API for SMS notifications
•	NumPy
•	Winsound for audio alerts
Setup Instructions
1.	Clone the repository:
bashCopy code
git clone https://github.com/yourusername/accident-detection-system.git cd accident-detection-system 
2.	Install dependencies:
bashCopy code
pip install -r requirements.txt 
3.	Ensure the following are available:
•	Video file (car2.mp4) or adjust code for camera input.
•	Twilio account credentials (account_sid and auth_token).
•	Model architecture (model.json) and weights (model_weights.h5).
4.	Run the script:
bashCopy code
python accident_detection_script.py 
Usage
1.	Run the script with the specified setup.
2.	Press 'q' to exit the video feed.
Contributing
Contributions are welcome! If you'd like to contribute to the project, please follow the standard GitHub flow: fork the repository, create a branch, make your changes, and submit a pull request.


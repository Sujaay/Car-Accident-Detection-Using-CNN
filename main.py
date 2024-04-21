import cv2
import numpy as np
from datetime import datetime
from twilio.rest import Client
import winsound

from detection import AccidentDetectionModel  # Assuming 'detection' is a module in your project

# Initialize Twilio credentials and location information
account_sid = "YOUR TWILIO ACCOUNT"
auth_token = "Your Token address"
loc_address = "Camera Location"

# Initialize the accident detection model
model = AccidentDetectionModel("model.json", 'model_weights.h5')

# Initialize video capture
video = cv2.VideoCapture("car2.mp4")  # For camera use video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Resize the frame for prediction (assuming model input size is 250x250)
    resized_frame = cv2.resize(frame, (250, 250))

    # Perform prediction on the resized frame
    pred, prob = model.predict_accident(resized_frame[np.newaxis, :, :])

    if pred == "Accident":
        prob_percent = round(prob[0][0] * 100, 2)
        if prob_percent > 95:
            # Sound alert
            # winsound.Beep(440, 300)

            # Display accident information on the frame
            cv2.rectangle(frame, (0, 0), (280, 40), (0, 0, 0), -1)
            cv2.putText(frame, f"Accident {prob_percent}%", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            
            # Notify emergency services via Twilio
            now = datetime.now().strftime("%H:%M")
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=f"Accident detected. Coordinates: {loc_address}. Time: {now}. Send Help!!",
                from_="+14344783815",
                to="+919860550514"
            )
            print(message.sid)
    else:
        # Display no accident information on the frame
        cv2.rectangle(frame, (0, 0), (280, 40), (0, 0, 0), -1)
        cv2.putText(frame, "No Accident", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close all windows
video.release()
cv2.destroyAllWindows()

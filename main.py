import cv2
from detection import AccidentDetectionModel
import numpy as np
import os
from twilio.rest import Client
from datetime import datetime
import winsound

account_sid = "AC28293862da3455f559cd01b008e5b429"
auth_token = "8559f9f24903bd5744e0d0c6e5a151ac"       
loc_address = "18.555807, 73.736986"  
model = AccidentDetectionModel("model.json", 'model_weights.h5')
flag=0


video = cv2.VideoCapture("car2.mp4") # for camera use video = cv2.VideoCapture(0)
while True:
    ret, frame = video.read()
    if ret==True:  
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        roi = cv2.resize(gray_frame, (250, 250))
        pred, prob = model.predict_accident(roi[np.newaxis, :, :])
        if(pred == "Accident"):  
            prob = (round(prob[0][0]*100, 2))
            if(prob > 95):
                flag=1
            #    winsound.Beep(440, 300)
                cv2.rectangle(frame, (0, 0), (280, 40), (0, 0, 0), -1)
                cv2.putText(frame, pred+" "+str(prob), 
                                (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, 
                                (255, 255, 0), 2)
        else:
            cv2.rectangle(frame, (0, 0), (280, 40), (0, 0, 0), -1)
            cv2.putText(frame, "No Accident ", 
                                (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, 
                                (255, 255, 0), 2)
                
                    
                    
        cv2.imshow('Frame', frame)     
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
if flag==1:
    now = datetime.now()
    time = now.strftime("%H:%M")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                body="Accident detected. Coordinates: "+ loc_address + ". Time: "+time + ". Send Help!! ",
                from_="+14344783815",
                to="+919860550514"
    )    
    print(message.sid)
# release the cap object
video.release()
# close all windows
cv2.destroyAllWindows()

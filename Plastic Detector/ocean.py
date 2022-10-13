# run pip install https://raw.githubusercontent.com/ujjwalkar0/Garuda/master/requirement.txt
# to install dependencies

import cv2
import numpy as np 
import time
import requests
from datetime import datetime
import sys

path = 0
try:
    path = sys.argv[1]
except:
    pass

token=[1]
token[0] = input("Enter Your Token")

def SendImage(path):
    url = 'https://oceanplastic.herokuapp.com/api/'

    headers = {
        "Authorization": f"token {token[0]}",
    }

    files = {
        'image':open(path,'rb'),
    }

    print("Start Uploading....")
    r = requests.post(url, files=files, headers=headers)

    print(r.status_code)

    if r.status_code==503:
        token[0] = input("Enter Your Token")
        return SendImage(path)

    elif r.status_code != 200:
        time.sleep(2)
        return SendImage(path)

    print(r.text)


net = cv2.dnn.readNet("weights/yolov4-custom_last.weights","yolov4-custom.cfg")
classes = ['trash_plastic']

layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

cap = cv2.VideoCapture(path)

while True:
    _, img = cap.read()
    if img is None:
        break

    img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    print(len(class_ids))

    if len(class_ids) >0:
        filename = 'savedImage.jpg'
        temp = img
        cv2.imwrite(filename, img)
        SendImage(filename)
        

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[0]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y + 30), font, 3, color, 3)
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == 27 & 0xFF == ord('q') :
        break

cap.release()
cv2.destroyAllWindows()
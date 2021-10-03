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

def SendImage(path):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    date = now.strftime("%D")
    date = date.replace('/','-')

    r = requests.get('https://ipinfo.io')
    x = r.json()['loc']

    url = 'http://127.0.0.1:8000/upload/'

    data = {
        'name':'Trash_Plastic',
        'location': x,
        'time': current_time,
        'date':date,
        }
    files = {
        'image':open(path,'rb'),
    }
    r = requests.post(url, data = data, files=files)

    if r.status_code != 200:
        time.sleep(2)
        return SendImage(path)

    print(r.status_code)


net = cv2.dnn.readNet("weights/yolov4-custom_last.weights","yolov4-custom.cfg")
classes = ['trash_plastic']

layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# Loading image
# img = cv2.imread("nasa.png")
# img = cv2.resize(img, None, fx=0.4, fy=0.4)

cap = cv2.VideoCapture(path)

while True:
    _, img = cap.read()
    try:
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
        if key == 27:
            break
    except:
        pass

cap.release()
cv2.destroyAllWindows()
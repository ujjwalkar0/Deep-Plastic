import cv2
import numpy as np 
import time
import requests
from datetime import datetime
import sys
from .models import UploadImageTest
import datetime
from rest_framework.authtoken.models import Token


def UploadImage(request, path):
    token, created = Token.objects.get_or_create(user=request.user)

    url = f"http://{request.get_host()}/api/"
    if request.is_secure():
        url = f"https://{request.get_host()}/api/"

    files = {
        'image':open(path,'rb'),
    }

    headers = {
        "Authorization": f"token {token.key}",
    }

    print(headers)

    r = requests.post(url, files=files, headers=headers)
    
    if r.status_code != 200:
        time.sleep(2)
        return UploadImage(request, path)

    print(r.text)

def CheckVideo(request,link):
    print(link)    
    net = cv2.dnn.readNet("dbs/weights/yolov4-custom_last.weights","dbs/yolov4-custom.cfg")
    classes = ['trash_plastic']


    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    # Loading image
    # img = cv2.imread("nasa.png")
    # img = cv2.resize(img, None, fx=0.4, fy=0.4)

    cap = cv2.VideoCapture(link)

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
            filename = f'Trash-Image.jpg'
            # temp = img
            cv2.imwrite(filename, img)
            UploadImage(request, filename)

            # UploadImageTest.objects.create(location=request.user, image=filename).save()
            

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[0]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label, (x, y + 30), font, 3, color, 3)

        # key = cv2.waitKey(1)
        # if key == 27 & 0xFF == ord('q'):
        #     break

    # cap.release()
    # cv2.destroyAllWindows()

    return "Complete"
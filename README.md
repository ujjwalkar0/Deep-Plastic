# Garuda
This project is for NASA Space Apps Challenge : https://2021.spaceappschallenge.org/challenges/statements/leveraging-aiml-for-plastic-marine-debris/details

### Problem
Plastic pollution has a direct and fatal impact on wildlife. Thousands of seabirds, sea turtles, seals and other marine mammals are killed every year after ingesting or entangled in plastic. Plastic fragments that contain chemicals and are often ingested by marine animals can harm wildlife. Floating plastic trash can survive in the water for thousands of years, as a miniature transportation vehicle for invasive species, destroying habitats. The most obvious and disturbing effect of ocean plastics is the ingestion, suffocation and entanglement of hundreds of marine species. Marine wildlife such as seabirds, whales, fish, and sea turtles mistake plastic waste for prey, and most of them starve to death because their stomachs are full of plastic debris.
Can we not detect how much plastics go to ocean every year ?

### Solution : Monitor Plastics and Reduce uses
I have made a Trash Plastic Detection system. It comes with both CLI and web versions. Embedded computers with Satellites, drones, submarines, etc. detect and send pictures of trash plastic to a database. It can detect plastics from a video, and send them to a server. A web interface also available where we can upload video, and trash plastics of the videos shown on website.
In future if we make a similar system that detects ocean life and sends images to the same server, and show these in an app, people interested in ocean life download the app. People see how we waste our earth, and they reduce the use of plastic

### How It Works ?
Method 1. A Computer integrated on Satellites or Drones or Submarine run <a href="https://raw.githubusercontent.com/ujjwalkar0/Garuda/master/Plastic%20Detector/ocean.py">ocean.py</a>  which takes photograph of ocean and whenever plastic detected it will send to a server. Go to https://oceanplastic.herokuapp.com/ to see images  

Method 2. Satellites or Drones, Submarine collect video of ocean. Pass this video through <a href="https://raw.githubusercontent.com/ujjwalkar0/Garuda/master/Plastic%20Detector/ocean.py">ocean.py</a>. All images of plastics will send to a database. Go to https://oceanplastic.herokuapp.com/ to see images 

Go to following Link for Details :
https://github.com/ujjwalkar0/Garuda/tree/master/Plastic%20Detector

![image](https://user-images.githubusercontent.com/55041104/135787349-0ae8a4fa-741f-48cc-a042-bc29cc2b0083.png)

Method 3: Collect video of ocean and upload it to https://oceanplastic.herokuapp.com/upload. Go to oceanplastic.heroku.app to see images  

![image](https://user-images.githubusercontent.com/55041104/135787519-710c5544-4640-487e-8114-6af53d5d6991.png)

### What benefits does it have?

If we make a similar system that detects ocean life and sends images to the same server, and show these in an app, people interested in ocean life download the app. People see how we waste our earth, and they reduce the use of plastic. This is the benefit.

### Technology Uses : 
Python, Opencv, Django, Bootstrap, and Most important thing Yolo object detection.

### References:
Get started with: https://github.com/gautamtata/DeepPlastic
Dataset: https://drive.google.com/drive/folders/1tk4HDftOVzmROHpkWRUIwL0Gu_p2E-qa
Youtube: https://youtu.be/yGMZOD44GrI and others...

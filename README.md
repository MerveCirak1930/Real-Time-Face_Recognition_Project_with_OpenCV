# Real-Time Face Recognition Project for Security and Time Management with OpenCV

## Face Detection
Its purpose is to find faces (position and size) in an image and extract them for possible use by the face recognition algorithm.

## Face Recognition
When face images have already been extracted, cropped, resized, and usually converted to grayscale, the face recognition algorithm is responsible for finding the features that best describe the image.

## Summary of files and folders in our project

### In our project, we first created the files yuz_verisi.py, yuz_tanima.py, and deneme.py, and two folders named deneme and dati.

- yuz_verisi.py: The module where we created our dataset within the data folder.
We introduced each person in our dataset to the camera by changing the yuz_name variable.
- deneme.py: The module where we trained our dataset.
- yuz_tanima.py: The module that will recognize faces shown to the camera by comparing them with faces in our dataset.
- veri.yml: The folder where our dataset is stored.
- deneme.yml: The folder where the data in our dataset is stored after training.

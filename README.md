# 👤 Face Recognition Comparison

A simple Python project that uses **face recognition** to compare two images and determine whether they contain the same person.

The program detects the face in each image, generates a numerical **face encoding** for each face, compares the encodings, and displays the result using OpenCV.

In this example, an image of **Tom Holland** is compared with an image of **Robert Downey Jr.**

## ✨ Features

* 👤 Detects faces in images
* 🧠 Generates facial encodings
* 🔍 Compares two faces
* 📏 Calculates the face distance between them
* 🟪 Draws bounding boxes around detected faces
* 🖥️ Displays the images and comparison result using OpenCV

## 🛠️ Technologies Used

* **Python**
* **OpenCV (`cv2`)** - Image processing and displaying images
* **NumPy** - Numerical operations
* **face_recognition** - Face detection, encoding, and comparison

## 📋 Requirements

Install the required Python packages:

```bash
pip install opencv-python numpy face-recognition
```

> **Note:** The `face-recognition` library depends on `dlib`, which can sometimes require additional setup depending on your operating system and Python version.

## 📁 Project Structure

The project expects the images to be stored inside an `images` folder:

```text
Face-Recognition/
│
├── attendance images/
│   ├── Chris Evans.jfif
|   ├── Tom Hollands.jfif
│   └── Robert Downey Jr.jpg
├── images/
│   ├── Tom Hollands.jfif
|   ├── Tom Hollands Test.jfif
│   └── Robert Downey Jr.jpg
│
├── attend_recog.py
├── attendance.csv
├── img_recog.py
└── README.md
```

## 🚀 How to Run

1. Clone or download the repository.

2. Make sure the required images are inside the `images` folder.

3. Install the dependencies:

```bash
pip install opencv-python numpy face-recognition
```

4. Run the program:

```bash
python attend_recog.py
```

5. Two windows will appear showing the video camera input.

6. Attendance with time stamp will be saved to csv file if the person matches with saved photos.

Press any key to close the windows.

## 🔍 How It Works

The program follows this process:

```text
Load Image
    │
    ▼
Detect Face
    │
    ▼
Generate Face Encoding
    │
    ├───────────────┐
    │               │
    ▼               ▼
Image 1          Image 2
    │               │
    └───────┬───────┘
            ▼
     Compare Encodings
            │
            ▼
       Face Distance
            │
            ▼
     Display Result
            │
            ▼
  save to person + timestamp attendance.csv
```
## ⚠️ Limitations

This project is intentionally simple and has several limitations:

* It assumes each frame contains at least one face.
* It only compares the **first detected face** in each frame.
* Accuracy can be affected by lighting, pose, image quality, and facial expressions.
* It is not designed for large-scale face recognition.
* The program does not handle multiple people in a frame.
* The images are hardcoded into the Python file.

## 🔮 Possible Improvements

The project could be expanded by adding:

* 👥 Recognition of multiple faces
* 📁 Automatic loading of a folder of known faces
* 🏷️ Assigning names to recognized people
* 🎯 Adjustable recognition thresholds
* 🖥️ A graphical user interface
* 💾 Saving face encodings for faster recognition
* 🔎 Recognition against a larger database
* 🚨 Notifications when an unknown face is detected

## 📚 Concepts Demonstrated

This project provides a basic introduction to:

* Computer vision
* Face detection
* Facial feature encoding
* Image processing
* Similarity comparison
* OpenCV
* Python libraries
* Basic biometric recognition

## 📄 License

This project is intended for educational and personal use.
All copy rights reserved to photographers who took the photos, I just took them from google >.

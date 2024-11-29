# **AI-Enhanced Engagement Tracker for Young Learners**
### **Infosys Springboard Internship - October 2024**

#### **Image Processing with OpenCV**

This project utilizes **OpenCV** for developing various image processing functionalities to enhance engagement tracking for young learners. The project focuses on operations like image concatenation, contour detection, cropping, morphological transformations, and more.

- **Library/Framework**: OpenCV
- **Version**: 4.10.0.84

---

## **Developed Features**

### A) **Image Concatenation**
- Resizes two input images to a specified pixel range and combines them horizontally and vertically.
- Uses `np.hstack()` for horizontal concatenation and `np.vstack()` for vertical concatenation.
- Displays concatenated results in separate windows.

**Input:**
![Input Image 1](https://github.com/user-attachments/assets/9877bd95-e226-426c-9395-bc59153199a3)
![Input Image 2](https://github.com/user-attachments/assets/4a0c9a80-c161-4199-b332-6d0c3cb5ffcc)

**Output:**
![Concatenated Image](https://github.com/user-attachments/assets/bb95e7e3-61fa-4c3d-b2ee-8705892ea3bc)

---

### B) **Image Contour Detection**
- Detects contours in a grayscale image by applying a binary threshold.
- Uses `cv2.findContours()` to identify contours and draws them in green.
- Displays the contour-highlighted image in a separate window.

**Input:**
![Grayscale Input](https://github.com/user-attachments/assets/4a0c9a80-c161-4199-b332-6d0c3cb5ffcc)

**Output:**
![Contour Output](https://github.com/user-attachments/assets/aa14d5c1-5a83-435d-9c22-39fe5de41ef4)

---

### C) **Image Crop**
- Extracts a specific region from the original image based on a defined pixel range.
- Displays the cropped image in a separate window.

**Input:**
![Input Image](https://github.com/user-attachments/assets/a44f9b5a-6251-4020-8621-cdb8a941ecc1)

**Output:**
![Cropped Output](https://github.com/user-attachments/assets/d8bfd525-0d02-44c0-a372-02d2a8ea37fa)

---

### D) **Image Dilation & Erosion**
- Uses a kernel matrix to perform morphological dilation and erosion, enhancing or reducing specific features.
- Displays both dilated and eroded images in separate windows.

**Input:**
![Input Image](https://github.com/user-attachments/assets/e426342c-d132-472f-ac3d-6d8a7d9d7f85)

**Output:**
![Dilated & Eroded Output](https://github.com/user-attachments/assets/eb05eeb4-86e5-4fd6-960d-0aba939527a0)

---

### E) **Edge Detection**
- Applies **Edge Detection** with threshold values of 100 and 200.
- Displays the edge-detected image in a separate window.

**Input:**
![Grayscale Input](https://github.com/user-attachments/assets/671b4832-f723-4816-9c1b-631a87ff0993)

**Output:**
![Edge Detection Output](https://github.com/user-attachments/assets/43a4e365-4793-41bd-8282-e38404e3f56f)

---

### F) **Histogram Equalization**
- Enhances the contrast of a grayscale image using histogram equalization.
- Displays the equalized image in a separate window.

**Input:**
![Grayscale Input](https://github.com/user-attachments/assets/98640483-f13c-436a-96c7-0c4a0003d686)

**Output:**
![Equalized Output](https://github.com/user-attachments/assets/ee2eadcc-2ebf-44e2-b49d-3ce756ff56bc)

---

### G) **HSV Conversion**
- Converts a BGR image to the HSV color space.
- Displays the HSV-converted image in a separate window.

**Input:**
![BGR Input](https://github.com/user-attachments/assets/b26c4076-3591-4631-b8f4-7d85f87664db)

**Output:**
![HSV Output](https://github.com/user-attachments/assets/9e4412e2-9501-47db-881b-5020a43faed3)

---

### H) **Morphological Transformation (Opening & Closing)**
- Performs `Opening` (erosion followed by dilation) to remove noise and `Closing` (dilation followed by erosion) to fill gaps.
- Displays the processed images in separate windows.

**Input:**
![Input Image](https://github.com/user-attachments/assets/744e8b69-4baa-43ed-8329-dc838f8a0c60)

**Output:**
![Morphological Transformation Output](https://github.com/user-attachments/assets/28fc43c4-f03e-4068-b6d6-12a0ac280aeb)

---

### I) **Image Resize**
- Resizes the input image to specified dimensions.
- Displays the resized image in a separate window.

**Input:**
![Input Image](https://github.com/user-attachments/assets/0c31f8d3-5465-47b5-8f52-4c28825f8a67)

**Output:**
![Resized Output](https://github.com/user-attachments/assets/c1a2006d-19a4-47c3-b4c4-657becff578d)

---

### J) **RGB to Grayscale Conversion**
- Converts a color image to grayscale using `cv2.cvtColor()` and saves the result.
- Displays the grayscale image in a separate window.

**Input:**
![Input Image](https://github.com/user-attachments/assets/d2b162f2-c5e4-4e41-9436-8f75611e0197)

**Output:**
![Grayscale Output](https://github.com/user-attachments/assets/1673a693-b249-4499-bf88-55862193a748)

---

### K) **Image Rotation**
- Rotates the image by 90 degrees around its center using `cv2.warpAffine()`.
- Displays the rotated image in a separate window.

**Input:**
![Input Image](https://github.com/user-attachments/assets/a16a3e78-45a2-47db-ad11-3c8756eb0b37)

**Output:**
![Rotated Output](https://github.com/user-attachments/assets/bd727570-7d95-4a42-ba44-1c78ada5a74c)

---

### L) **Image Blur**
- Applies a Gaussian blur with a 15x15 kernel to reduce noise and smooth the image.
- Displays the blurred image in a separate window.

**Input:**
![Input Image](https://github.com/user-attachments/assets/e3e2cfad-ab4e-4696-87bc-f7b176b06d18)

**Output:**
![Blurred Output](https://github.com/user-attachments/assets/dfe50e24-cbe3-491d-be99-e7b7b433c681)

---

#### **Image and Video Processing with OpenCV**

This project leverages **OpenCV** for developing various image and video processing functions, with additional support for annotations to enhance engagement tracking for young learners. The project includes operations such as noise removal, morphological transformations, template matching, and more.

- **Library/Framework**: OpenCV
- **Version**: 4.10.0.84

---

## **Image Processing**

### **Developed Features**

#### M) `image_noise_removal & closing_gaps`
- **Functionality**: Uses morphological operations to remove noise and fill gaps in the image, helping to clean up the image data for better clarity and analysis.

#### N) `image_template`
- **Functionality**: Performs template matching to locate a template image within a larger image, enabling the identification of specific regions of interest.

---

## **Video Processing**

### **Libraries or Frameworks Used:**
- **OpenCV**: Version 4.10.0.84

### **Developed Features**

#### A) `Video_multivideo`
- **Functionality**: Reads and displays images from a specified folder, printing the dimensions of each image for inspection and verification.

#### B) `Video_fps`
- **Functionality**: Captures video from the webcam, displays it in real-time, and calculates the frames per second (FPS), allowing users to monitor the performance.

#### C) `Video_save`
- **Functionality**: Captures live video and saves it to a specified output file, enabling users to record and review footage.

#### D) `Video_stack`
- **Functionality**: Reads and resizes two video files, concatenating them horizontally, which allows for side-by-side video comparisons.

#### E) `Video_stream`
- **Functionality**: Captures live video from the webcam and displays it in real-time, providing a continuous live stream for immediate feedback.

---

## **Annotations**

### **Libraries or Frameworks Used:**
- **OpenCV**: Version 4.10.0.84
- **LabelImg**: Version 1.8.6

### **Developed Features**

#### A) `data_segregate`
- **Functionality**: Organizes images and their label files by moving them into `matched` and `unmatched` directories based on their label status, making data management easier.

- **Input:**
  ![Input Image](https://github.com/user-attachments/assets/02e52f2f-6748-4001-afc5-5dcd6b0878d1)

- **Output:**
  ![Output Image](https://github.com/user-attachments/assets/2d4752e2-503a-42d0-960d-a8c4052ea4af)

#### B) `label`
- **Functionality**: Draws bounding boxes on images based on annotations in the label files, helping to visualize detected objects and regions of interest.

- **Input:**
  ![Input Image](https://github.com/user-attachments/assets/00912d51-adb0-4966-99b3-050b5ebdf0b5)

- **Output:**
  ![Output Image](https://github.com/user-attachments/assets/9313c7f1-aa45-45e5-bd1f-625b73ca6a57)

#### C) `label_manipulate`
- **Functionality**: Updates class numbers in label files for object detection tasks, facilitating the reclassification or adjustment of labels as needed.

- **Input:**
  ![Input Image](https://github.com/user-attachments/assets/f37cebd8-1bec-4b76-be9e-d4ca59d9cc13)

- **Output:**
  ![Output Image](https://github.com/user-attachments/assets/ec43245d-01b4-4b4e-9e70-ef4088e713d4)

---

This project leverages **OpenCV**, **dlib**, and **face_recognition** libraries to perform real-time face recognition, attentiveness tracking, and attendance logging for online educational applications. The goal is to improve engagement tracking by capturing detailed data on student participation, attentiveness, and facial recognition events.

---

## **Face Recognition**

### **Libraries or Frameworks Used:**
- **OpenCV**: Version 4.10.0.84
- **LabelImg**: Version 1.8.6
- **dlib**: Version 19.24.6
- **face_recognition**: Version 1.3.0
- **imutils**: Version 0.5.4

### **Developed Features**

#### A) `Face_recognition`
- **Functionality**: Performs real-time face recognition to identify whether the individual in live video frames matches a known face. Displays the person’s name if recognized; otherwise, shows "Not Recognized."

- **Input:**
  ![Sample Input Image](https://github.com/user-attachments/assets/ef6b1a6e-57a9-4b60-a5c5-40bd47680012)

- **Output:**
  ![Sample Output Image](https://github.com/user-attachments/assets/87f7bfdf-e0e0-41fb-b9a6-4ffdd58afc04)

#### B) `Attendence_save`
- **Functionality**: Utilizes a live video feed to identify and log attendance with date and time. After five recognitions, saves records to an Excel file and resets the counter.

- **Input:**
  ![Sample Input Image](https://github.com/user-attachments/assets/ef6b1a6e-57a9-4b60-a5c5-40bd47680012)

- **Output:**
  ![Sample Output Image](https://github.com/user-attachments/assets/d902b33c-7639-4a2a-ab97-3706af531af6)
  ![Additional Output Image](https://github.com/user-attachments/assets/0953d67b-0e85-43ab-b7d5-2a2887aba4fa)

#### C) `test`
- **Functionality**: Recognizes faces in a live video feed, logging each identification event every 30 seconds to Excel to avoid duplicates. Displays "Recognized" or "Not Recognized."

- **Input:**
  ![Sample Input Image](https://github.com/user-attachments/assets/323fea74-a68d-45bb-905e-64105c64ab98)

- **Output:**
  ![Sample Output Image](https://github.com/user-attachments/assets/412ad2ad-0468-4976-aed0-5f78486af917)
  ![Additional Output Image](https://github.com/user-attachments/assets/b37c0bcc-0dd5-420b-bafe-e981e66a91b9)

#### D) `tools`
- **Functionality**: Captures real-time video to recognize faces, saving attendance logs after five detections. Exits and saves data when 'q' is pressed.

- **Input:**
  ![Sample Input Image](https://github.com/user-attachments/assets/ef6b1a6e-57a9-4b60-a5c5-40bd47680012)

- **Output:**
  ![Sample Output Image](https://github.com/user-attachments/assets/0e67fd69-db4d-49be-88e6-9a331d62ccc5)
  ![Additional Output Image](https://github.com/user-attachments/assets/f6575fd2-b8fb-4915-8864-90d3de696025)

#### E) `excel_sc`
- **Functionality**: Logs attendance to Excel, capturing screenshots every 30 seconds with error handling and termination on pressing 'q'.

- **Input:**
  ![Sample Input Image](https://github.com/user-attachments/assets/dfc4223a-39ca-49c4-8a37-e1316e40b8b9)

- **Output:**
  ![Sample Output Image](https://github.com/user-attachments/assets/5fc7f30e-ce33-4047-8e1a-c31e54c16b6b)
  ![Additional Output Image](https://github.com/user-attachments/assets/8b5de8b6-4460-40be-b370-ebcb2dc9bfdf)

#### F) `excel_sc_dt`
- **Functionality**: Uses real-time face recognition to log attendance, capturing screenshots and avoiding multiple logs within a 5-minute interval.

- **Input:**
  ![Sample Input Image](https://github.com/user-attachments/assets/e9b887a3-c584-41f1-a5a8-5d5c2c9bc3a9)

- **Output:**
  ![Sample Output Image](https://github.com/user-attachments/assets/b0867453-3e33-4962-b06c-6f9097943284)
  ![Additional Output Image](https://github.com/user-attachments/assets/ca58f282-39ee-44cd-b6c4-4165d816fb3a)

#### G) `landmark`
- **Functionality**: Tracks attentiveness in real-time, logging events with timestamp and screenshot, and displays "Attentive" or "Not Attentive."

- **Input:**
  ![Sample Input Image](https://github.com/user-attachments/assets/043e1cd9-a586-4f51-9e9c-76d2e69397bf)

- **Output:**
  ![Sample Output Image](https://github.com/user-attachments/assets/a153f6ac-cf89-4aa0-90d7-cebe64bc7758)
  ![Additional Output Image](https://github.com/user-attachments/assets/ff1229d5-f576-46d1-b57b-713056cdb7f5)

#### H) `atten_score`
- **Functionality**: Computes attentiveness based on head pose and logs to Excel every 30 seconds if attentive.

- **Input:**
  ![Sample Input Image](https://github.com/user-attachments/assets/731848e6-0bce-4971-84fe-e756729d76b6)

- **Output:**
  ![Sample Output Image](https://github.com/user-attachments/assets/cd5d5421-1e46-49fc-a07d-511cb2fad86e)
  ![Additional Output Image](https://github.com/user-attachments/assets/65a0dafe-eebf-48ab-a8df-08d4b0e08c7e)

#### I) `avg_atten_score`
- **Functionality**: Calculates attentiveness scores and logs data to Excel every 30 seconds, displaying an average attentiveness score at the end of the session.

- **Input:**
  ![Sample Input Image](https://github.com/user-attachments/assets/3e8f0c19-08cf-497c-8463-89e6b6e4de95)

- **Output:**
  ![Sample Output Image](https://github.com/user-attachments/assets/c45ca786-e6de-4f19-867f-f643e5aee5ab)
  ![Additional Output Image 1](https://github.com/user-attachments/assets/399a5178-f728-4e24-8dca-df6dc5536b0f)
  ![Additional Output Image 2](https://github.com/user-attachments/assets/3eb18991-da16-42e7-add4-685c8d950ff2)

---

Each feature is designed to enhance face recognition, attendance tracking, and attentiveness monitoring, supporting engagement tracking in educational applications.




# Advanced Student Monitoring System

## Overview
The Advanced Student Monitoring System is a sophisticated Python application designed to monitor student attention and engagement during online learning sessions. It uses computer vision and facial recognition technologies to track student presence, attention levels, and suspicious activities in real-time.

## Features
- **Face Recognition**: Identifies registered students and detects unknown faces
- **Attention Monitoring**: 
  - Tracks eye movements and mouth positions
  - Calculates real-time attention scores
  - Monitors head position and orientation
- **Activity Tracking**:
  - Records student attendance (login/logout times)
  - Monitors keyboard activity for suspicious behavior
  - Takes random screenshots for verification
- **Logging System**:
  - Generates detailed Excel logs for each student
  - Tracks face missing incidents
  - Records average attention scores
  - Documents keyboard events and screenshots

## Prerequisites

Required packages:
- OpenCV (cv2)
- face_recognition
- dlib
- pandas
- numpy
- imutils
- keyboard

## Project Structure
student_monitoring/
│
├── advanced_student_monitoring.py # Main application file
├── known_students/ # Directory for student reference images
├── monitoring_screenshots/ # Directory for captured screenshots
├── student_logs/ # Directory for Excel log files
└── shape_predictor_68_face_landmarks.dat # Required facial landmark model

## Setup Instructions
1. Install the required dependencies
2. Download the shape predictor file from dlib's official repository
3. Create a directory for known students and add their reference photos
4. Update the model path in the code to point to your shape predictor file

## Usage
1. Add student reference photos to the `known_students` directory
   - Name format: `student_name.jpg`
   - One clear frontal face photo per student

2. Run the application: python advanced_student_monitoring.py
   
4. The system will:
   - Start the webcam
   - Begin monitoring students
   - Display real-time video feed with attention scores
   - Generate logs automatically

5. Press 'q' to quit the application

## Configuration
You can adjust various parameters in the `StudentMonitoringSystem` class:
- `MAX_YAW_THRESHOLD`: Maximum head rotation threshold
- `MAX_PITCH_THRESHOLD`: Maximum head tilt threshold
- `KEYBOARD_THRESHOLD`: Maximum allowed keyboard events per minute

## Output
some sample are:


https://github.com/user-attachments/assets/0d209679-4178-43cb-bc46-d5d38a4582e2

![image](https://github.com/user-attachments/assets/23a910c5-7b77-4c40-8345-39284024f400)


- **Excel Logs**: Generated in the `student_logs` directory
  - Date and time stamps
  - Attendance records
  - Attention scores
  - Activity metrics

- **Screenshots**: Stored in the `monitoring_screenshots` directory
- sample output:
![mousam_photo_20241129_193013](https://github.com/user-attachments/assets/d1d20a4a-c804-4aac-abb2-e9e496d2434b)
![mousam_photo_20241129_195445](https://github.com/user-attachments/assets/a23e4237-ca66-4a0d-9b57-c0650c18db13)
![mousam_photo_20241129_194135](https://github.com/user-attachments/assets/5e65d575-fb49-4bed-ac41-0641b9ef13a6)
![mousam_photo_20241129_193455](https://github.com/user-attachments/assets/20594555-b690-4604-8ff2-3f27ad748078)

  - Random captures during sessions
  - Named with timestamp and student ID

## Security Features
- Unknown face detection
- Suspicious keyboard activity monitoring
- Random screenshot verification
- Comprehensive activity logging

## Limitations
- Requires good lighting conditions
- Depends on stable internet connection for real-time processing
- Requires proper camera positioning

## Contributing
Feel free to fork this project and submit pull requests for any improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- dlib for facial landmark detection
- face_recognition library for face recognition capabilities
- OpenCV community for computer vision tools



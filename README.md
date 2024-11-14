# Mousam_AshAI-Enhanced-Engagement-Tracker-for-Young-Learners_Infosys_Internship_Oct2024
infosys spring bord internship
Image Processing 

Libraries or Frame Works used - opencv 

Version - 4.10.0.84 

Developed Logics -

A) image_concatenation:- This resizes two images, to given trange of pixels and combines them both horizontally and vertically. Using np.hstack() and np.vstack(), the images are concatenated side-by-side and one on top of the other, respectively. The concatenated results are displayed in separate windows.

Input :-
![download](https://github.com/user-attachments/assets/9877bd95-e226-426c-9395-bc59153199a3)
![OIP](https://github.com/user-attachments/assets/4a0c9a80-c161-4199-b332-6d0c3cb5ffcc)


Output :- 

![image](https://github.com/user-attachments/assets/bb95e7e3-61fa-4c3d-b2ee-8705892ea3bc)


B) image_contour :- This detects contours in a grayscale image. First, it applies a binary threshold to the image to separate foreground from background. Then, it finds contours using cv2.findContours() and draws them onto the original image in green. The result, with highlighted contours, is displayed in a separate window.

Input :- 

![OIP](https://github.com/user-attachments/assets/4a0c9a80-c161-4199-b332-6d0c3cb5ffcc)

Output :- 

![image](https://github.com/user-attachments/assets/aa14d5c1-5a83-435d-9c22-39fe5de41ef4)


C) image_crop :- It extracts a specific region from the original image, defined by the pixel range, and displays the cropped section in a separate window.

Input :-

![OIP](https://github.com/user-attachments/assets/a44f9b5a-6251-4020-8621-cdb8a941ecc1)


Output :- 

![image](https://github.com/user-attachments/assets/d8bfd525-0d02-44c0-a372-02d2a8ea37fa)


D) image_dilation & erosion :- A kernel matrix is used to perform dilation and erosion, which enhance and reduce certain features of the image, respectively. The results of these morphological operations, dilated and eroded images, are displayed in separate windows.

Input :- 

![download](https://github.com/user-attachments/assets/e426342c-d132-472f-ac3d-6d8a7d9d7f85)


Output :- 

![image](https://github.com/user-attachments/assets/eb05eeb4-86e5-4fd6-960d-0aba939527a0)


E) image_edge detection:- This detects edges in a grayscale image using the **Canny edge detection** algorithm. The `cv2.Canny()` function is applied with threshold values of 100 and 200 to identify edges in the image. The resulting edge-detected image is displayed in a separate window.

Input :- 

![download](https://github.com/user-attachments/assets/671b4832-f723-4816-9c1b-631a87ff0993)


Output :- 

![image](https://github.com/user-attachments/assets/43a4e365-4793-41bd-8282-e38404e3f56f)



F) image_histogram_equalization :- This performs **histogram equalization** on a grayscale image to improve the contrast of the image. The `cv2.equalizeHist()` function enhances the image by redistributing the intensity values across the full range, making the dark areas brighter and the bright areas darker. The resulting equalized image is displayed in a separate window.

Input :-

![download](https://github.com/user-attachments/assets/98640483-f13c-436a-96c7-0c4a0003d686)


Output :- 

![image](https://github.com/user-attachments/assets/ee2eadcc-2ebf-44e2-b49d-3ce756ff56bc)



G) image_hsv :- This converts a color image from the BGR color space (used by OpenCV) to the HSV color space using the `cv2.cvtColor()` function. The result is displayed in a separate window, where the image is represented in Hue, Saturation, and Value (HSV) instead of the standard Blue, Green, Red (BGR) format.

Input :- 

![OIP](https://github.com/user-attachments/assets/b26c4076-3591-4631-b8f4-7d85f87664db)


Output :- 

![image](https://github.com/user-attachments/assets/9e4412e2-9501-47db-881b-5020a43faed3)


H) image_morphological_transformation :- This applies morphological operations, opening, and closing, to a grayscale image to process noise and gaps. `Opening` (erosion followed by dilation) removes small noise from the image, while `Closing` (dilation followed by erosion) fills small holes or gaps. The processed images are displayed in separate windows, showing the effects of noise removal and gap filling.

Input :- 

![OIP](https://github.com/user-attachments/assets/744e8b69-4baa-43ed-8329-dc838f8a0c60)


Output :- 

![image](https://github.com/user-attachments/assets/28fc43c4-f03e-4068-b6d6-12a0ac280aeb)


I) image_resize :- This resizes an input image, to the dimensions of a given range of pixels. The resized image is then displayed in a separate window.

Input :- 

![OIP](https://github.com/user-attachments/assets/0c31f8d3-5465-47b5-8f52-4c28825f8a67)


Output :- 

![image](https://github.com/user-attachments/assets/c1a2006d-19a4-47c3-b4c4-657becff578d)


J) image_rgb2gray :- This converts a color image to grayscale using `cv2.cvtColor()` and saves the grayscale version image. The grayscale image is then displayed in a separate window.

Input :- 

![OIP](https://github.com/user-attachments/assets/d2b162f2-c5e4-4e41-9436-8f75611e0197)


Output : - 

![image](https://github.com/user-attachments/assets/1673a693-b249-4499-bf88-55862193a748)


K) image_rotate :- This rotates an image by 90 degrees around its center. It first calculates the center point and then creates a rotation matrix with a 90-degree angle. Using `cv2.warpAffine()`, the image is rotated and displayed in a separate window. 

Input :- 

![download](https://github.com/user-attachments/assets/a16a3e78-45a2-47db-ad11-3c8756eb0b37)


Output :- 

![image](https://github.com/user-attachments/assets/bd727570-7d95-4a42-ba44-1c78ada5a74c)


L) image_blur :- This code applies a Gaussian blur to an image using a 15x15 kernel size, which helps in reducing image noise and detail. The blurred image is then displayed in a separate window.

Input :- 

 ![download](https://github.com/user-attachments/assets/e3e2cfad-ab4e-4696-87bc-f7b176b06d18)


Output :- 

![image](https://github.com/user-attachments/assets/dfe50e24-cbe3-491d-be99-e7b7b433c681)



#### M) `image_noise_removal & closing_gaps`
This function removes noise and fills gaps using morphological operations.

#### N) `image_template`
This function performs template matching to locate a template image within a larger image.

## Video Processing

### Libraries or Frameworks Used:
- **OpenCV**: Version 4.10.0.84

### Developed Logics:

#### A) `Video_multivideo`
This function reads and displays images from a specified folder, printing the dimensions of each image.

#### B) `Video_fps`
This function captures video from the webcam, displays it in real-time, and calculates the FPS.

#### C) `Video_save`
This function captures live video and saves it to a specified output file.

#### D) `Video_stack`
This function reads and resizes two video files, concatenating them horizontally.

#### E) `Video_stream`
This function captures live video from the webcam and displays it in real-time.

## Annotations

### Libraries or Frameworks Used:
- **OpenCV**: Version 4.10.0.84
- **LabelImg**: Version 1.8.6

### Developed Logics:

#### A) `data_segregate`
This function organizes images and their label files into matched and unmatched directories.

- **Input:**

![image](https://github.com/user-attachments/assets/02e52f2f-6748-4001-afc5-5dcd6b0878d1)


- **Output:**

![image](https://github.com/user-attachments/assets/2d4752e2-503a-42d0-960d-a8c4052ea4af)


#### B) `label`
This function draws bounding boxes on images based on annotations in the label files.

- **Input:**
![image](https://github.com/user-attachments/assets/00912d51-adb0-4966-99b3-050b5ebdf0b5)


- **Output:**

![image](https://github.com/user-attachments/assets/9313c7f1-aa45-45e5-bd1f-625b73ca6a57)


#### C) `label_manipulate`
This function updates class numbers in label files for object detection tasks.

- **Input:**

![image](https://github.com/user-attachments/assets/f37cebd8-1bec-4b76-be9e-d4ca59d9cc13)



- **Output:**

![image](https://github.com/user-attachments/assets/ec43245d-01b4-4b4e-9e70-ef4088e713d4)


## Face Recognition

### Libraries or Frameworks Used:
- **OpenCV**: Version 4.10.0.84
- **LabelImg**: Version 1.8.6
- **dlib**: Version 19.24.6
- **face_recognition**: Version 1.3.0
- **imutils**: Version 0.5.4

### Developed Logics:

#### A) `Face_recognition`
This performs real-time face recognition to identify whether the person in live video frames a known image by comparing. His name is displayed if He/She is recognized; otherwise, "Not He/She" appears.

- **Input:**

![mousam_photo](https://github.com/user-attachments/assets/ef6b1a6e-57a9-4b60-a5c5-40bd47680012)


- **Output:**

![image](https://github.com/user-attachments/assets/87f7bfdf-e0e0-41fb-b9a6-4ffdd58afc04)


#### B) `Attendence_save`
Using a live video stream, this performs real-time face recognition to identify He/She. When He/She's face is recognized, his/her name is displayed on the video feed, and the recognition event is logged with the date and time in an Excel file. After every 5 recognitions, the current log is saved to an Excel file, and the recognition counter and DataFrame are reset.

- **Input:**

![mousam_photo](https://github.com/user-attachments/assets/ef6b1a6e-57a9-4b60-a5c5-40bd47680012)

- **Output:**

![image](https://github.com/user-attachments/assets/d902b33c-7639-4a2a-ab97-3706af531af6)


![image](https://github.com/user-attachments/assets/0953d67b-0e85-43ab-b7d5-2a2887aba4fa)


#### C) `test`
This performs real-time face recognition to identify He/She in a live video feed, logging each recognition event with the date and time into an Excel file every 30 seconds. It tracks recognition intervals to avoid duplicate entries and displays He/She or "Not He/She" based on identification.

- **Input:**

![mousam_photo](https://github.com/user-attachments/assets/323fea74-a68d-45bb-905e-64105c64ab98)


- **Output:**

![image](https://github.com/user-attachments/assets/412ad2ad-0468-4976-aed0-5f78486af917)


![image](https://github.com/user-attachments/assets/b37c0bcc-0dd5-420b-bafe-e981e66a91b9)

#### D) `tools`
This performs real-time face recognition using the live camera feed to identify He/She. Each time a face is recognized, it records the name, date, and time in a data frame. Once a recognition count of 5 is reached, it saves the records to an Excel file, then resets the counter and DataFrame. It displays "He/She's name" or "Not He/She's name" over the video feed, and pressing 'q' exits the program with a final save of any remaining records.

- **Input:**

![mousam_photo](https://github.com/user-attachments/assets/ef6b1a6e-57a9-4b60-a5c5-40bd47680012)

- **Output:**

![image](https://github.com/user-attachments/assets/0e67fd69-db4d-49be-88e6-9a331d62ccc5)


![image](https://github.com/user-attachments/assets/f6575fd2-b8fb-4915-8864-90d3de696025)



#### E) `excel_sc`
This is for face recognition with time-based logging looks well-structured and includes the logic to save screenshots and log attendance into an Excel file.

1. **Efficiency**: Resizing frames to 640x480 is good for speed. You can reduce the size further if needed.
2. **File Saving**: Screenshots are saved in `"Teja_screenshots(5)"`, and Excel is updated every 30 seconds.
3. **Recognition Timings**: Logs every 30 seconds for the same person and logs every 5 minutes to avoid multiple entries in short time frames.
4. **Error Handling**: Proper `try-except` block for handling errors.
5. **Termination**: Exits when the 'q' key is pressed.

- **Input:**

![mousam_photo](https://github.com/user-attachments/assets/dfc4223a-39ca-49c4-8a37-e1316e40b8b9)


- **Output:**

![image](https://github.com/user-attachments/assets/5fc7f30e-ce33-4047-8e1a-c31e54c16b6b)


![image](https://github.com/user-attachments/assets/8b5de8b6-4460-40be-b370-ebcb2dc9bfdf)


#### F) `excel_sc_dt`
This uses OpenCV and `face_recognition` to detect and recognize a specific face (His/Her's) from a webcam feed. Upon recognition, a screenshot is saved, and the attendance (name, date, time, screenshot path) is logged into an Excel file. The script processes every second frame, saves data every 30 seconds, and ensures attendance is only logged every 5 minutes for the same person. The attendance data is stored in a DataFrame and periodically exported to an Excel file.

Key Features:
- Real-time face detection and recognition
- Saves screenshots with timestamp
- Logs attendance to Excel every 30 seconds
- Avoids multiple logs within a 5-minute interval for the same person

- **Input:**

![mousam_photo](https://github.com/user-attachments/assets/e9b887a3-c584-41f1-a5a8-5d5c2c9bc3a9)


- **Output:**

![image](https://github.com/user-attachments/assets/b0867453-3e33-4962-b06c-6f9097943284)


![image](https://github.com/user-attachments/assets/ca58f282-39ee-44cd-b6c4-4165d816fb3a)


#### G) `landmark`
This code is a face recognition and attentiveness tracking system that operates in real time. Key functions include:

1. **Face Recognition**: Detects and recognizes "His/Her's face" from the camera using a pre-loaded image.
2. **Attentiveness Detection**: Uses facial landmarks and head pose estimation to assess if the subject is attentive.
3. **Logging**: Records each recognition event with a timestamp, attentiveness status, and screenshot in an Excel file, saving every 30 seconds.
4. **Live Feedback**: Displays "Attentive" or "Not Attentive" on the video feed along with facial landmarks.

The system continues until you press 'q' to exit.

- **Input:**

![teja](https://github.com/user-attachments/assets/8cd23fad-89bb-4962-bc21-930acb518fd0)

- **Output:**

![Guru Teja_2024-11-07_20-16-27](https://github.com/user-attachments/assets/20b1feef-0c90-4832-a128-45268391b394)

![Screenshot 2024-11-13 181911](https://github.com/user-attachments/assets/5de5e452-ba9d-4062-a23b-a02604d9ff3d)

#### H) `atten_score`
This script captures real-time webcam video to recognize "His/Her's face" and assess attentiveness based on head pose:

1. **Setup**: Loads His/Her's face data and initializes detectors.
2. **Face Recognition**: Compares detected faces with the known face, identifying if it's a match.
3. **Attentiveness Check**: Estimates head orientation (yaw/pitch) to compute an attentiveness score.
4. **Logging**: Logs details (name, date, time, attentiveness, screenshot) in an Excel file every 30 seconds if attentive.
5. **Display**: Shows video with face labels, attentiveness status, and facial landmarks. 

Exits on 'q' press, ensuring the final save to Excel.

- **Input:**

![teja](https://github.com/user-attachments/assets/8cd23fad-89bb-4962-bc21-930acb518fd0)

- **Output:**

![Guru Teja_2024-11-07_21-34-50](https://github.com/user-attachments/assets/40f12cd5-c468-459c-a610-395366915ff8)

![Screenshot 2024-11-13 182336](https://github.com/user-attachments/assets/45034df8-9044-4850-b471-ba579c1a942a)

#### I) `avg_atten_score`
This captures webcam video, performs face recognition for "His/Her's face," calculates attentiveness based on the head pose, and logs the data into an Excel file every 30 seconds. Here is a summary of its key actions:

1. **Face Recognition**: Uses `face_recognition` to identify "His/Her's face" by comparing face encodings.
2. **Head Pose Detection**: Calculates the head pose (yaw, pitch) using `dlib`'s facial landmark predictor to assess attentiveness.
3. **Attentiveness Calculation**: Computes an attentiveness score based on yaw and pitch, with values between 0 (not attentive) and 1 (fully attentive).
4. **Logging**: Every 30 seconds, the script saves recognized face data (name, date, time, attentiveness, attention score, and screenshot) into an Excel file.
5. **Display and Feedback**: Shows real-time video with facial landmarks, attentiveness status, and face bounding boxes.

The final output includes an Excel file with logged details and an average attentiveness score at the end of the session. The user can stop the video stream by pressing 'q'.

- **Input:**

![teja](https://github.com/user-attachments/assets/8cd23fad-89bb-4962-bc21-930acb518fd0)

- **Output:**

![Guru Teja_2024-11-07_22-10-43](https://github.com/user-attachments/assets/ace6a953-372a-4297-b598-3aa79f8ef4f3)

![Screenshot 2024-11-13 183057](https://github.com/user-attachments/assets/ad3ba39e-0b64-42f7-836a-2e0f3cacc442)

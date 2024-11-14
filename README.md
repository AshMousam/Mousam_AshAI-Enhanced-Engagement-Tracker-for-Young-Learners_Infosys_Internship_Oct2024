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

![image1](https://github.com/user-attachments/assets/701c01c1-17fe-408e-b030-6113d813aa02)

Output :- 

![Screenshot 2024-11-12 184440](https://github.com/user-attachments/assets/fcb29fb6-e559-4b00-b56e-27c0667ea6dc)

J) image_rgb2gray :- This converts a color image to grayscale using `cv2.cvtColor()` and saves the grayscale version image. The grayscale image is then displayed in a separate window.

Input :- 

![image2](https://github.com/user-attachments/assets/bb3ec4c2-fe8c-43fd-9d54-14ce6f897cef)

Output : - 

![Screenshot 2024-11-12 180732](https://github.com/user-attachments/assets/fcf4a4c2-bda8-48bf-b729-9db743544b74)

K) image_rotate :- This rotates an image by 90 degrees around its center. It first calculates the center point and then creates a rotation matrix with a 90-degree angle. Using `cv2.warpAffine()`, the image is rotated and displayed in a separate window. 

Input :- 

![image2](https://github.com/user-attachments/assets/ff931e78-37ad-40d6-a0df-67d37aa092af)

Output :- 

![Screenshot 2024-11-12 184152](https://github.com/user-attachments/assets/35d20bb4-ab51-464d-bd1e-4d295f5c50c0)

L) image_blur :- This code applies a Gaussian blur to an image using a 15x15 kernel size, which helps in reducing image noise and detail. The blurred image is then displayed in a separate window.

Input :- 

![image1](https://github.com/user-attachments/assets/9052a6fe-fe8e-41f8-a078-6928d5ae0f32) 

Output :- 

![Screenshot 2024-11-12 183920](https://github.com/user-attachments/assets/a0cfade1-69db-48ae-a533-c7512a78e4cc)


M) image_noise removal & closing gaps:- This performs morphological operations on a grayscale image. It first checks if the image is loaded successfully, then defines a kernel matrix to apply:

1. **Opening**: This operation, which combines erosion followed by dilation, is used to remove small noise from the image.
2. **Closing**: This operation, which combines dilation followed by erosion, helps in filling small gaps.

Additionally, it defines a function `display_image()` that uses Matplotlib to display an image with a title in grayscale.

N) image_template:- This code performs template matching to locate a template image within a larger image. The `cv2.matchTemplate()` function is used to find the region in the larger image that best matches the template. It then draws a green rectangle around the matched area.


Video Processing 

Libraries or Frame Works used - opencv 

Version - 4.10.0.84 

Developed Logics - 

A) Video_multivideo :- This reads and displays all images in a specified folder. It iterates over the files in the folder, reads each image using `cv2.imread()`, and checks if the image is successfully loaded. If the image is loaded, it displays the image and prints its dimensions (height, width, and number of channels). If an image fails to load, it prints a message indicating the failure. After displaying each image, it waits for a key press before moving to the next image. 

B) Video_fps :- This captures video from the webcam, displays it in real-time, and calculates the frames per second (FPS) for the video feed. Here's how it works:

Once the video capture is finished, the `cap.release()` and `out.release()` functions are called to release the webcam and the video writer. All OpenCV windows are closed using `cv2.destroyAllWindows()`.

C) Video_save :- This captures live video from the webcam, displays it in real-time, and saves the video to an output file. The video is recorded with a frame rate of a certain FPS and a resolution of given pixels. Press 'q' to stop the recording and close the webcam feed.

D) Video_stack :- This reads two video files, resizes the frames to a resolution of given pixels, and concatenates them horizontally to display both videos side by side in real-time. The concatenated video is shown in a single window. Press 'q' to stop the playback and close the window.

E) Video_stream :- This captures live video from the webcam and displays it in real-time in a window. The video feed continues until the user presses the 'q' key to stop the capture and close the window.


Annotations 

Libraries or Frame Works used - opencv, labelImg

Version - 4.10.0.84, 1.8.6 

Developed Logics - 

A) data_segregate :- This defines a function segregate_images_by_labels that organizes images and their associated label files into matched and unmatched directories.

B) label :- This is used to draw bounding boxes on images based on the annotations in the label files and save the resulting images to an output directory.

C) label_manipulate :- This is a Python function that updates class numbers in label files (typically used for object detection tasks).


Face Recognition

Libraries or Frame Works used - opencv, labelImg, dlib, face_recognition, imutils

Version - 4.10.0.84, 1.8.6, 19.24.6, 1.3.0, 0.5.4

Developed Logics - 

A) Face_recognition
B) Attendence_save
C) test
D) tools
E) excel_sc
F) excel_sc_dt
G) landmark
H) atten_score
I) avg_atten_score

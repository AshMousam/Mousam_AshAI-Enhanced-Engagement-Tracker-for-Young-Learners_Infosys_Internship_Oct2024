import cv2 as cv
import face_recognition

# Load the known image of mousam
known_image = face_recognition.load_image_file("mousam_photo.jpg")
known_faces = face_recognition.face_encodings(known_image, num_jitters=50, model='large')[0]

# Launch the live camera (or video file)
cam = cv.VideoCapture(0)                      #if i need to open my camera and recognisie own face then change image and change video graph make it "0" if check face in video then putit video file in this video path

# Check if the camera or video is opened
if not cam.isOpened():
    print("Camera or video file not working")
    exit()

# Confidence threshold
confidence_threshold = 0.6  # Adjust this value as needed

# When the camera is opened
while True:
    # Capture the image frame-by-frame
    ret, frame = cam.read()

    # Check if frame is reading or not
    if not ret:
        print("Can't receive the frame or end of video reached")
        break

    # Convert the frame from BGR to RGB
    rgb_frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)

    # Face detection in the frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame)

    recognized = False

    for face_encoding, face_location in zip(face_encodings, face_locations):
        # Compute the distance to the known face encoding
        distance = face_recognition.face_distance([known_faces], face_encoding)[0]

        if distance < confidence_threshold:  # Check if the distance is below the threshold
            recognized = True
            top, right, bottom, left = face_location
            cv.rectangle(frame, (left, top), (right, bottom), color=(0, 255, 0), thickness=2)
            frame = cv.putText(frame, 'Mousam', (left, top - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5,
                               (255, 0, 0), 2, cv.LINE_AA)

    if not recognized:
        frame = cv.putText(frame, 'Mousam', (30, 55), cv.FONT_HERSHEY_SIMPLEX, 1,
                           (255, 0, 0), 2, cv.LINE_AA)

    # Display the resulting frame
    cv.imshow('Video Stream', frame)

    # End the streaming
    if cv.waitKey(1) == ord('q'):
        break

# Release the capture
cam.release()
cv.destroyAllWindows()

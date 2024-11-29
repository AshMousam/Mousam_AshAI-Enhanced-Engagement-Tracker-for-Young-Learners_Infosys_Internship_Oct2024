import cv2 as cv
import face_recognition
import dlib
import pandas as pd
import numpy as np
from datetime import datetime
import os
import keyboard
import random
import time
from imutils import face_utils

class StudentMonitoringSystem:
    def __init__(self):
        # Initialize paths and directories
        self.model_path = "E:\python\INFOSYS_INTERNSHIP\code_file\FACE_RECOGNITION\shape_predictor_68_face_landmarks.dat"
        self.known_students_dir = "known_students"
        self.screenshots_dir = "monitoring_screenshots"
        self.logs_dir = "student_logs"
        
        # Create necessary directories
        for directory in [self.known_students_dir, self.screenshots_dir, self.logs_dir]:
            if not os.path.exists(directory):
                os.makedirs(directory)
        
        # Initialize face detection tools
        self.detector = dlib.get_frontal_face_detector()
        self.landmark_predictor = dlib.shape_predictor(self.model_path)
        
        # Load known students
        self.known_faces = {}
        self.known_names = []
        self.load_known_students()
        
        # Initialize student tracking data
        self.student_data = {}
        self.initialize_student_data()
        
        # Parameters for attention monitoring
        self.MAX_YAW_THRESHOLD = 0.5
        self.MAX_PITCH_THRESHOLD = 0.5
        self.KEYBOARD_THRESHOLD = 50  # Maximum allowed keyboard events per minute
        self.last_screenshot_time = {}
        
    def load_known_students(self):
        """Load known students' images and encode their faces"""
        for img_file in os.listdir(self.known_students_dir):
            if img_file.endswith(('.jpg', '.jpeg', '.png')):
                name = img_file.split('.')[0]
                image_path = os.path.join(self.known_students_dir, img_file)
                student_img = face_recognition.load_image_file('E:\python\INFOSYS_INTERNSHIP\code_file\FACE_RECOGNITION\mousam_photo.jpg')
                encoding = face_recognition.face_encodings(student_img, num_jitters=50, model='large')
                
                if encoding:
                    self.known_faces[name] = encoding[0]
                    self.known_names.append(name)
    
    def initialize_student_data(self):
        """Initialize tracking data for each student"""
        for name in self.known_names:
            self.student_data[name] = {
                'login_time': None,
                'logout_time': None,
                'face_missing_count': 0,
                'attention_scores': [],
                'keyboard_events': 0,
                'last_keyboard_check': time.time(),
                'screenshots': []
            }
    
    def calculate_eye_score(self, left_eye, right_eye):
        """Calculate eye openness score based on eye aspect ratio (EAR)"""
        def eye_aspect_ratio(eye):
            # Compute the euclidean distances between the vertical eye landmarks
            A = np.linalg.norm(eye[1] - eye[5])
            B = np.linalg.norm(eye[2] - eye[4])
            # Compute the euclidean distance between the horizontal eye landmarks
            C = np.linalg.norm(eye[0] - eye[3])
            # Compute the eye aspect ratio
            ear = (A + B) / (2.0 * C)
            return ear
        
        # Calculate the eye aspect ratio for both eyes
        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)
        
        # Average the eye aspect ratio
        avg_ear = (left_ear + right_ear) / 2.0
        
        # Convert EAR to a score between 0 and 1
        # Typical EAR values: 0.2 (closed) to 0.3 (open)
        eye_score = min(max((avg_ear - 0.2) / 0.1, 0), 1)
        return eye_score
    
    def calculate_mouth_score(self, mouth):
        """Calculate mouth movement score based on mouth aspect ratio (MAR)"""
        # Calculate vertical distances
        A = np.linalg.norm(mouth[2] - mouth[10])  # Upper lip to lower lip
        B = np.linalg.norm(mouth[4] - mouth[8])   # Upper lip to lower lip
        
        # Calculate horizontal distance
        C = np.linalg.norm(mouth[0] - mouth[6])   # Mouth width
        
        # Calculate mouth aspect ratio
        mar = (A + B) / (2.0 * C)
        
        # Convert MAR to a score between 0 and 1
        # Typical MAR values: 0.1 (closed) to 0.5 (open)
        mouth_score = min(max(1.0 - (mar - 0.1) / 0.4, 0), 1)
        return mouth_score
    
    def calculate_attention_score(self, landmarks):
        """Calculate attention score based on face, eye, and lip movements"""
        # Extract facial features
        (left_eye_start, left_eye_end) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (right_eye_start, right_eye_end) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
        (mouth_start, mouth_end) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]
        
        # Get landmarks for each feature
        left_eye = landmarks[left_eye_start:left_eye_end]
        right_eye = landmarks[right_eye_start:right_eye_end]
        mouth = landmarks[mouth_start:mouth_end]
        
        # Calculate individual scores
        eye_score = self.calculate_eye_score(left_eye, right_eye)
        mouth_score = self.calculate_mouth_score(mouth)
        
        # Weight the scores (you can adjust these weights)
        attention_score = 0.7 * eye_score + 0.3 * mouth_score
        return attention_score
    
    def take_random_screenshot(self, frame, student_name):
        """Take random screenshots of students"""
        current_time = time.time()
        if student_name not in self.last_screenshot_time or \
           current_time - self.last_screenshot_time.get(student_name, 0) > 300:  # 5 minutes
            filename = f"{self.screenshots_dir}/{student_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            cv.imwrite(filename, frame)
            self.student_data[student_name]['screenshots'].append(filename)
            self.last_screenshot_time[student_name] = current_time
    
    def monitor_keyboard_activity(self):
        """Monitor keyboard activity for suspicious behavior"""
        for name in self.known_names:
            current_time = time.time()
            elapsed_time = current_time - self.student_data[name]['last_keyboard_check']
            
            if elapsed_time >= 60:  # Check every minute
                events_per_minute = self.student_data[name]['keyboard_events']
                if events_per_minute > self.KEYBOARD_THRESHOLD:
                    print(f"Warning: High keyboard activity detected for {name}")
                
                self.student_data[name]['keyboard_events'] = 0
                self.student_data[name]['last_keyboard_check'] = current_time
    
    def save_student_logs(self):
        """Save monitoring data to Excel for each student"""
        for name in self.known_names:
            data = self.student_data[name]
            df = pd.DataFrame({
                'Date': [datetime.now().date()],
                'Login Time': [data['login_time']],
                'Logout Time': [data['logout_time']],
                'Face Missing Count': [data['face_missing_count']],
                'Average Attention Score': [np.mean(data['attention_scores']) if data['attention_scores'] else 0],
                'Keyboard Events': [data['keyboard_events']],
                'Screenshots Taken': [len(data['screenshots'])]
            })
            
            excel_path = f"{self.logs_dir}/{name}_log.xlsx"
            df.to_excel(excel_path, index=False)

    def run_monitoring(self):
        """Main monitoring loop"""
        cam = cv.VideoCapture(0)
        if not cam.isOpened():
            print("Camera not working")
            return

        try:
            while True:
                ret, frame = cam.read()
                if not ret:
                    break

                # Detect and process faces
                face_locations = face_recognition.face_locations(frame)
                face_encodings = face_recognition.face_encodings(frame, face_locations)

                # Track present students and unknown faces
                present_students = set()

                for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                    matches = face_recognition.compare_faces(list(self.known_faces.values()), face_encoding)
                    
                    if True in matches:
                        student_idx = matches.index(True)
                        student_name = self.known_names[student_idx]
                        present_students.add(student_name)
                        
                        # Process student presence
                        if self.student_data[student_name]['login_time'] is None:
                            self.student_data[student_name]['login_time'] = datetime.now()
                        
                        # Calculate attention score
                        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                        face_landmarks = self.landmark_predictor(gray, dlib.rectangle(left, top, right, bottom))
                        landmarks = face_utils.shape_to_np(face_landmarks)
                        attention_score = self.calculate_attention_score(landmarks)
                        self.student_data[student_name]['attention_scores'].append(attention_score)
                        
                        # Take random screenshots
                        self.take_random_screenshot(frame, student_name)
                        
                        # Draw rectangle and name
                        cv.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                        cv.putText(frame, f"{student_name} - Attention: {attention_score:.2f}", 
                                 (left, top - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    else:
                        # Unknown face detected
                        cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                        cv.putText(frame, "Unknown Person!", (left, top - 10),
                                 cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                # Update face missing count for absent students
                for name in self.known_names:
                    if name not in present_students:
                        self.student_data[name]['face_missing_count'] += 1

                # Monitor keyboard activity
                self.monitor_keyboard_activity()

                # Display the frame
                cv.imshow("Student Monitoring", frame)
                if cv.waitKey(1) & 0xFF == ord('q'):
                    break

        finally:
            # Save final logs
            for name in self.known_names:
                if self.student_data[name]['login_time'] and not self.student_data[name]['logout_time']:
                    self.student_data[name]['logout_time'] = datetime.now()
            
            self.save_student_logs()
            cam.release()
            cv.destroyAllWindows()

if __name__ == "__main__":
    monitoring_system = StudentMonitoringSystem()
    monitoring_system.run_monitoring() 
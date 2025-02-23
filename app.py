import cv2
import face_recognition
import numpy as np
from supabase_setup.client import supabase
from datetime import datetime

class FaceRecognizer:
    def __init__(self, tolerance=0.6):
        self.tolerance = tolerance
        self.known_encodings = []
        self.known_ids = []
        self.load_employees()
    
    def load_employees(self):
        employees = supabase.get_employees().data
        self.known_encodings = [np.array(emp['face_encoding']) for emp in employees]
        self.known_ids = [emp['id'] for emp in employees]
    
    def process_frame(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_frame = small_frame[:, :, ::-1]
        
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(
                self.known_encodings, 
                face_encoding, 
                tolerance=self.tolerance
            )
            
            if True in matches:
                first_match_index = matches.index(True)
                employee_id = self.known_ids[first_match_index]
                self.log_entry(employee_id)
                
                # Scale back up face locations
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        
        return frame
    
    def log_entry(self, employee_id):
        supabase.log_entry(employee_id)
    
    def run(self):
        video_capture = cv2.VideoCapture(0)
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break
            
            processed_frame = self.process_frame(frame)
            cv2.imshow('FacePass - Entry System', processed_frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    recognizer = FaceRecognizer()
    recognizer.run()

import tkinter as tk
import cv2
import mediapipe as mp
import numpy as np

# Function to open main page
def open_main_page():
    root.withdraw()  # Hide the home page
    main_page.deiconify()  # Show the main page

# Function to execute bicep curl exercise code
def execute_bicep_curl():
    cap = cv2.VideoCapture(0)
    counter = 0 
    stage = None
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils
    
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            results = pose.process(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark

                shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                         landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                         landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                angle = calculate_angle(shoulder, elbow, wrist)

                cv2.putText(image, str(angle), 
                            tuple(np.multiply(elbow, [640, 480]).astype(int)), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                if angle > 160:
                    stage = "down"
                if angle < 30 and stage == 'down':
                    stage = "up"
                    counter += 1
                    print(counter)

            except:
                pass

            cv2.rectangle(image, (0, 0), (225, 73), (245, 117, 16), -1)

            cv2.putText(image, 'REPS', (15, 12), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(counter), 
                        (10, 60), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.putText(image, 'STAGE', (65, 12), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, stage, 
                        (60, 60), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                       mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2), 
                                       mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))

            cv2.imshow('Mediapipe Feed', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
def execute_shoulder_press():
    cap = cv2.VideoCapture(0)
    counter = 0 
    stage = None
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils
    
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            results = pose.process(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark

                left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                 landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                  landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                # Calculate angle between right shoulder, left shoulder, and left wrist
                angle = calculate_angle(left_shoulder, right_shoulder, left_wrist)

                cv2.putText(image, str(angle), 
                            tuple(np.multiply(left_shoulder, [640, 480]).astype(int)), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                if angle < 20:
                    stage = "down"
                if angle > 45 and stage == 'down':
                    stage = "up"
                    counter += 1
                    print(counter)

            except:
                pass

            cv2.rectangle(image, (0, 0), (225, 73), (245, 117, 16), -1)

            cv2.putText(image, 'REPS', (15, 12), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(counter), 
                        (10, 60), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.putText(image, 'STAGE', (65, 12), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, stage, 
                        (60, 60), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                       mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2), 
                                       mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))

            cv2.imshow('Mediapipe Feed', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
def execute_lateral_raises():
    cap = cv2.VideoCapture(0)
    counter = 0 
    stage = None
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils
    
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            results = pose.process(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark

                left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                 landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]

                # Calculate angle between left hip, left shoulder, and left elbow
                angle = calculate_angle(left_hip, left_shoulder, left_elbow)

                cv2.putText(image, str(angle), 
                            tuple(np.multiply(left_shoulder, [640, 480]).astype(int)), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                if angle < 30:
                    stage = "down"
                if angle > 75 and stage == 'down':
                    stage = "up"
                    counter += 1
                    print(counter)

            except:
                pass

            cv2.rectangle(image, (0, 0), (225, 73), (245, 117, 16), -1)

            cv2.putText(image, 'REPS', (15, 12), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(counter), 
                        (10, 60), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.putText(image, 'STAGE', (65, 12), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, stage, 
                        (60, 60), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                       mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2), 
                                       mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))

            cv2.imshow('Mediapipe Feed', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()




# Function to calculate angle
def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle > 180.0:
        angle = 360 - angle
        
    return angle

root = tk.Tk()
root.attributes("-fullscreen", True)  # Make the window full-screen
root.configure(bg="#2c3e50")  # Set background color

# Home page
home_page = tk.Frame(root, bg="#2c3e50")
home_page.pack(expand=True, fill="both")

app_name_label = tk.Label(home_page, text="GYM BUDDY", font=("Helvetica", 48), fg="white", bg="#2c3e50")
app_name_label.pack(pady=50)

get_started_button = tk.Button(home_page, text="Get Started", command=open_main_page, font=("Helvetica", 24), bg="#3498db", fg="white")
get_started_button.pack()

# Main page
# Main page
main_page = tk.Toplevel(root)
main_page.attributes("-fullscreen", True)  # Make the window full-screen
main_page.configure(bg="#2c3e50")  # Set background color
main_page.protocol("WM_DELETE_WINDOW", root.destroy)  # Close both windows when main page is closed
main_page.withdraw()  # Hide main page initially

# Title
title_label = tk.Label(main_page, text="Choose an Exercise", font=("Helvetica", 36), fg="white", bg="#2c3e50")
title_label.pack(pady=20)
exercise_options = ['Bicep Curl', 'Shoulder Press', 'Lateral Raises', 'Front Raises']


# Exercise buttons
for exercise in exercise_options:
    if exercise == 'Bicep Curl':
        exercise_button = tk.Button(main_page, text=exercise, command=execute_bicep_curl, font=("Helvetica", 24), bg="#3498db", fg="white")
    elif exercise == 'Shoulder Press':
        exercise_button = tk.Button(main_page, text=exercise, command=execute_shoulder_press, font=("Helvetica", 24), bg="#3498db", fg="white")
    elif exercise == 'Lateral Raises':
        exercise_button = tk.Button(main_page, text=exercise, command=execute_lateral_raises, font=("Helvetica", 24), bg="#3498db", fg="white")
    else:
        exercise_button = tk.Button(main_page, text=exercise, command=lambda: print("Exercise not implemented yet!"), font=("Helvetica", 24), bg="#3498db", fg="white")
    
    exercise_button.pack(pady=10, padx=50, fill=tk.X)

root.mainloop()

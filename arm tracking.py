import cv2
import mediapipe as mp
import time

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
mp_hands = mp.solutions.hands

# ==== Open the webcam directly ====
cap = cv2.VideoCapture(0)  # Change to 1 or 2 if needed

if not cap.isOpened():
    print("Cannot open camera")
    exit()

# ==== Initialize MediaPipe models ====
pose_confidence = 0.4
hand_confidence = 0.4

mp_pose_model = mp_pose.Pose(min_detection_confidence=pose_confidence, min_tracking_confidence=pose_confidence)
mp_hands_model = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=hand_confidence)

# ==== FPS calculation ====
prev_time = 0

while True:
    success, frame = cap.read()
    if not success:
        print("Ignoring empty frame.")
        continue

    frame = cv2.flip(frame, 1)

    # Resize to increase FPS
    scale_percent = 75
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    frame_resized = cv2.resize(frame, (width, height))

    image = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
    results_pose = mp_pose_model.process(image)
    results_hands = mp_hands_model.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    h, w, _ = image.shape

    color = (0, 0, 255)  # Red

    # ==== Pose landmarks (shoulder, elbow, wrist) ====
    if results_pose.pose_landmarks:
        landmarks = results_pose.pose_landmarks.landmark
        shoulder = landmarks[12]  # Right shoulder
        elbow = landmarks[14]     # Right elbow
        wrist = landmarks[16]     # Right wrist

        cv2.circle(image, (int(shoulder.x * w), int(shoulder.y * h)), 10, color, -1)
        cv2.circle(image, (int(elbow.x * w), int(elbow.y * h)), 10, color, -1)
        cv2.circle(image, (int(wrist.x * w), int(wrist.y * h)), 10, color, -1)

        cv2.line(image, (int(shoulder.x * w), int(shoulder.y * h)),
                        (int(elbow.x * w), int(elbow.y * h)), color, 3)
        cv2.line(image, (int(elbow.x * w), int(elbow.y * h)),
                        (int(wrist.x * w), int(wrist.y * h)), color, 3)

        # Print coordinates
        print("Shoulder (x, y):", int(shoulder.x * w), int(shoulder.y * h))
        print("Elbow    (x, y):", int(elbow.x * w), int(elbow.y * h))
        print("Wrist    (x, y):", int(wrist.x * w), int(wrist.y * h))

    # ==== Hand landmarks (fingers) ====
    if results_hands.multi_hand_landmarks:
        for hand_landmarks in results_hands.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=color, thickness=2, circle_radius=3),
                mp_drawing.DrawingSpec(color=color, thickness=2))

            for i, lm in enumerate(hand_landmarks.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(f"Finger {i}: ({cx}, {cy})")

    # ==== FPS calculation ====
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if prev_time else 0
    prev_time = curr_time

    cv2.putText(image, f'FPS: {int(fps)}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Arm + Fingers Tracking (No Threading)', image)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
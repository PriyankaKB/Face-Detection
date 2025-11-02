import cv2
import ctypes

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start video capture from the webcam
cap = cv2.VideoCapture(0)

# Create the window once, set to window mode and small size, move to bottom right
cv2.namedWindow('Face Detection', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Face Detection', 240, 180)  # Slightly smaller
user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)
cv2.moveWindow('Face Detection', screen_width - 260, screen_height - 220)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame (tuned parameters for better detection)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.05, minNeighbors=3, minSize=(20, 20)
    )

    if len(faces) > 0:
        print("Face detected. Continuing webcam proctoring.")
        warning_shown = False
    else:
        print("Warning: No face detected!")

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the frame with detected faces
    if frame is not None:
        cv2.imshow('Face Detection', frame)
    else:
        print("Frame is None. Unable to display.")

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

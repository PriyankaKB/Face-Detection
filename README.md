# Face-Detection
Recognizes Face in Images and Videos

## Requirements
- Python 3.6+
- OpenCV (opencv-python)

## Installation
1. Clone this repository or download the source code.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Run Face Detection with Webcam
Execute the following command in your terminal:
```bash
C:/Users/pranav/AppData/Local/Programs/Python/Python36-32/python.exe face_detection.py
```
- A window will open showing the webcam feed with detected faces highlighted.
- Press 'q' to exit the window.
- The script will print logs to the terminal:
  - If a face is detected: `Face detected. Continuing webcam proctoring.`
  - If no face is detected: `Warning: No face detected!`

## Files
- `face_detection.py`: Main script for real-time face detection using your webcam, with output logs for proctoring.
- `requirements.txt`: List of required Python packages.

## Notes
- Make sure your webcam is connected and accessible.
- You can modify the script to detect faces in images or video files if needed.

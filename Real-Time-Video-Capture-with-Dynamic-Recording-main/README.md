
# Time Video Capture with Dynamic Recording

Description:

This Python program utilizes OpenCV for real-time video capture from your webcam, coupled with intelligent motion detection and dynamic video recording. It automatically triggers recording upon detecting movement (faces or bodies) and continues until a set timeframe elapses after the movement stops, ensuring you capture relevant footage.

## Features :
* Real-time video streaming: Captures video from your webcam with minimal latency for a smooth viewing experience.

* Motion detection: Leverages pre-trained Haar cascade classifiers to efficiently detect faces and bodies.

* Dynamic recording: Initiates recording when motion is detected and stops after a customizable duration of inactivity.

* Timestamped videos: Generates video file names with timestamps for easy organization and identification.

* Customizable recording duration: Set the desired recording duration after movement stops using the SECONDS_TO_RECORD_AFTER_DETECTION variable.
## Installation

* Clone the repository: Use git clone https://github.com/jefrijebason/Real-Time-Video-Capture-with-Dynamic-Recording.git to clone this repository to your local machine.

* Install dependencies: Run pip install opencv-python in your terminal to install the required OpenCV library.
## Usage:

* Run the script: Execute the script using python real_time_video_capture_dynamic_recording.py (replace with the actual filename if different).

* Webcam access: Grant permission to the script to access your webcam when prompted.

* Recording: The program will continuously monitor the webcam feed. When movement is detected, it will start recording a video and display a message in the console. Recording will stop automatically after the specified duration of inactivity.

* Exit: Press the 'q' key on your keyboard to terminate the program.
## Code Explanation 
The core functionality utilizes OpenCV functions for:

* Webcam access (cv2.VideoCapture)
* Grayscale conversion (cv2.cvtColor) (Potentially for object detection algorithms)
* Face and body detection (cv2.CascadeClassifier.detectMultiScale)
* Video writing (cv2.VideoWriter)

# RGB_COLOR_DETECTION_ALGORITHM_OPENCV

This project demonstrates real-time color analysis of a webcam feed and displays the most prominent color (blue, green, or red) overlaid on the video frame.


## Dependencies

    * OpenCV (cv2)
    
    * NumPy (np)
## Installation

    pip install opencv-python numpy

## CODE EXPLANATION

* Imports libraries: OpenCV (cv2) for video capture and image processing, and NumPy (np) for numerical operations.
* Webcam Capture: Initializes a VideoCapture object to access the webcam.
* Main Loop: Continuously captures frames from the webcam.
* Color Channel Extraction: Extracts blue (B), green (G), and red (R) channels from the captured frame (assuming BGR format).
* Mean Calculation: Calculates the average intensity for each color channel.
* Dominant Color Detection: Determines the most prominent color (blue, green, or red) based on the highest mean value.
* Text Overlay: Overlays the detected color name on the video frame using OpenCV's putText function.
* Frame Display: Displays the frame with the overlaid text.
* Exit: The loop continues until the user presses the 'q' key, at which point the program terminates and releases resources.
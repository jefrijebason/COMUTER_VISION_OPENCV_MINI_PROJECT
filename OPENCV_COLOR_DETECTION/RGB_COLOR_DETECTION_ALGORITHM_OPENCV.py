import cv2
import numpy as np

# Taking the input from webcam
vid = cv2.VideoCapture(0)

# Font for displaying text
font = cv2.FONT_HERSHEY_SIMPLEX

# Loop to capture and process frames
while True:

    # Capturing the current frame
    _, frame = vid.read()

    # Extracting color channels (assuming BGR format)
    b = frame[:, :, 0]  # Blue channel (index 0 for BGR)
    g = frame[:, :, 1]  # Green channel (index 1 for BGR)
    r = frame[:, :, 2]  # Red channel (index 2 for BGR)

    # Computing mean for each channel
    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)

    # Determining most prominent color
    most_prominent_color = None
    if b_mean > g_mean and b_mean > r_mean:
        most_prominent_color = "Blue"
    elif g_mean > r_mean and g_mean > b_mean:
        most_prominent_color = "Green"
    else:
        most_prominent_color = "Red"

    # Displaying the frame with text overlay
    cv2.putText(frame, most_prominent_color, (10, 30), font, 1, (0, 0, 255), 2)  # White text with black outline
    cv2.imshow("frame", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleaning up resources
vid.release()
cv2.destroyAllWindows()

# pip install opencv-python

import cv2
import numpy as np

# Initialize video capture
cap = cv2.VideoCapture(0)

# Create background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    # Read a frame from the video feed
    ret, frame = cap.read()

    # Apply background subtraction
    fgmask = fgbg.apply(frame)

    # Threshold the foreground mask
    _, thresh = cv2.threshold(fgmask, 25, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through contours
    for contour in contours:
        # Calculate contour area
        area = cv2.contourArea(contour)

        # Set a threshold for contour area to filter small contours (noise)
        if area > 500:
            # Draw a bounding box around the detected object
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, 'Intrusion Detected', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Display the result
    cv2.imshow('Intrusion Detection', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

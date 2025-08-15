import cv2
import numpy as np
from pyzbar.pyzbar import decode  # Library for decoding QR codes and barcodes

# Initialize webcam (index 1 — may be external camera)
webcam = cv2.VideoCapture(0)


# Dummy callback function for trackbar (required by OpenCV)
def empty(e):
    pass


# Create a control window for adjusting parameters
cv2.namedWindow(winname="parameters")
cv2.resizeWindow(winname="parameters", width=640, height=50)
cv2.moveWindow(winname="parameters", x=350, y=560)

# Trackbar for adjusting webcam brightness
cv2.createTrackbar("Brightness", "parameters", 50, 100, empty)

# Main loop for reading frames and decoding barcodes
while True:
    # Read a frame from the webcam
    is_successful, frame = webcam.read()
    if is_successful:
        # Get current brightness value from trackbar
        brightness = cv2.getTrackbarPos(trackbarname="Brightness", winname="parameters")

        # Adjust frame brightness based on trackbar value
        frame = cv2.convertScaleAbs(src=frame, alpha=brightness / 50)

        # Decode any barcodes/QR codes in the frame
        barcodes = decode(frame)
        for barcode in barcodes:
            # Extract the data as a UTF-8 string
            data = barcode.data.decode("utf-8")

            # Get the polygon points of the detected code
            points = np.array(object=barcode.polygon, dtype=np.int32)
            points = np.reshape(a=points, newshape=(-1, 1, 2))

            # Draw a bounding polygon around the detected QR/Barcode
            cv2.polylines(
                img=frame, pts=[points], isClosed=True, color=(255, 0, 255), thickness=5
            )

            # Display the decoded data above the detected code
            cv2.putText(
                img=frame,
                text=data,
                org=(barcode.rect[0], barcode.rect[1] - 10),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=0.9,
                color=(255, 0, 255),
                thickness=2,
            )

        # Show the processed webcam feed
        cv2.imshow(winname="webcam", mat=frame)
        cv2.moveWindow(winname="webcam", x=350, y=50)

        # Wait for key press — ESC (27) exits the loop
        key = cv2.waitKey(delay=1)
        if key == 27:
            break
    else:
        break

# Release resources and close windows
webcam.release()
cv2.destroyAllWindows()


import cv2

#640x480
FRAME_WIDTH = 640
FRAME_HEIGHT = 480


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Camera not working")


cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_HEIGHT)

while True:

    frameSuccess, frameBuf = cap.read()

    if not frameSuccess:
        print("Failed to retrieve camera frame, closing program")
        break

    gray = cv2.cvtColor(frameBuf, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Live Feed (grayscale)", gray)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

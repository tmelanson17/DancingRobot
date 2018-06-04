import numpy as np
import cv2

cap = cv2.VideoCapture(0)
i=0
while(True):
    if i >= 100000:
        break
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Write out to file
    # cv2.imwrite("images/%06d.png" % i, gray)

    # Increment counter
    i+=1
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

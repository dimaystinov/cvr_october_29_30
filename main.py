import cv2
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    cv2.imshow('camera', frame)
    key = cv2.waitKey(1)
    if key == ord(" "):
        break
    print(key)
    # print(ret)
    # print(frame)
cv2.destroyAllWindows()
cap.release()



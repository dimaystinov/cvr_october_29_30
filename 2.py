import cv2
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    # print(frame.shape)
    height, width, _ = frame.shape
    x_center = width // 2
    y_center = height // 2
    length = round(0.52 * height)   # 255, 200, 255  Blue, Green, Red
    frame[y_center - length // 2: y_center + length // 2, x_center - length // 2: x_center + length // 2,0 ] = 255
    cv2.imshow('camera', frame)
    key = cv2.waitKey(1)
    if key == ord(" "):
        break

    # print(key)
    # print(ret)
    # print(frame)
cv2.destroyAllWindows()
cap.release()



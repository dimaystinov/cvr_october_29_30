from ultralytics import YOLO
import cv2
from pprint import pprint
from ultralytics.utils.plotting import Annotator  # ultralytics.yolo.utils.plotting is deprecated

model = YOLO('yolov8n.pt') #  yolov8n.pt
cap = cv2.VideoCapture(1)
pprint(model.names)

# exit()

while True:
    _, img = cap.read()

    # BGR to RGB conversion is performed under the hood
    # see: https://github.com/ultralytics/ultralytics/issues/2575
    results = model.predict(img)

    for r in results:

        annotator = Annotator(img)

        boxes = r.boxes
        for box in boxes:
            # print(box)
            b = box.xyxy[0]  # get box coordinates in (top, left, bottom, right) format
            c = box.cls
            print(b)

            (top, left, bottom, right) = b.numpy().astype(int)



            if model.names[int(c)] == 'person':
                # annotator.box_label(b, model.names[int(c)])
                img[ left:left + right , top:top + bottom, 0] = 255
                # print(type(model.names))

    img = annotator.result()
    cv2.imshow('YOLO V8 Detection', img)
    # print(img)

    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

cap.release()
cv2.destroyAllWindows()
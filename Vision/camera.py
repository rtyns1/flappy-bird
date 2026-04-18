import cv2

#general skeleton for opening camera i found in google, plus this is the go to opening camera blueprint
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error, cannot open camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error, cannot read camera frame")
        break

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1)& 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()



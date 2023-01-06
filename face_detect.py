import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    faces = face_cascade.detectMultiScale(
        frame, scaleFactor=2.1, minNeighbors=5) #ukuran rectangular deteksi wajah
    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow('Face Detector', frame)

    key = cv2.waitKey(20) # time jeda ketika tombol kontrol stop dieksekusi

    if key == ord('3'): #tombol kontrolstop detect / running program
        break

video.release()
cv2.destroyAllWindows()

import cv2 as cv
# reading images

me = cv.imread('photos/photo_6004438364155130791_x.jpg')
cv.imshow("image", me)

cv.waitKey(0)


# reading videos

capture = cv.VideoCapture("videos/JOE METTLE -  NEW COVENANT ASSEMBLY, CALGARY (Full Ministration).mp4")

while True:
    isTrue, frame = capture.read()

    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()

cv.destroyAllWindows()
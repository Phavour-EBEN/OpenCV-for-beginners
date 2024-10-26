# resize and rescale of image/video

img = cv.imread('photos\photo_5878501912922403677_x.jpg')
cv.imshow("Image", img)


# resized function

def resized_image(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    resized_img = cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    return resized_img
# for scaling images
cv.imshow("resized_image", resized_image(img))

video = cv.VideoCapture('videos/Kofi Karikari - Meda Wase.mp4')
while True:
    isTrue,  frame = video.read()
    if not isTrue:
        break
    cv.imshow("video", frame)
    # for scaling videos
    resized_img = resized_image(frame)
    cv.imshow("resized_image", resized_img)

    if cv.waitKey(20) & 0xFF ==ord("q"):
        break
video.release()
cv.destroyAllWindows()

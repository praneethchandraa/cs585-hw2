import cv2


def snap(saveLoc):
    """
    Taken and edited from https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv

    The function captures and save a frame from a live video feed to a given location on hitting space

    """


    cam = cv2.VideoCapture(0)

    cv2.namedWindow("Cam Feed")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("frame", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = saveLoc + "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()
    cv2.destroyAllWindows()


def displayImage(arr):
    
    cv2.imshow('image', arr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return
import cv2
def takesnapshot():
    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videocaptureobject.read()
        #a,b,c = 3,2,1,4
        cv2.imwrite("pic.jpg", frame)
        result = False
    videocaptureobject.release()
    cv2.destroyAllWindows()
takesnapshot()

import cv2 
#http://user:password@ip/video.cgi
cap = cv2.VideoCapture("http://admin:0@192.168.0.7/video.cgi")

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
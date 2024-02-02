import cv2

img = cv2.imread("4f.jpg")

gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray,1.5,4)
print(len(faces))

for (x,y,w,h) in faces:
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,250),1)
       as_region_of_interest=img[y:y+h,x:x+w]

             
cv2.imshow('img',img)
cv2.imshow('img1',as_region_of_interest)
cv2.waitKey(10**5)


#When we are subtracting two different images to extract the desired region 
import cv2
 
# reading the images
circle = cv2.imread('/Users/namitajain/Desktop/001.jpeg')
star = cv2.imread('/Users/namitajain/Desktop/002.jpeg')
 
# subtract the images
subtracted = cv2.subtract(star, circle)
 
# TO show the outputC:\proj_img
cv2.imshow('image', subtracted)
 
# To close the window
cv2.waitKey(0)
cv2.destroyAllWindows()




#When we are subtracting similar images we get nothing which proves this could be one of the successful approach to extract the weak number.
import cv2
 
# reading the images
circle = cv2.imread('/Users/namitajain/Desktop/001.jpeg')
star = cv2.imread('/Users/namitajain/Desktop/001.jpeg')
 
# subtract the images
subtracted = cv2.subtract(star, circle)
 
# TO show the outputC:\proj_img
cv2.imshow('image', subtracted)
 
# To close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
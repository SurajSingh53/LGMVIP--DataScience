# Beginner Level Task 04 - Image to pencil sketch with Python.
# By - Suraj Singh
# 2nd year CSE at Walchand Institute of Technology

# Importing libraries
import cv2
#Loading the image.
img = cv2.imread( 'sample.jpg' )
cv2.imshow( 'Original Image' , img )
cv2.waitKey(0)

# Applying Grayscale.
gray_img = cv2.cvtColor( img , cv2.COLOR_BGR2GRAY )
cv2.imshow( 'GrayScale Image' , gray_img )
cv2.waitKey(0)

#Inverting the grayscaled image.
invert_img = 255 - gray_img
cv2.imshow( 'Inverted Image' , invert_img )
cv2.waitKey(0)

# Ceating blur and inverting it.
blur = cv2.GaussianBlur( invert_img , (21,21) , -1 )
inv_blur = 255 - blur

# Applying Divide function to obtain final image.
sketch = cv2.divide( gray_img , inv_blur , scale = 240)
cv2.imshow('Sketch', sketch)
cv2.imwrite('sampleSketch.jpg',sketch)
cv2.waitKey(0)
# End of the code
# THANK YOU

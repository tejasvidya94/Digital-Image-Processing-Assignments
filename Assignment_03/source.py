# Q.Separate the rectangle from the image using the thresholding from openCV.
import cv2
import numpy as np

# Read the image in grayscale
image = cv2.imread('./Assignment_03/sample.png', cv2.IMREAD_GRAYSCALE)

# Check if image is loaded
if image is None:
    print("Error: Wrong path")
    exit()

# use _ to store the thresold value and thresh for storing the resultant image
_, thresh = cv2.threshold(image, 128, 240, cv2.THRESH_BINARY)

# display original and converted image.
cv2.imshow("Original Image", image)
cv2.imshow("Thresholded Rectangle", thresh)

# wait and then close window
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the modified image
cv2.imwrite('./Assignment_03/converted_image.jpg', thresh)

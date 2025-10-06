# Q.Convert the image to grayscale using the opencv.

import cv2 

# read the image using cv2
image = cv2.imread('sample.jpg')
# check if any error while loading the image.
if image is None:
    print("Error: Image does not found.")
    exit()

# Display original image
cv2.imshow('Original Image',image)
cv2.waitKey(0)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display modified image
cv2.imshow('Grayscale Image',gray_image)
cv2.waitkey(0)
cv2.destroyAllWindows()

# Save the modified image
cv2.imwrite('converted_image.jpg',gray_image)


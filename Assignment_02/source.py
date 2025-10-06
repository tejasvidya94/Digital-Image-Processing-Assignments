import cv2

# Read image default mode
image = cv2.imread("sample.jpg")

# check if the image is loaded successfully
if image is None:
    raise FileNotFoundError("Image File not found.")

# create a negative image
negative_image = 255 - image

# Display input and output image
cv2.imshow('Original image', image)
cv2.imshow('Negative Image', negative_image)

# wait and then close window
cv2.wait(0)
cv2.destroyAllWindows()

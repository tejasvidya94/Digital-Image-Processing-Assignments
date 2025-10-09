# Q. implement code for clipping using openCV and numpy

import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread("./Assignment_04/sample.jpg", cv2.IMREAD_GRAYSCALE)

# Check if image is loaded
if image is None:
    print("Error: Wrong path")
    exit()

# Define clipping range
min_val = 10
max_val = 150

# Create a copy to hold the clipped result
clipped_black = np.zeros_like(image)

# Keep only pixels within the range
clipped_black[(image >= min_val) & (image <= max_val)
              ] = image[(image >= min_val) & (image <= max_val)]

# Display results
cv2.imshow("Original Image", image)
cv2.imshow("Clipped (Outside Black) Image", clipped_black)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save output
cv2.imwrite("./Assignment_04/converted_image.jpg", clipped_black)


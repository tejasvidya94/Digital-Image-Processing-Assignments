import cv2
import numpy as np

# Load the  image
image = cv2.imread('./Assignment_05/sample.webp', cv2.IMREAD_GRAYSCALE)

# Check if image is loaded
if image is None:
    print("Error: Image not found")
    exit()


# Function to get bit planes of a grayscale image
def bit_plane_slicing(gray_img):
    planes = []
    for i in range(8):
        plane = cv2.bitwise_and(gray_img, 1 << i)
        plane = plane * 255 // (1 << i)
        planes.append(plane)
    return planes


# Get bit planes
bit_planes = bit_plane_slicing(image)
print(bit_planes[0])


# Stack all bit planes horizontally for display
bit_planes_stacked = np.hstack(bit_planes)

# Show results
cv2.imshow("Gray Image Bit Plane no: 0", bit_planes[0])
cv2.imshow("Gray Image Bit Planes", bit_planes_stacked)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save output
cv2.imwrite("./Assignment_05/converted_image.jpg", bit_planes_stacked)

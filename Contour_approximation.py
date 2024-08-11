import cv2
import numpy as np

# Load the image
image = cv2.imread('path to image')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a threshold to get a binary image
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours in the binary image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop over the contours and approximate them
for contour in contours:
    # Calculate the perimeter of the contour
    epsilon = 0.02 * cv2.arcLength(contour, True)
    # Approximate the contour
    approx = cv2.approxPolyDP(contour, epsilon, True)
    # Draw the approximated contour on the image
    cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)

# Save or display the corrected image
cv2.imwrite('corrected_image.png', image)
cv2_imshow( image)
cv2.waitKey(0)
cv2.destroyAllWindows()

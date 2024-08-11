import cv2
import numpy as np
from google.colab.patches import cv2_imshow
# Step 1: Load the image
image = cv2.imread('path to the image')
original_image = image.copy()

# Step 2: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply edge detection
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Step 4: Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Step 5: Fit curves and complete the incomplete ones
for contour in contours:
    if len(contour) > 5:
        # Fit an ellipse to the contour
        ellipse = cv2.fitEllipse(contour)
        cv2.ellipse(original_image, ellipse, (0, 255, 0), 5)

# Step 6: Draw the complete curves on the image
cv2_imshow(original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the result
cv2.imwrite('completed_curves.jpg', original_image)
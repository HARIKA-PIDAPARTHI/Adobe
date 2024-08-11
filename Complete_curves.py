import cv2
import numpy as np

def complete_incomplete_curves(image_path):
    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a mask for inpainting
    mask = np.zeros_like(gray)

    # Draw the detected contours on the mask
    for contour in contours:
        cv2.drawContours(mask, [contour], -1, 255, 1)

    # Inpainting to complete the curves
    completed_image = cv2.inpaint(image, mask, inpaintRadius=10, flags=cv2.INPAINT_TELEA)

    # Display the results
    cv2_imshow( image)
    cv2_imshow( mask)
    cv2_imshow( completed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Main function
if __name__ == "__main__":
    image_path = "path to the image"
    complete_incomplete_curves(image_path)
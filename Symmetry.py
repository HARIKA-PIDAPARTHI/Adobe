import cv2
import numpy as np

# Function to identify and count symmetric curves
def detect_symmetric_curves(image_path):
    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection
    edged = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize symmetric curve count
    symmetric_curve_count = 0

    # Loop over each contour
    for contour in contours:
        # Create a mask from the contour
        mask = np.zeros_like(gray)
        cv2.drawContours(mask, [contour], -1, 255, -1)

        # Get the bounding box and extract the ROI
        x, y, w, h = cv2.boundingRect(contour)
        roi = mask[y:y+h, x:x+w]

        # Flip the ROI horizontally and vertically
        roi_flipped_horizontally = cv2.flip(roi, 1)
        roi_flipped_vertically = cv2.flip(roi, 0)

        # Compare original ROI with its flipped versions
        horizontal_symmetry = np.sum(roi == roi_flipped_horizontally) / roi.size
        vertical_symmetry = np.sum(roi == roi_flipped_vertically) / roi.size

        # Consider a contour symmetric if it is sufficiently similar to its flipped version
        if horizontal_symmetry > 0.9 or vertical_symmetry > 0.9:
            symmetric_curve_count += 1
            cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

    # Print the number of symmetric curves detected
    print(f"Number of symmetric curves detected: {symmetric_curve_count}")

    # Display the output image
    cv2_imshow( image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Main function
if __name__ == "__main__":
    image_path = "path to the image" 
    detect_symmetric_curves(image_path)
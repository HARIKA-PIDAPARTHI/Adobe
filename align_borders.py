import cv2
import numpy as np

def align_borders(image_path):
    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a copy of the image for drawing aligned shapes
    aligned_image = image.copy()

    for contour in contours:
        # Approximate the contour to a polygon
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Get the bounding box for the contour
        x, y, w, h = cv2.boundingRect(approx)

        # Draw the original contour
        cv2.drawContours(aligned_image, [approx], -1, (0, 255, 0), 2)

        # Draw the bounding box
        cv2.rectangle(aligned_image, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Align borders to the nearest axis
        # Calculate the center of the bounding box
        center_x = x + w // 2
        center_y = y + h // 2

        # Calculate new aligned coordinates
        new_x = x
        new_y = y

        # Round the center coordinates to align the rectangle
        new_x = (center_x - (center_x % w))
        new_y = (center_y - (center_y % h))

        # Draw the aligned rectangle
        aligned_box = (new_x, new_y, w, h)
        cv2.rectangle(aligned_image, (new_x, new_y), (new_x + w, new_y + h), (0, 0, 255), 2)

    # Display the results
    cv2_imshow( image)
    cv2_imshow(aligned_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Main function
if __name__ == "__main__":
    image_path = "path to the image" 
    align_borders(image_path)
import cv2
import numpy as np

# Function to detect shapes and count them
def detect_shapes(image_path):
    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection
    edged = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dictionary to count shapes
    shape_counts = {
        "Triangle": 0,
        "Square": 0,
        "Rectangle": 0,
        "Pentagon": 0,
        "Hexagon": 0,
        "Circle": 0
    }

    # Loop over the contours
    for contour in contours:
        # Approximate the contour
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.04 * peri, True)

        # Get the bounding box for the contour
        x, y, w, h = cv2.boundingRect(approx)

        # Determine the shape
        if len(approx) == 3:
            shape = "Triangle"
        elif len(approx) == 4:
            aspect_ratio = w / float(h)
            if 0.95 <= aspect_ratio <= 1.05:
                shape = "Square"
            else:
                shape = "Rectangle"
        elif len(approx) == 5:
            shape = "Pentagon"
        elif len(approx) == 6:
            shape = "Hexagon"
        else:
            shape = "Circle"

        # Update the shape count
        shape_counts[shape] += 1

        # Draw the contour and label the shape
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
        cv2.putText(image, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Display the counts of each shape
    for shape, count in shape_counts.items():
        print(f"{shape}: {count}")

    # Display the output image
    cv2_imshow( image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Main function
if __name__ == "__main__":
    image_path = "Path to the image"
    detect_shapes(image_path)
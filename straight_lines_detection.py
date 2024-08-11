import cv2
import numpy as np

# Function to detect and count straight lines
def detect_and_count_straight_lines(image_path):
    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection
    edged = cv2.Canny(blurred, 50, 150)

    # Hough Line Transform to detect lines
    lines = cv2.HoughLinesP(edged, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)

    # Initialize the line count
    line_count = 0

    # Draw the detected lines on the image
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            line_count += 1

    # Print the count of detected lines
    print(f"Number of straight lines detected: {line_count}")

    # Display the output image
    cv2_imshow( image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Main function
if __name__ == "__main__":
    image_path = "path to image" 
    detect_and_count_straight_lines(image_path)
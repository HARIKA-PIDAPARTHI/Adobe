import cv2
import numpy as np

def regularize_curves(image_path):
    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create an empty image for drawing the regularized curves
    regularized_image = np.zeros_like(image)

    # Process each contour to regularize the curves
    for contour in contours:
        # Approximate the contour to a polygon to reduce the number of points
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx_curve = cv2.approxPolyDP(contour, epsilon, True)

        # Draw the approximated curve
        cv2.drawContours(regularized_image, [approx_curve], -1, (0, 255, 0), 2)

        # Optionally, smooth the curve using a polynomial fit
        if len(approx_curve) >= 3:  # At least 3 points needed to fit a polynomial
            points = np.array([pt[0] for pt in approx_curve], dtype=np.float32)
            if points.shape[0] > 2:
                # Fit a polynomial of degree 2 (quadratic) to the points
                z = np.polyfit(points[:, 0], points[:, 1], 2)
                p = np.poly1d(z)
                x = np.linspace(points[:, 0].min(), points[:, 0].max(), num=100)
                y = p(x)
                smooth_curve = np.vstack((x, y)).T.astype(np.int32)
                for i in range(len(smooth_curve) - 1):
                    cv2.line(regularized_image, tuple(smooth_curve[i]), tuple(smooth_curve[i+1]), (255, 0, 0), 2)

    # Display the results
    cv2_imshow(image)
    cv2_imshow(regularized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Main function
if __name__ == "__main__":
    image_path = "path to the image"  
    regularize_curves(image_path)

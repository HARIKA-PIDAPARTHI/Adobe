import cv2
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Preprocessing the image
def preprocess_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, thresholded = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
    edges = cv2.Canny(thresholded, 50, 150)
    return edges

# Extracting the contours
def extract_contours(edges):
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour = max(contours, key=cv2.contourArea)  # Get the largest contour
    contour = contour.reshape(-1, 2)  # Reshape for easier handling
    return contour

# Bézier curve function
def bezier_curve(t, p0, p1, p2, p3):
    return (1 - t)**3 * p0 + 3 * (1 - t)**2 * t * p1 + 3 * (1 - t) * t**2 * p2 + t**3 * p3

# Fitting the Bézier curve
def fit_bezier(contour):
    t = np.linspace(0, 1, len(contour))  # Parameter t
    x, y = contour[:, 0], contour[:, 1]  # Contour coordinates

    # Initial guess for the control points
    p0 = contour[0]
    p3 = contour[-1]
    p1 = (2/3 * p0 + 1/3 * p3)
    p2 = (1/3 * p0 + 2/3 * p3)

    popt_x, _ = curve_fit(lambda t, p1, p2: bezier_curve(t, p0[0], p1, p2, p3[0]), t, x, p0=[p1[0], p2[0]])
    popt_y, _ = curve_fit(lambda t, p1, p2: bezier_curve(t, p0[1], p1, p2, p3[1]), t, y, p0=[p1[1], p2[1]])

    return p0, [popt_x[0], popt_y[0]], [popt_x[1], popt_y[1]], p3

# Plotting the results
def plot_results(contour, bezier_points):
    t = np.linspace(0, 1, 100)
    bezier_x = bezier_curve(t, bezier_points[0][0], bezier_points[1][0], bezier_points[2][0], bezier_points[3][0])
    bezier_y = bezier_curve(t, bezier_points[0][1], bezier_points[1][1], bezier_points[2][1], bezier_points[3][1])

    plt.plot(contour[:, 0], contour[:, 1], 'ro', label='Contour points')
    plt.plot(bezier_x, bezier_y, 'b-', label='Fitted Bézier curve')
    plt.legend()
    plt.show()

# Main function
def main(image_path):
    edges = preprocess_image(image_path)
    contour = extract_contours(edges)
    bezier_points = fit_bezier(contour)
    plot_results(contour, bezier_points)

# Run the main function
image_path = 'path to the image'
main(image_path)